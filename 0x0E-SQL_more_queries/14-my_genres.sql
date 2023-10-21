-- Lists all genres of the show Dexter.
USE hbtn_0d_tvshows;
SELECT t.name
FROM tv_genres AS t 
INNER JOIN tv_show_genres AS g ON t.id = g.genre_id
INNER JOIN tv_shows AS s ON s.id = g.show_id
WHERE s.title = Dexter
ORDER BY t.name;