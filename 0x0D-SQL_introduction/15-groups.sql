-- List a number of records with a same score in the table second_table.
-- Record are ordered by the descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
