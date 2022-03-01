-- this will select all title and gener id fouend
SELECT title , genre_id  
FROM tv_shows  
INNER JOIN  tv_show_genres 
ON tv_show_genres.show_id = tv_shows.id 
ORDER BY title , genre_id;