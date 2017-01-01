import ast_visitor

class FormatVisitor(ast_visitor.AstVisitor):
    """
    Use this after GenDataVisitor
    """
    def __init__(self):
        super(FormatVisitor, self).__init__()
        self.func_dict = {
            "table_definition" : self.table_definition
        }

    def miss_func(self, node, *args, **kwargs):
        pass

    def table_definition(self, node, *args, **kwargs):
        code = 'CREATE TABLE'
        if node.childs[2].data is not None:
            code += ' ' + node.childs[2].data
        code += ' ' + node.childs[3].data + ' (\n'
        for name, datatype, comment in node.childs[5].data:
            code += '    ' + name + ' ' + datatype + ' COMMENT \"'
            if comment is None:
                code += '\"'
            else:
                code += comment[1:-1] + '\"'
            code += ',\n'
        code = code[0:-2] + "\n)"
        if node.childs[7].data is not None:
            code += '\nCOMMENT \"' + node.childs[7].data[1:-1] + '\"'
        if node.childs[8].data is not None:
            code += '\nPARTITIONED BY (\n'
            for name, datatype, comment in node.childs[8].data:
                code += '    ' + name + ' ' + datatype + ' COMMENT \"'
                if comment is None:
                    code += '\"'
                else:
                    code += comment[1:-1] + '\"'
                code += ',\n'
            code = code[0:-2] + "\n)"
        if node.childs[9].data is not None:
            code += '\nLIFECYCLE ' + str(node.childs[9].data)
        code += ';'
        kwargs['result'].append(code)





            