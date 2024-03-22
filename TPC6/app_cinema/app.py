from flask import Flask, render_template, url_for
import requests
from datetime import datetime

app = Flask(__name__)

# data do sistema em formato ANSI ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint details
graphdb_endpoint = "http://epl.di.uminho.pt:7200/repositories/cinema2024"

@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_iso_formatada})

@app.route('/filmes')
def filmes():
    sparql_query = '''  '''

@app.route('/atores')
def atores():
    sparql_query = '''  '''

@app.route('/realizadores')
def realizadores():
    sparql_query = '''  '''

@app.route('/produtores')
def produtores():
    sparql_query = '''  '''

@app.route('/escritores')
def escritores():
    sparql_query = '''  '''

@app.route('/argumentistas')
def argumentistas():
    sparql_query = '''  '''

@app.route('/compositores')
def bandas_sonoras():
    sparql_query = '''  '''

@app.route('/generos')
def generos():
    sparql_query = '''  '''

if __name__ == '__main__':
    app.run(debug=True)