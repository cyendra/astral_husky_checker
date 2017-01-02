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
            "table_name" : self.table_name,
            "all_or_distinct" : self.all_or_distinct,
            "simple_expr" : self.simple_expr
        }

    def visit(self, node, *args, **kwargs):
        self.post_order_visit(node, *args, **kwargs)

#------------------

    def limit_stmt(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 2:
            node.data = node.childs[1]

    def order_stmt(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 3:
            node.data = node.childs[2].data

    def order_condition(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 1:
            node.data = [node.childs[0].data]
        elif n == 3:
            node.data = node.childs[0].data + [node.childs[2].data]        

    def order_expr(self, node, *args, **kwargs):
        if len(node.childs) == 1:
            node.data = (node.childs[0].data, None)
        elif len(node.childs) == 2:
            node.data = (node.childs[0].data, node.childs[1])

    def where_condition(self, node, *args, **kwargs):
        node.data = node.childs[0].data

    def where_stmt(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 2:
            node.data = node.childs[1].data

    def table_other_name(self, node, *args, **kwargs):
        node.data = node.childs[0]

    def symbol_expr(self, node, *args, **kwargs):
        node.data = node.childs[0]

    def select_expr_list(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 1:
            node.data = [node.childs[0].data]
        elif n == 3:
            node.data = node.childs[0].data + [node.childs[2].data]

    def func_expr(self, node, *args, **kwargs):
        node.data = ('func', node.childs[0], node.childs[2].data)

    def expr_list(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 1:
            node.data = [node.childs[0].data]
        elif n == 3:
            node.data = node.childs[0].data + [node.childs[2].data]

    def factor_expr(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 3:
            node.data = ['('] + node.childs[1].data + [')']
        elif n == 1:
            node.data = [node.childs[0].data]

    def simple_expr(self, node, *args, **kwargs):
        if hasattr(node.childs[0], 'data'):
            node.data = node.childs[0].data
        else:
            node.data = node.childs[0]

    def line_expr(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 1:
            node.data = node.childs[0].data
        elif n == 2:
            node.data = node.childs[0].data + node.childs[1].data

    def select_expr(self, node, *args, **kwargs):
        n = len(node.childs)
        if n == 1:
            node.data = (node.childs[0].data, None)
        elif n == 3:
            node.data = (node.childs[0].data, node.childs[2])

    def all_or_distinct(self, node, *args, **kwargs):
        node.data = node.childs[0]

#-----------------------

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

            