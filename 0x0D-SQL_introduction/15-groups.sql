-- this should print 
--      the grouped score
--      the score
SELECT score , count(score) AS number
from second_table
GROUP BY score
HAVING COUNT(score) > 0
ORDER BY score ASC;
