SELECT ANIMAL_TYPE, NVL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

select animal_type, decode(name,null,'No name',name) as name, sex_upon_intake
from animal_ins
order by animal_id