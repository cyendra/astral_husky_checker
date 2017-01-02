
class AstVisitor(object):
    def __init__(self):
        self.func_dict = {
        }

    def miss_func(self, node, *args, **kwargs):
        pass

    def dispatch(self, node, *args, **kwargs):
        if self.func_dict.has_key(node.type):
            f = self.func_dict.get(node.type, None)
            f(node, *args, **kwargs)
        elif hasattr(self, node.type):
            f = getattr(self, node.type)
            f(node, *args, **kwargs)
        else:
            self.miss_func(node, *args, **kwargs)

    def pre_order_visit(self, node, *args, **kwargs):
        self.dispatch(self, node, *args, **kwargs)
        for child in node.childs:
            if hasattr(child, 'visit'):
                self.pre_order_visit(child, *args, **kwargs)

    def post_order_visit(self, node, *args, **kwargs):
        for child in node.childs:
            if hasattr(child, 'visit'):
                self.post_order_visit(child, *args, **kwargs)
        self.dispatch(node, *args, **kwargs)

    def visit(self, node, *args, **kwargs):
        self.dispatch(node, *args, **kwargs)