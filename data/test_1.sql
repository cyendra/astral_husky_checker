select distinct user_id, name, fak(a + 1, b) as len, m * 7 / (4 * 2) as m7 from ${app}_table
where ds=${bizdate} and (length(b) > 10 or tp = true)
order by length(b) desc, name
limit 100