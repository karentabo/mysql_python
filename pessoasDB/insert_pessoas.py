import mysql.connector

pessoas_db = mysql.connector.connect(
    host="localhost",  # 127.0.0.1
    user="root",
    password="admin",
    database="pessoas_db"
)

cursor = pessoas_db.cursor()
comando_sql = 'INSERT INTO pessoas (nome, sobrenome, idade) VALUES (%s, %s, %s)'
valores = ('Carlos', 'ALves', 30)
cursor.execute(comando_sql, valores)
pessoas_db.commit()
print(f'O registro foi criado com sucesso! {valores}')
cursor.close()
pessoas_db.close()