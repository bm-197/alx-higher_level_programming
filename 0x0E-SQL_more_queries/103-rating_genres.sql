-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT t.name, SUM(r.rate) AS rating
FROM tv_genres AS t
    INNER JOIN tv_show_genres AS g ON t.id = g.genre_id
    INNER JOIN tv_shows AS s ON g.show_id = s.id 
    INNER JOIN tv_show_ratings AS r ON s.id = r.show_id
GROUP BY (t.name)
ORDER BY rating DESC;