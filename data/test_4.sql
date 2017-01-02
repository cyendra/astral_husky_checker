select user_id, name, count(*) as cnt 
from (
    select * from ( select user_id, name, ds from some_proj.${job}_table_name where ds >= ${bizdate}) a
    limit 100
) t
where ds=${bizdate}