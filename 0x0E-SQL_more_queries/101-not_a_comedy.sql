-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT s.title
  FROM tv_shows AS s
       LEFT JOIN tv_show_genres AS g
       ON g.show_id = s.id

       LEFT JOIN tv_genres AS t
       ON t.id = g.genre_id
       WHERE s.title NOT IN
             (SELECT s.title
                FROM tv_shows AS s
	             INNER JOIN tv_show_genres AS g
		     ON g.show_id = s.id

		     INNER JOIN tv_genres AS t
		     ON t.id = g.genre_id
		     WHERE t.name = "Comedy")
 ORDER BY s.title;