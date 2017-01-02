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


    def _merge_line_expr(self, line):
        code = ''
        for i in range(len(line)):
            tok = line[i]
            if type(tok) is tuple:
                tp = tok[0]
                if tp == 'func':
                    name = tok[1]
                    value_list = tok[2]
                    tok = name + '({0})'.format(self._merge_para_expr(value_list))
            s = str(tok)
            if i == 0:
                code += s
            elif line[i-1] == '(' :
                code += s
            elif s == ')':
                code += s 
            else:
                code += ' ' + s
        return code

    def _merge_para_expr(self, line):
        code = ''
        for i in range(len(line)):
            s = self._merge_line_expr(line[i])
            if i != 0:
                code += ', '
            code += s
        return code

    def select_stmt(self, node, *args, **kwargs):
        tab = kwargs.get('tab', "")
        code = tab + 'SELECT'
        if node.childs[1].data is not None:
            code += ' ' + node.childs[1].data 
        code += ' '
        for i in range(len(node.childs[2].data)):
            item = node.childs[2].data[i]
            if i > 0:
                code += '\n' + tab + '    ' + ', '
            if type(item[0]) is list:
                code += self._merge_line_expr(item[0])
            if item[1] is not None:
                code += ' AS ' + item[1]
        code += '\n' + tab + 'FROM'
        if node.childs[4].childs[0] == '(':
            rs = []
            node.childs[4].childs[1].visit(self, tab=tab + '    ', result=rs)
            code += ' (\n' + rs[0] + '\n' + tab + ')'
            if node.childs[4].childs[3].data is not None:
                code += ' ' + node.childs[4].childs[3].data 
        else:
            code += ' ' + node.childs[4].childs[0].data
            if node.childs[4].childs[1].data is not None:
                code += ' ' + node.childs[4].childs[1].data
        if node.childs[5].data is not None:
            code += '\n' + tab + 'WHERE '
            code += self._merge_line_expr(node.childs[5].data)

        if node.childs[7].data is not None:
            code += '\n' + tab + 'ORDER BY '
            for i in range(len(node.childs[7].data)):
                item = node.childs[7].data[i]
                if i > 0:
                    code += '\n' + tab + '    ' + ', '
                if type(item[0]) is list:
                    code += self._merge_line_expr(item[0])
                if item[1] is not None:
                    code += ' ' + item[1]
        if node.childs[9].data is not None:
            code += '\n' + tab + 'LIMIT '
            code += str(node.childs[9].data)

        kwargs['result'].append(code)

 
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
        kwargs['result'].append(code)





            