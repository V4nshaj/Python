import sqlite3

conn = sqlite3.connect('recipe.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE recipes
         (id INT PRIMARY KEY,
         name           VARCHAR(400),
         description    TEXT,
         category_id    INT,
         chef_id       INT,
         created         DATETIME);''')

conn.execute("INSERT INTO recipes (id,name,description,category_id,chef_id,created) \
      VALUES (1, 'Paul', 'Chinese', 252, NULL, NULL)")

      
conn.commit()

cursor = conn.execute("SELECT * FROM recipes WHERE description = 'Chinese'")
for i in cursor:
      print("Description ",i[0])

conn.close()