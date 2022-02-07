"""CREATE DATABASE mydb;
USE mydb;
CREATE TABLE Student(
    StudentID varchar(15) PRIMARY KEY,
    Name varchar(35),
    ClassYear varchar(10),
    Status varchar(10)
);
SELECT * FROM Student
-- DESC Student;

alter  TABLE Student RENAME TO stu;

select * from stu

alter TABLE stu ADD address varchar(100);

alter TABLE stu ADD  column address varchar(100);

alter TABLE stu rename column address  TO  college ;

alter TABLE stu  DROP column college ;

alter TABLE stu modify column Name varchar(100);

DROP TABLE stu;
desc stu;  #description about student




CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);
alter TABLE Persons DROP COLUMN city;
alter TABLE Persons ADD COlUMN city varchar(200);
rename table Persons to Per_details;
alter table Per_details rename column address to contact;
-- desc Per_details

insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('1','sri', 'reddy',  '1234', 'Bengaluru');
insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('2', 'hari', 'singh',  '5678', 'mysore');
insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('3','deo', 'kumar',  '9874', 'delhi');
insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('4','shyam', 'viswas',  '5612', 'goa');
insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('5','ram', 'mohan',  '3215', 'US');
insert into Per_details (PersonID,LastName, FirstName, contact,  City) values ('6','niti', 'kumari',  '8794', 'BALI');
select * from Per_details;


select PersonID ,LastName ,FirstName ,contact ,City from Per_details;
select * from Per_details Where city ='delhi'
select * from Per_details Where city ='US' and LastName ='kumar';
select * from Per_details Where city ='Delhi' and LastName ='kumar';
select * from Per_details Where PersonID ='5' or LastName ='kumar';
select * from Per_details Where LastName ='kumar' IN ('7894,1234');
select * from Per_details Where city ='US' NOT IN ('1234,54987');
select * from Per_details Where city ='US' and LastName ='kumar';
select * from Per_details WHERE city ='US' LIMIT 5;
select * from Per_details WHERE city  IS NULL;
select * from Per_details WHERE city  IS NOT NULL;
select * from Per_details WHERE LastName  order by PersonID;
select * from Per_details WHERE city ='delhi' group by contact;
select * from Per_details WHERE city  group by contact having PersonID;




select  city  as area from Per_details;
SELECT city, contact FROM Per_details GROUP BY  city,contact WITH ROLLUP;

INSERT INTO Per_details (PersonID,LastName, FirstName, contact,  City) VALUES ( '5','python','guiod', '1234','delhi' );
INSERT INTO Per_details (PersonID,LastName, FirstName, contact,  City) VALUES ( '6','java', 'van','00021','US' );
INSERT INTO Per_details (PersonID,LastName, FirstName, contact,  City) VALUES ( '1','ruby','reddy', '7894','Bengaluru' );
-- desc Per_details--  #  for commenting (--)
INSERT INTO Per_details  VALUES ( '9','kumar','ved', '4561','Mysore' );
INSERT INTO Per_details  VALUES ( '5','python','guiod', '1234','delhi' ),( '10','preti','kumari', '8982','goa' ),( '0','krishna','ram', '70991','czech' );
INSERT Ignore INTO Per_details (PersonID,LastName, FirstName, contact,  City) VALUES ( '5','python','guiod', '1234','delhi' );
-- select * from Per_details



-- UPDATE Per_details SET LastName= 'kundan' WHERE city ='delhi';
-- UPDATE Per_details SET FirstName = 'python' ,LastName = 'singh' WHERE city ='delhi';

delete from Per_details Where city ='delhi';
delete from Per_details Where city ='delhi' and 'contact';
delete from Per_details  4 x Where LastName IN ;



 CREATE TABLE dummy (
emp_id INT NOT NULL,
name VARCHAR (45) NOT NULL,
phone_no VARCHAR (45) NOT NULL,
technology VARCHAR (45) NOT NULL,
salary VARCHAR (45) NOT NULL,
start_date VARCHAR (45) NOT NULL,
comments VARCHAR (45) NULL,
PRIMARY KEY (emp_id))
COMMENT = 'this table contains all the employee details';
 ALTER TABLE dummy RENAME TO employee;

DESC employee;
SELECT * FROM EMPLOYEE;

 START TRANSACTION;

 INSERT INTO employee VALUES
('001' , 'aaaa', '2345623452' , 'Java' , '20000', '2022-01-011' , 'none'),
('002' , 'ssss','7436654656','Python', '21000', '2022-01-04', 'none'),
('003' , 'dadd' , '8584567766', 'Database', '18000', '2022-01-06' , 'none'),
('004' , 'EffE','4524354556','Testing', '15000' , '2022-01-031' , 'none');

INSERT INTO employee VALUES
('005', 'eeee', '2345745772', 'Java', '20000', '2022-01-08', 'none'),
('006' , 'Efff' ,'4563674678','Java','30000','2022-01-08','none');
SAVEPOINT sp1;
UPDATE employee SET salary = '25000' WHERE (emp_id = '5') ;

SAVEPOINT sp2;

DELETE e FROM employee as e WHERE e.technology = 'Java' AND e.salary = (SELECT * FROM (
SELECT MAX(salary) FROM employee where technology = 'Java' order by salary DESC) x);

DELETE e FROM employee as e WHERE e.salary in (SELECT * FROM (SELECT salary FROM employee where
salary > '20000') x);

SELECT * FROM EMPLOYEE;

TRUNCATE TABLE employee;
"""