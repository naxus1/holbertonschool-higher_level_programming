-- displays the average temperature
SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY city ASC;
