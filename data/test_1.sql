select distinct user_id, name, length(b) as len from ${app}_table
where ds=${bizdate} and length(b) > 10
order by length(b) desc
limit 100