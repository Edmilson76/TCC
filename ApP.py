import sqlite3
from flask import Flask
from flask_cors import CORS
from flask import jsonify

def pega_conexao():
    nome_banco = "iphone.db"
    con = sqlite3.connect(nome_banco) # Conecta no banco
    return con

app = Flask(__name__)
CORS(app)
    
@app.route("/")
def raiz():
    return "Resposta do meu backend em Python"


@app.route("/todos")
def todos():
    con= pega_conexao()
    cur= con.cursor()

    try:
        cur.execute("SELECT * FROM Iphone")
    except:
        con.close()
        return jsonify("Erro ao consultar")

    dados = cur.fetchall()
    con.close()
    return jsonify(dados)

@app.route("/lista/<int:id>")
def lista_um(id):
    con=pega_conexao()
    cur=con.cursor()

    try:
        cur.execute(f"SELECT * FROM Iphone WHERE id={id}")
    except:
       con.close()
       return jsonify("Erro ao consultar")         
       
    dados = cur.fetchone()
    con.close()
    return jsonify(dados)


app.run()





