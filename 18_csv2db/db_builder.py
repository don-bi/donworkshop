'''
RICE EXPLOSION :: Nakib Abedin, Wilson Mach, Donald Bi
SoftDev  
k18:: SQLITE3 BASICS
Time Spent: 1.5 hrs
2022-10-25

DISCO:
-fstrings can help add data into the table without concatenation
-drop table helps solve the issue with the table already existing
-learned how to use sqlite3 in python file
-we can use fetchall() to print the tables in python
-we can use open() with DictReader to go through a csv file

QCC:
-what exactly does fetchall() do to allow us to print it?
'''

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O
import pprint as pp


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

c.execute("DROP TABLE if exists courses") #deletes the tables if they already exist
c.execute("DROP TABLE if exists students") #to make sure there's no issues

c.execute("CREATE table courses (code TEXT, mark int, id int)") #creates table
with open("courses.csv", newline='') as csvfile: #opens csv file
    reader = csv.DictReader(csvfile)
    for row in reader: #iterates through each line in dictReader object
        c.execute(f"INSERT into courses values (\"{row['code']}\",{row['mark']},{row['id']})") #adds data in each line into table

c.execute("CREATE table students (name TEXT, age int, id int)")
with open("students.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute(f"INSERT into students values (\"{row['name']}\",{row['age']},{row['id']})")        

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

print("COURSES TABLE")
c.execute("select * from courses") #prints courses table
pp.pprint(c.fetchall())

print("\n")

print("STUDENTS TABLE")
c.execute("select * from students") #prints students table
pp.pprint(c.fetchall())
#==========================================================

db.commit() #save changes
db.close()  #close database


