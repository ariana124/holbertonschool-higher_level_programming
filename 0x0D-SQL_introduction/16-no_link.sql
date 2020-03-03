-- Lists all the records of the table 'second_table'
--    + don't list rows without a name value
--    + should be listed in descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
