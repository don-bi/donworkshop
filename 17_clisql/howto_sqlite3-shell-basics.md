# Creating a file
`sqlite3 FILENAME`
- if FILENAME does not exist, then it creates a file
- if FILENAME does exist, it runs the file
- if you just do `sqlite3` the shell opens but the changes are temporary unless you choose to save it

# Creating a table
`CREATE TABLE <NAME> (<COLUMN NAME> <DATA TYPE>, <COLUMN NAME> <DATA TYPE>, ...);`

# Inserting values
`INSERT INTO <tbl_name> VALUES (<field 1>, <field 2> ...);`

# Accessing Values
To see entire table: `SELECT * FROM <tbl_name>;`
To access specific column: `SELECT <field_name> FROM <tbl_name>;`
To access specific info from specific column: `SELECT <field_name> FROM <tbl_name> WHERE <condition>;`

# Commands
To leave the sqlite shell: .quit

# Example code
```
sqlite3

/* creates a table named demo */
create table demo (firstName text, lastName text);

/* inserts "Wilson" into first column and "Mach" into second column"*/
insert into demo values ("Wilson", "Mach");

/* inserts "Donald" into first column and "Bi" into second column"*/
insert into demo values ("Donald", "Bi");

/* inserts "Nakib" into first column and "Abedin" into second column"*/
insert into demo values ("Nakib", "Abedin");

/* views entire table */
select * from demo;

/* views all values in colum1 (firstName) */
select firstName from demo;  

/* views all values with lastName equals "Mach" in colum1 (firstName) */
select firstName from demo where lastName = "Mach";  
```
