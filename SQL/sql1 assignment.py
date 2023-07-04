#sql
import sqlite3
conn = sqlite3.connect("test.db")
print("Opened database successfully\n")
conn.execute('''CREATE TABLE IF NOT EXISTS recipes(id integer(11), name varchar(400),
description text,
category_id integer(11),
chef_id varchar(255),
created datetime);''')
print("Table created successfull ")
conn.execute("INSERT INTO recipes VALUES(1100045,'W','Chinese',55,'BL000002',2010);") 
conn.execute("INSERT INTO recipes VALUES(1100089,'P','Italian',03,'BL000006',2011);") 
conn.execute("INSERT INTO recipes VALUES(1100004,'E','Chinese',51,'BL000089',2006);") 
conn.execute("INSERT INTO recipes VALUES(1100109,'K','Persian',19,'BL0008705',2013);")
conn.execute("INSERT INTO recipes VALUES(1100073,'S','Korean',67,'BL000021',2007);") 
conn.execute("INSERT INTO recipes VALUES(11002050,'P','American',16,'BL000002',2003);")
one = conn.execute("SELECT COUNT(*) FROM recipes WHERE description = 'Chinese'")
for i in one:
    print("Chinese : ",i[0])
two = conn.execute("SELECT id, name FROM recipes WHERE chef_id = 'BL000002'")
for j in two:
    print("id :",j[0]) 
    print("name :",j[1],"\n")
three = conn.execute("SELECT description FROM recipes WHERE name LIKE 'P%';")
for k in three:
    print("Description : {0}\n".format(k[0]))
conn.execute("DELETE FROM recipes") 
conn.commit()
conn.close()
