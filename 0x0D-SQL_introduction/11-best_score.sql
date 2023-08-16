-- List all the records in a table second_table with the score >= 10.
-- Record are ordered by the descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
