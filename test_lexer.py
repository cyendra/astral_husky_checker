import unittest
import lexer

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
        lex = lexer.lexer
        lex.input(CREATE_TABLE_SQL)
        self.tokens = []
        while True:
            tok = lex.token()
            if not tok: break
            self.tokens.append(tok)

    def test_lineno(self):
        for tok in self.tokens:
            if tok.type == 'CREATE':
                self.assertEqual(tok.lineno, 2)
            if tok.type == 'BY':
                self.assertEqual(tok.lineno, 9)
            if tok.type == 'LIFECYCLE':
                self.assertEqual(tok.lineno, 13)

    def test_type(self):
        self.assertEqual(self.tokens[0].type, "CREATE")
        self.assertEqual(self.tokens[2].type, "IF")
        self.assertEqual(self.tokens[9].type, "COMMA")
        self.assertEqual(self.tokens[21].type, "STR")
        self.assertEqual(self.tokens[37].type, "NUMBER")

    def test_value(self):
        self.assertEqual(self.tokens[0].value, "CREATE")
        self.assertEqual(self.tokens[5].value, "test_${conf}_gogo")
        self.assertEqual(self.tokens[13].value, "\'qqqq\'")
        self.assertEqual(self.tokens[27].value, '(')
        self.assertEqual(self.tokens[37].value, 88)

if __name__ == '__main__':  
    unittest.main()  