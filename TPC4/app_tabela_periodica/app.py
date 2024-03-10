from flask import Flask, render_template, url_for
import requests
from datetime import datetime

app = Flask(__name__)

# data do sistema em formato ANSI ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

# GraphDB endpoint details
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

@app.route('/')
def index():
    return render_template('index.html', data = {"data": data_iso_formatada})

@app.route('/elementos')
def elementos():
    sparql_query = '''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?nome ?simbolo ?numero_atomico ?grupo where {
    ?s a tp:Element ;
       tp:name ?nome ;
       tp:symbol ?simbolo ;
       tp:atomicNumber ?numero_atomico ;
       tp:group ?grupo .
}
order by (?nome)
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elementos.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })


@app.route('/elementos/<nome>')
def elemento(nome):
    sparql_query = f'''
PREFIX tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?peso ?numero_atomico ?bloco ?cr ?clasificacao ?cor ?grupo ?periodo ?ss ?simbolo where {{
    ?s a tp:Element ;
       tp:name "{nome}" ;
       tp:group ?grupo ;
       tp:symbol ?simbolo ;
       tp:atomicNumber ?numero_atomico .
    #Os próximos paraâmetros não aprecem em todos os elementos daí usarmos a função de opcional
    optional {{ ?s tp:atomicWeight ?peso . }}
    optional {{ ?s tp:block ?bloco . }}
    optional {{ ?s tp:casRegistryID ?cr . }}
    optional {{ ?s tp:classification ?clasificacao . }}
    optional {{ ?s tp:color ?cor . }}
    optional {{ ?s tp:period ?periodo . }}
    optional {{ ?s tp:standardState ?ss . }}
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elemento.html', data = { 'name': elemento, 'data': dados })
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })


@app.route('/grupos')
def grupos():
    sparql_query = '''
PREFIX tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?grupo (count (?elemento) as ?elementos) where {
    ?grupo a tp:Group ;
           tp:element ?elemento .
} group by ?grupo
order by (xsd:integer(strafter(str(?grupo), '_')))
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('grupos.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })


@app.route('/grupos/<grupo>')
def grupo(grupo):
    sparql_query = f'''
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select ?grupo ?nome_grupo ?numero ?nome_elemento where {{
    ?grupo a tp:Group .
    optional {{ ?grupo tp:name ?nome_grupo . }}
    optional {{ ?grupo tp:number ?numero . }}
    ?group tp:element ?elemento .
    ?elemento tp:name ?nome_elemento .
    filter(str(?grupo) = "http://www.daml.org/2003/01/periodictable/PeriodicTable#{grupo}")
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('grupo.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

if __name__ == '__main__':
    app.run(debug=True)

