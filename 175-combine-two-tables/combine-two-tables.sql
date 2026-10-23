# Write your MySQL query statement below
select
    p.firstName,
    p.lastName,
    a.city,
    a.state
from
    person p
Left join
    Address a
on 
    p.personID = a.personId