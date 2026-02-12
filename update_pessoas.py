import mysql.connector

pessoas_db = mysql.connector.connect(
    host="localhost",  # 127.0.0.1
    user="root",
    password="admin",
    database="pessoas_db"
)

cursor = pessoas_db.cursor()
comando_sql = 'UPDATE pessoas SET nome=%s, sobrenome=%s, idade=%s WHERE id=%s'
valores = ('Carlos', 'Alves', 40, 5)
cursor.execute(comando_sql, valores)
pessoas_db.commit()
print(f'O registro foi atualizado com sucesso!')
cursor.close()
pessoas_db.close()