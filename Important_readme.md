Before launching this program :
launch MySql and create a database:

Query:
create database database_name;#run it 

#then create a table with query belore:

create table expenses(
id int(),
name varchar(20),
category varchar(40),
amount decimal(10,2),
date date); #run this query 

#now expenses table is created and now you can do the expenses work

#for budget table

create table budget(
month varchar(20),
limit_amount decimal(10,2));

#run it and it will create a budget table 
