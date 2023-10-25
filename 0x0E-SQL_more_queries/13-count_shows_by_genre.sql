-- List all the genres from a database hbtn_0d_tvshows along with a number of
-- shows that are linked to each.
-- Doesn't display the genres without the linked shows.
-- Records ordered by the descending number of the shows linked.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
