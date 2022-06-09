import sqlite3
import os.path
import os

nome_banco = "iphone.db"

if os.path.exists(nome_banco):
    os.unlink(nome_banco)


conexao = sqlite3.connect(nome_banco)

cursor = conexao.cursor()

consulta = """CREATE TABLE Iphone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Modelo TEXT, 
    Capacidade TEXT,
    Preco REAL)"""

cursor.execute(consulta)

consulta = "INSERT INTO Iphone VALUES(?, ?, ?, ?, )"

conexao.commit()
conexao.close()

