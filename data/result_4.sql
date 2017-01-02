 0 select_stmt None
   0 SELECT <type 'str'>
   1 all_or_distinct None
     0 None <type 'NoneType'>
   2 select_expr_list [(['user_id'], None), (['name'], None), ([('func', 'count', [['*']])], 'cnt')]
     0 select_expr_list [(['user_id'], None), (['name'], None)]
       0 select_expr_list [(['user_id'], None)]
         0 select_expr (['user_id'], None)
           0 line_expr ['user_id']
             0 factor_expr ['user_id']
               0 simple_expr user_id
                 0 user_id <type 'str'>
       1 , <type 'str'>
       2 select_expr (['name'], None)
         0 line_expr ['name']
           0 factor_expr ['name']
             0 simple_expr name
               0 name <type 'str'>
     1 , <type 'str'>
     2 select_expr ([('func', 'count', [['*']])], 'cnt')
       0 line_expr [('func', 'count', [['*']])]
         0 factor_expr [('func', 'count', [['*']])]
           0 simple_expr ('func', 'count', [['*']])
             0 func_expr ('func', 'count', [['*']])
               0 count <type 'str'>
               1 ( <type 'str'>
               2 expr_list [['*']]
                 0 line_expr ['*']
                   0 factor_expr ['*']
                     0 simple_expr *
                       0 symbol_expr *
                         0 * <type 'str'>
               3 ) <type 'str'>
       1 AS <type 'str'>
       2 cnt <type 'str'>
   3 FROM <type 'str'>
   4 table_reference None
     0 ( <type 'str'>
     1 select_stmt None
       0 SELECT <type 'str'>
       1 all_or_distinct None
         0 None <type 'NoneType'>
       2 select_expr_list [(['*'], None)]
         0 select_expr (['*'], None)
           0 line_expr ['*']
             0 factor_expr ['*']
               0 simple_expr *
                 0 symbol_expr *
                   0 * <type 'str'>
       3 FROM <type 'str'>
       4 table_reference None
         0 ( <type 'str'>
         1 select_stmt None
           0 SELECT <type 'str'>
           1 all_or_distinct None
             0 None <type 'NoneType'>
           2 select_expr_list [(['user_id'], None), (['name'], None), (['ds'], None)]
             0 select_expr_list [(['user_id'], None), (['name'], None)]
               0 select_expr_list [(['user_id'], None)]
                 0 select_expr (['user_id'], None)
                   0 line_expr ['user_id']
                     0 factor_expr ['user_id']
                       0 simple_expr user_id
                         0 user_id <type 'str'>
               1 , <type 'str'>
               2 select_expr (['name'], None)
                 0 line_expr ['name']
                   0 factor_expr ['name']
                     0 simple_expr name
                       0 name <type 'str'>
             1 , <type 'str'>
             2 select_expr (['ds'], None)
               0 line_expr ['ds']
                 0 factor_expr ['ds']
                   0 simple_expr ds
                     0 ds <type 'str'>
           3 FROM <type 'str'>
           4 table_reference None
             0 table_name some_proj.${job}_table_name
               0 some_proj <type 'str'>
               1 . <type 'str'>
               2 ${job}_table_name <type 'str'>
             1 table_other_name None
               0 None <type 'NoneType'>
           5 where_stmt ['ds', '>=', '${bizdate}']
             0 WHERE <type 'str'>
             1 where_condition ['ds', '>=', '${bizdate}']
               0 line_expr ['ds', '>=', '${bizdate}']
                 0 line_expr ['ds', '>=']
                   0 line_expr ['ds']
                     0 factor_expr ['ds']
                       0 simple_expr ds
                         0 ds <type 'str'>
                   1 factor_expr ['>=']
                     0 simple_expr >=
                       0 symbol_expr >=
                         0 >= <type 'str'>
                 1 factor_expr ['${bizdate}']
                   0 simple_expr ${bizdate}
                     0 ${bizdate} <type 'str'>
           6 group_stmt None
             0 None <type 'NoneType'>
           7 order_stmt None
             0 None <type 'NoneType'>
           8 distribute_stmt None
             0 None <type 'NoneType'>
           9 limit_stmt None
             0 None <type 'NoneType'>
         2 ) <type 'str'>
         3 table_other_name a
           0 a <type 'str'>
       5 where_stmt None
         0 None <type 'NoneType'>
       6 group_stmt None
         0 None <type 'NoneType'>
       7 order_stmt None
         0 None <type 'NoneType'>
       8 distribute_stmt None
         0 None <type 'NoneType'>
       9 limit_stmt 100
         0 LIMIT <type 'str'>
         1 100 <type 'int'>
     2 ) <type 'str'>
     3 table_other_name t
       0 t <type 'str'>
   5 where_stmt ['ds', '=', '${bizdate}']
     0 WHERE <type 'str'>
     1 where_condition ['ds', '=', '${bizdate}']
       0 line_expr ['ds', '=', '${bizdate}']
         0 line_expr ['ds', '=']
           0 line_expr ['ds']
             0 factor_expr ['ds']
               0 simple_expr ds
                 0 ds <type 'str'>
           1 factor_expr ['=']
             0 simple_expr =
               0 symbol_expr =
                 0 = <type 'str'>
         1 factor_expr ['${bizdate}']
           0 simple_expr ${bizdate}
             0 ${bizdate} <type 'str'>
   6 group_stmt None
     0 None <type 'NoneType'>
   7 order_stmt None
     0 None <type 'NoneType'>
   8 distribute_stmt None
     0 None <type 'NoneType'>
   9 limit_stmt None
     0 None <type 'NoneType'>

SELECT user_id
    , name
    , count(*) AS cnt
FROM (
    SELECT *
    FROM (
        SELECT user_id
            , name
            , ds
        FROM some_proj.${job}_table_name
        WHERE ds >= ${bizdate}
    ) a
    LIMIT 100
) t
WHERE ds = ${bizdate}