--  lists the number of records 
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC, score DESC;
