-- Balı 10-dan böyük və ya bərabər olan sətirləri seçir
-- Nəticəni score və name sütunları üzrə azalan sıra ilə göstərir
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
