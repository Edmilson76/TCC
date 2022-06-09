import sqlite3

nome_banco = "iphone.db"
con= sqlite3.connect(nome_banco)
cur=con.cursor()
#id INTEGER, modelo TEXT, cor TEXT, ano INTEGER, preco REAL

cur.execute("SELECT modelo, preco FROM Iphone")
dados=cur.fetchall()
print(dados)

con.close()