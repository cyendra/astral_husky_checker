import sys
import parser
import ast_visitor_gen_data as gen_data
import ast_visitor_format as fmt





def load_test_sql(idx):
    name = 'data/test_{0}.sql'.format(idx)
    f = open(name)
    ret = '\n'.join(f.readlines())
    f.close()
    return ret


if __name__ == "__main__":
    if sys.argv[1] == 'test':
        idx = int(sys.argv[2])
        sql = load_test_sql(idx)
        node = parser.parser.parse(sql)
        print node
        gen_data_visitor = gen_data.GenDataVisitor()
        node.visit(gen_data_visitor)
        node.debug()
        rs = []
        fmt_visitor = fmt.FormatVisitor()
        node.visit(fmt_visitor, result=rs)
        print rs[0]
    