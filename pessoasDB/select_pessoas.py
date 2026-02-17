import mysql.connector

pessoas_db = mysql.connector.connect(
    host="localhost", #127.0.0.1
    user="root",
    password="admin",
    database="pessoas_db"
)

cursor = pessoas_db.cursor()
cursor.execute('SELECT * FROM pessoas');
result = cursor.fetchall()

for pessoa in result:
    print(pessoa)

cursor.close()
pessoas_db.close()