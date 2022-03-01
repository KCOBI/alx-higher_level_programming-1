-- THIS WILL SELECT TV SHOWS WITH NULL GENERE

SELECT title , genre_id   
FROM tv_shows   
LEFT JOIN tv_show_genres 
ON tv_show_genres.show_id = tv_shows.id 
WHERE genre_id IS NULL 
ORDER BY title , genre_id;