
 0 table_definition None
   0 CREATE <type 'str'>
   1 TABLE <type 'str'>
   2 if_not_exists IF NOT EXISTS
     0 IF <type 'str'>
     1 NOT <type 'str'>
     2 EXISTS <type 'str'>
   3 table_name test_${conf}_gogo
     0 test_${conf}_gogo <type 'str'>
   4 ( <type 'str'>
   5 table_col_list [('abc', 'BIGINT', None), ('cde', 'BIGINT', "'qqqq'"), ('go', 'DOUBLE', None), ('s', 'STRING', '"bcd"')]
     0 table_col_list [('abc', 'BIGINT', None), ('cde', 'BIGINT', "'qqqq'"), ('go', 'DOUBLE', None)]
       0 table_col_list [('abc', 'BIGINT', None), ('cde', 'BIGINT', "'qqqq'")]
         0 table_col_list [('abc', 'BIGINT', None)]
           0 table_col_term ('abc', 'BIGINT', None)
             0 abc <type 'str'>
             1 BIGINT <type 'str'>
             2 table_comment None
               0 None <type 'NoneType'>
         1 , <type 'str'>
         2 table_col_term ('cde', 'BIGINT', "'qqqq'")
           0 cde <type 'str'>
           1 BIGINT <type 'str'>
           2 table_comment 'qqqq'
             0 COMMENT <type 'str'>
             1 'qqqq' <type 'str'>
       1 , <type 'str'>
       2 table_col_term ('go', 'DOUBLE', None)
         0 go <type 'str'>
         1 DOUBLE <type 'str'>
         2 table_comment None
           0 None <type 'NoneType'>
     1 , <type 'str'>
     2 table_col_term ('s', 'STRING', '"bcd"')
       0 s <type 'str'>
       1 STRING <type 'str'>
       2 table_comment "bcd"
         0 COMMENT <type 'str'>
         1 "bcd" <type 'str'>
   6 ) <type 'str'>
   7 table_comment "table test"
     0 COMMENT <type 'str'>
     1 "table test" <type 'str'>
   8 table_partitioned [('ggg', 'BIGINT', "'qqqqq'"), ('nono', 'STRING', None)]
     0 PARTITIONED <type 'str'>
     1 BY <type 'str'>
     2 ( <type 'str'>
     3 table_col_list [('ggg', 'BIGINT', "'qqqqq'"), ('nono', 'STRING', None)]
       0 table_col_list [('ggg', 'BIGINT', "'qqqqq'")]
         0 table_col_term ('ggg', 'BIGINT', "'qqqqq'")
           0 ggg <type 'str'>
           1 BIGINT <type 'str'>
           2 table_comment 'qqqqq'
             0 COMMENT <type 'str'>
             1 'qqqqq' <type 'str'>
       1 , <type 'str'>
       2 table_col_term ('nono', 'STRING', None)
         0 nono <type 'str'>
         1 STRING <type 'str'>
         2 table_comment None
           0 None <type 'NoneType'>
     4 ) <type 'str'>
   9 table_lifecycle 88
     0 LIFECYCLE <type 'str'>
     1 88 <type 'int'>
