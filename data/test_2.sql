                                -- 1
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