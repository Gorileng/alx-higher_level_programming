-- List all the shows containing a database hbtn_0d_tvshows.
-- Display NULL for the shows without the genres.
-- Records ordered by the ascending tv_shows.title and the tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
