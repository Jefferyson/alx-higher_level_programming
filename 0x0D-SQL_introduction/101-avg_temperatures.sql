-- Displays the average temperature (in Fhrenheit)
-- by city ordered by descending temperature.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
