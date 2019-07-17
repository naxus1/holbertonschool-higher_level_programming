-- script that lists all genres from hbtn_0d_tvshows

SELECT tv_genres.name AS genre, COUNT(genre_id) AS number_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_shows DESC;
