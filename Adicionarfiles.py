import sqlite3

nome_banco = "iphone.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
 #id INTEGER, modelo TEXT, cor TEXT, ano INTEGER, preco REAL, automatico INTEGER
iphone = [
    (None, 'Iphone11', '128GB',5500 ),
    (None, 'Iphone12', '128GB',6000),
    (None, 'Iphone13', '256GB', 10.200)
]
cur.executemany("INSERT INTO Iphone VALUES (?, ?, ?, ?)", iphone)

con.commit()
con.close()