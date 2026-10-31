# Write your MySQL query statement below
select p.product_id, ifnull(round(sum(p.price*uniS.units)/sum(uniS.units),2),0) as average_price
from Prices p
left join UnitsSold uniS 
on p.product_id=uniS.product_id
and uniS.purchase_date >= p.start_date
and uniS.purchase_date <= p.end_date
group by p.product_id