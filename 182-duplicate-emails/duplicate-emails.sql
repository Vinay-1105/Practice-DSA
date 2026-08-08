SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(ID) > 1;