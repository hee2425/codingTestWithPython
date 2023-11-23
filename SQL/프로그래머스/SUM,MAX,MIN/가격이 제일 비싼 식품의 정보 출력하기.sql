SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
FETCH FIRST 1 ROWS ONLY

select product_id, product_name, product_cd, category, price
from food_product
where price = (select max(price) from food_product)