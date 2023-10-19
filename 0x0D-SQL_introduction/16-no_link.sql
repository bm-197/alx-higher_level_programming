-- Converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;