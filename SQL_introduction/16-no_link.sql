-- 'second_table' cədvəlində 'name' sütunu boş olmayan (is not NULL) sətirləri seçir
-- Nəticəni score və name sütunları üzrə, score-a görə azalan sıra ilə göstərir
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
