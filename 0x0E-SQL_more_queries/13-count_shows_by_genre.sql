-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t.name AS genre COUNT(*) AS number_of_shows
FROM tv_genres AS t INNER JOIN tv_show_genres AS g
ON t.id = g.genre_id
GROUP BY t.name
ORDER BY number_of_shows DESC;