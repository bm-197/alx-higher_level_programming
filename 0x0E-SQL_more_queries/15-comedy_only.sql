-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title
FROM tv_shows AS s 
INNER JOIN tv_show_genres AS g ON s.id = g.show_id
INNER JOIN tv_genres AS t ON t.id = g.genre_id 
WHERE (t.name = 'Comedy')
ORDER BY s.title;