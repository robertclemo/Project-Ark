select catcondition from cats

select * from cats where catcondition = 'Stable';

select  * from dogs where adoptable = 'Yes';

#_________THIS JOINS columns from both TABLES to A SINGLE column_________
select name, age, adoptable from cats

union

select name, age, adoptable from dogs;
#__________