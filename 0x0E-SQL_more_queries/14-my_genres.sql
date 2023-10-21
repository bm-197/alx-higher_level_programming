-- Lists all genres of the show Dexter.

SELECT t.name
FROM tv_genres AS t 
    INNER JOIN tv_show_genres AS g ON t.id = g.genre_id
    INNER JOIN tv_shows AS s ON g.show_id = s.id 
    WHERE s.title = 'Dexter'
ORDER BY t.name;