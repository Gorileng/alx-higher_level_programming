-- list all the cities containing a database hbtn_0d_usa.
-- Each of every record must display: cities.id - cities.name - states.name
-- Results should be sorted in the ascending order by the cities.id
-- You can only use one of SELECT statement
-- A database name can be passed as the argument of mysql command

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
