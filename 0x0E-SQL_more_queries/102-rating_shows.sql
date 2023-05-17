-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
SELECT tvs.title, SUM(tvs_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tvs_ratings ON tvs.id = tvs_ratings.show_id
GROUP BY tvs_ratings.show_id
ORDER BY rating DESC;
