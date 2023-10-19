-- List all recors with score >= 10 in second_tabele.
SELECT score, name 
FROM second_table WHERE score >= '10'
ORDER BY score DESC;