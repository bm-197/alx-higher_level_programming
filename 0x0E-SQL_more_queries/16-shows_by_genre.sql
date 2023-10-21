-- List all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT s.title, t.name
FROM tv_shows as s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
LEFT JOIN tv_genres AS t ON g.genre_id = t.id
ORDER BY s.title, t.name