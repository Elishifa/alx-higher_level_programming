-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT t.title
FROM tv_shows t
WHERE s.title NOT IN (
      SELECT t.title
      FROM tv_shows t
      INNER JOIN tv_show_genres m ON t.id = m.show_id
      INNER JOIN tv_genres g ON m.genre_id = g.id
      WHERE g.name = 'Comedy'
)
ORDER BY t.title ASC;
