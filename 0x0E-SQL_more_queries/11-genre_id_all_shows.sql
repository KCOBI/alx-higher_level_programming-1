-- THIS WILL SELECT ALL SHOWS
SELECT title , genre_id  
FROM tv_shows  
LEFT JOIN tv_show_genres 
ON tv_show_genres.show_id = tv_shows.id 
ORDER BY title , genre_id;