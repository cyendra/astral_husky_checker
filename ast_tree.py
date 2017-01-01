import collections

class Node(object):

    def __init__(self, asttype = "AST_ROOT", value = None):
        self.childs = collections.deque()
        self.type = asttype
        self.value = value

    def add(self, obj):
        self.childs.append(obj)
