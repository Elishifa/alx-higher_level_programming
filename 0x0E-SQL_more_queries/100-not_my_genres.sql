-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_genres.name - rating sum
-- results must be sorted in descending order by their rating
-- you can use only one SELECT statement
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
      SELECT g.name
      FROM tv_genres g
      INNER JOIN tv_show_genres m ON g.id = m.genre_id
      INNER JOIN tv_shows s ON m.show_id = s.id
      WHERE t.title = 'Dexter'
)
ORDER BY g.name ASC;
