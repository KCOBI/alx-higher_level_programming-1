-- select c.id c.name and s.name
USE hbtn_0d_usa

SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s
ON s.id = c.state_id
ORDER BY c.id
;
