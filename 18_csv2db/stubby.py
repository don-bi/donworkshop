#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo") 

c = db.cursor() #facilitate db ops

# c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
c.execute('INSERT INTO roster VALUES("John",10)')
c.execute('INSERT INTO roster VALUES("Donald",10)')
res = c.execute("select * from roster")
print(res.fetchall())

db.commit() #save changes
db.close()
