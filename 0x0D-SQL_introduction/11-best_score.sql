-- Lists all records of the table 'second_table' with a score >= 10
--    + displays the score and the name
--    + should be ordered from score

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
