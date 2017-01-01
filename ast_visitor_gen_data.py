
class GenDataVisitor(object):
    def __init__(self):
        self.func_dict = {
            "table_comment" : self.table_comment,
            "table_col_term" : self.table_col_term,
            "table_col_list" : self.table_col_list,
            "table_partitioned" : self.table_partitioned,
            "table_lifecycle" : self.table_lifecycle
        }

    def visit(self, node):
        f = self.func_dict.get(node.type, None)
        if f is not None:
            f(node)

    def table_comment(self, node):
        if len(node.childs) == 2:
            node.data = node.childs[1]

    def table_col_term(self, node):
        node.data = (node.childs[0], node.childs[1], node.childs[2].data)

    def table_col_list(self, node):
        if len(node.childs) == 1:
            node.data = [node.childs[0].data]
        elif len(node.childs) == 3:
            node.data = node.childs[0].data + [node.childs[2].data]

    def table_partitioned(self, node):
        node.data = node.childs[3].data    

    def table_lifecycle(self, node):
        node.data = node.childs[1]

            