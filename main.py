import parser
import ast_visitor_gen_data as gen_data
if __name__ == "__main__":
    s = """                                -- 1
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
    node = parser.parser.parse(s)
    gen_data_visitor = gen_data.GenDataVisitor()
    node.dfs(gen_data_visitor)
    node.debug()