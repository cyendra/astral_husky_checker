# -*- coding: utf-8 -*-
#pylint: disable=maybe-no-member

import lxml.etree as xml
import collections


class JobConf(object):

    _catch = {}
    
    def __init__(self, filename=None):
        self.para = {}
        self.parents = []
        if filename is not None:
            self.open(filename)
    
    def open(self, filename):
        if self._catch.has_key(filename):
            return self._catch.get(filename)
        doc = xml.parse(filename)
        terms = doc.findall("")
        for term in terms:
            name = term.find("name").text
            value = term.find("value").text
            self.para[name] = value
        self._catch[filename] = self
    
    def get(self, name):
        return self.para.get(name)

    def find(self, name):
        if self.para.has_key(name):
            return self.para[name]
        queue = collections.deque()
        for p in self.parents:
            queue.append(p)
        while len(queue) > 0:
            p = queue.popleft()
            rs = p.get(name)
            if rs is not None:
                return rs
            queue.extend(p.parents)
        return None


