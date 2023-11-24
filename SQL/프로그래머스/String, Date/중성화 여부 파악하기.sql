SELECT ANIMAL_ID, NAME, 
        CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%' THEN 'O'
        ELSE 'X' END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

select animal_id, name, 
        case when lower(sex_upon_intake) like '%neutered%' or lower(sex_upon_intake) like '%spayed%' then 'O'
        else 'X' end as "중성화"
from animal_ins
order by animal_id