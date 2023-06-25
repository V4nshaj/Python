'''import sqlite3

conn = sqlite3.connect('test3.db')
print ("Opened database successfully")
sqlt="CREATE TABLE trial
         (id INT PRIMARY KEY,
         name           VARCHAR(400),
         description    TEXT,
         category_id    INT,
         chef_id       INT,
         created         DATETIME);"
conn.execute(sqlt)

conn.execute("INSERT INTO trial (id,name,description,category_id,chef_id,created) \
      VALUES (1, 'Paul', 'Chinese', 252, NULL, NULL)")

      
conn.commit()

cursor = conn.execute("SELECT * FROM trial WHERE description = 'Chinese'")
print(cursor)

conn.close()
'''
import sqlite3

conn= sqlite3.connect("test.db")
#u can write connection.Cursor


sql_table="""CREATE TABLE trial( 
    id INTEGER PRIMARY KEY, 
    name VARCHAR(20),
    gender VARCHAR(20), 
    dob DATE);"""

conn.execute(sql_table)

conn.execute("INSERT INTO trial (id, name, gender, dob)\
        VALUES (15, 'Vanshaj', 'Male', 21-08-21)")

# sql_table= 'INSERT INTO trial VALUES(11, Arnav, male, 20-03-22);'
conn.commit()
#connection.commit

cursor=conn.execute("SELECT * FROM trial")
# print(conn)
# a=conn.fetchall()
# for i in a:
#     print(i)

conn.close()
