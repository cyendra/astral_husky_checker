import ast_visitor

class GenDataVisitor(ast_visitor.AstVisitor):
    def __init__(self):
        super(GenDataVisitor, self).__init__()
        self.func_dict = {
            "table_comment" : self.table_comment,
            "table_col_term" : self.table_col_term,
            "table_col_list" : self.table_col_list,
            "table_partitioned" : self.table_partitioned,
            "table_lifecycle" : self.table_lifecycle,
            "if_not_exists" : self.if_not_exists,
            "table_name" : self.table_name
        }

    def visit(self, node, *args, **kwargs):
        self.post_order_visit(node, *args, **kwargs)

    def table_name(self, node, *args, **kwargs):
        node.data = ''.join(node.childs)

    def if_not_exists(self, node, *args, **kwargs):
        if len(node.childs) == 3:
            node.data = ' '.join(node.childs)

    def table_comment(self, node, *args, **kwargs):
        if len(node.childs) == 2:
            node.data = node.childs[1]

    def table_col_term(self, node, *args, **kwargs):
        node.data = (node.childs[0], node.childs[1], node.childs[2].data)

    def table_col_list(self, node, *args, **kwargs):
        if len(node.childs) == 1:
            node.data = [node.childs[0].data]
        elif len(node.childs) == 3:
            node.data = node.childs[0].data + [node.childs[2].data]

    def table_partitioned(self, node, *args, **kwargs):
        if len(node.childs) == 5:
            node.data = node.childs[3].data    

    def table_lifecycle(self, node, *args, **kwargs):
        if len(node.childs) == 2:
            node.data = node.childs[1]

            