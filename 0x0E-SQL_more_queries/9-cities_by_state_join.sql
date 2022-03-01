-- select c.id c.name and s.name
USE hbtn_0d_usa

SELECT c.id, c.name, s.name
FROM cities as c
INNER JOIN states as s
ON s.id = c.state_id
order by c.id
;