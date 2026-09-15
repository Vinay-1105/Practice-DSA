# Write your MySQL query statement below
select e.name, euni.unique_id
from Employees e
left join EmployeeUNI euni
on e.id = euni.id;