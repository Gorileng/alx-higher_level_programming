-- List all the records of a table second_table having the name value.
-- Record are ordered by the descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
