-- script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
LEFT OUTER JOIN states
ON cities.state_id = states.id;
