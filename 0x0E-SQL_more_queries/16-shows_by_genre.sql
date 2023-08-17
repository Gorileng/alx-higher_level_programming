-- List all the shows and the genres linked to show from the
-- Databases hbtn_0d_tvshows.
-- Records ordered by the ascending show title and the genre name.
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
