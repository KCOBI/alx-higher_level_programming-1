-- this will display  all city found in californiya wht ever the id of californiya is

USE hbtn_0d_usa;
SELECT id , name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')  ORDER BY id;