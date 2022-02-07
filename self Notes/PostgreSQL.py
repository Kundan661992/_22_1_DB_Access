"""

1.  What Is PostgreSQL?
PostgreSQL is an object-relational database management system (ORDBMS) based on POSTGRES, Version 4.2, developed at
 the University of California at Berkeley Computer Science Department

PostgreSQL is an open-source.. It supports a large part of the SQL standard and offers many modern features:

                                    complex queries
                                    foreign keys
                                    triggers
                                    updatable views
                                    transactional integrity
                                    multiversion concurrency control
Also, PostgreSQL can be extended by the user in many ways, for example by adding new

                                data types
                                functions
                                operators
                                aggregate functions
                                index methods
                                procedural languages

The object-relational database management system now known as PostgreSQL is derived from the POSTGRES package
written at the University of California at Berkeley. With over two decades of development behind it, PostgreSQL
is now the most advanced open-source database available anywhere.
By 1996, it became clear that the name “Postgres95” would not stand the test of time.We chose a new name,PostgreSQL,
to reflect the relationship between the original POSTGRES and the more recent versions with SQL capability.

Many people continue to refer to PostgreSQL as “Postgres” (now rarely in all capital letters) because of tradition
or because it is easier to pronounce. This usage is widely accepted as a nickname or alias.



In database jargon, PostgreSQL uses a client/server model. A PostgreSQL session consists of the following
cooperating processes (programs):

A server process, which manages the database files, accepts connections to the database from client applications,
and performs database actions on behalf of the clients. The database server program is called postgres.

The user's client (frontend) application that wants to perform database operations. Client applications
can be very diverse in nature: a client could be a text-oriented tool, a graphical application, a web server
that accesses the database to display web pages, or a specialized database maintenance tool.
Some client applications are supplied with the PostgreSQL distribution; most are developed by users.


As is typical of client/server applications, the client and the server can be on different hosts. In
that case they communicate over a TCP/IP network connection. You should keep this in mind, because the
files that can be accessed on a client machine might not be accessible (or might only be accessible using a
different file name) on the database server machine.
"""


"""
To create a new database, in this example named mydb, you use the following command:

$ createdb mydb
"""

# CREATE TABLE weather (
#     city            varchar(80),
#     temp_lo         int,           -- low temperature
#     temp_hi         int,           -- high temperature
#     prcp            real,          -- precipitation
#     date            date
# );
# The INSERT statement is used to populate a table with rows:
#
# INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');

# CREATE TABLE cities (
#     name            varchar(80),
#     location        point
# );
# INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');



# To retrieve data from a table, the table is queried. An SQL SELECT statement is used to do this.
# SELECT * FROM weather;
# Here * is a shorthand for “all columns”. [2] So the same result would be had with:

#    city      | temp_lo | temp_hi | prcp |    date
# ---------------+---------+---------+------+------------
#  San Francisco |      46 |      50 | 0.25 | 1994-11-27
#  San Francisco |      43 |      57 |    0 | 1994-11-29
#  Hayward       |      37 |      54 |      | 1994-11-29
# (3 rows)
"""
You can request that duplicate rows be removed from the result of a query:

SELECT DISTINCT city FROM weather;
SELECT DISTINCT city FROM weather ORDER BY city;



In some database systems, including older versions of PostgreSQL, the implementation of DISTINCT 
automatically orders the rows and so ORDER BY is unnecessary. But this is not required by the SQL standard, 
and current PostgreSQL does not guarantee that DISTINCT causes the rows to be ordered.

"""

"""

Joins Between Tables
Thus far, our queries have only accessed one table at a time. Queries can access multiple tables at once, or 
access the same table in such a way that multiple rows of the table are being processed at the same time. 
Queries that access multiple tables (or multiple instances of the same table) at one time are called join queries. 
They combine rows from one table with rows from a second table, with an expression specifying which rows are to be
 paired. For example, to return all the weather records together with the location of the associated city, the 
 database needs to compare the city column of each row of the weather table with the name column of all rows in 
 the cities table, and select the pairs of rows where these values match.[4] This would be accomplished by the 
 following query:
 
 
 
 SELECT * FROM weather JOIN cities ON city = name;

"""
"""
many to many relations

CREATE TABLE Class(
    ClassID varchar2(10) PRIMARY KEY, 
    Title varchar2(30),
    Instructor varchar2(30), 
    Day varchar2(15), 
    Time varchar2(10)
);

CREATE TABLE Student(
    StudentID varchar2(15) PRIMARY KEY, 
    Name varchar2(35),
    Major varchar2(35), 
    ClassYear varchar2(10), 
    Status varchar2(10)
);  

CREATE TABLE ClassStudentRelation(
    StudentID varchar2(15) NOT NULL,
    ClassID varchar2(14) NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID), 
    FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
    UNIQUE (StudentID, ClassID)
);
"""