-- List all the shows in the hbtn_0d_tvshows that has one genre linked.
-- Records sorted by the ascending tv_shows.title and the tv_show_genres.genre_id.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
