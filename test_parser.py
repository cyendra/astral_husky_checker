import unittest
import parser
import ast_visitor_gen_data
import ast_visitor_format

CREATE_TABLE_SQL="""                                -- 1
create table if not exists test_${conf}_gogo (      -- 2
    abc bigint,                                     -- 3
    cde bigint comment 'qqqq',
    go double,                                      -- 5
    s string comment "bcd"
)
comment "table test" -- ready go                    -- 8
partitioned by (
    ggg bigint comment 'qqqqq',
    nono string
)
lifecycle 88                                         -- 13 


"""


class CreateTableTestCase(unittest.TestCase):

    def setUp(self):
        p = parser.parser
        self.ast = p.parse(CREATE_TABLE_SQL)

    def test_ast_struct(self):
        root = self.ast
        self.assertEqual(root.childs[0], 'CREATE')
        self.assertEqual(root.childs[2].type, 'if_not_exists')
        self.assertEqual(root.childs[5].type, 'table_col_list')
        self.assertEqual(root.childs[8].type, 'table_partitioned')
        self.assertEqual(root.childs[9].type, 'table_lifecycle')

    def test_gen_data(self):
        vst = ast_visitor_gen_data.GenDataVisitor()
        root = self.ast
        root.visit(vst)
        self.assertEqual(root.childs[2].data, 'IF NOT EXISTS')
        self.assertEqual(root.childs[3].data, 'test_${conf}_gogo')
        self.assertEqual(root.childs[5].data, [('abc', 'BIGINT', None), ('cde', 'BIGINT', "'qqqq'"), ('go', 'DOUBLE', None), ('s', 'STRING', '"bcd"')])
        self.assertEqual(root.childs[9].data, 88)

    def test_format(self):
        vst = ast_visitor_gen_data.GenDataVisitor()
        fmt = ast_visitor_format.FormatVisitor()
        root = self.ast
        root.visit(vst)
        rs = []
        root.visit(fmt, result=rs)
        true_ans = '''CREATE TABLE IF NOT EXISTS test_${conf}_gogo (
    abc BIGINT COMMENT "",
    cde BIGINT COMMENT "qqqq",
    go DOUBLE COMMENT "",
    s STRING COMMENT "bcd"
)
COMMENT "table test"
PARTITIONED BY (
    ggg BIGINT COMMENT "qqqqq",
    nono STRING COMMENT ""
)
LIFECYCLE 88;'''
        self.assertEqual(true_ans, rs[0])

if __name__ == '__main__':  
    unittest.main()  