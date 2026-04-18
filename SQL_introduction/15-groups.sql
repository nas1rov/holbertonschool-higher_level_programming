-- Balları qruplaşdırır və hər baldan neçə ədəd olduğunu sayır
-- Nəticəni sayına görə azalan sıra ilə düzür
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
