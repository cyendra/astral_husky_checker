import collections

class Node(object):

    def __init__(self, asttype = "AST_ROOT", data = None):
        self.childs = collections.deque()
        self.type = asttype
        self.data = data

    def add(self, obj):
        self.childs.append(obj)

    def visit(self, visitor, *args, **kwargs):
        visitor.visit(self, *args, **kwargs)

    def debug(self, idx=0, tab=""):
        print tab, idx, self.type, self.data
        if self.childs is not None:
            for i in range(len(self.childs)):
                if type(self.childs[i]) is Node:
                    self.childs[i].debug(i, tab+"  ")
                else:
                    print tab+"  ", i, self.childs[i], type(self.childs[i])

