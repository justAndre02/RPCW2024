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
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?s ?duracao ?data where {
    ?s a tp:Film ;
       tp:duration ?duracao ;
       tp:date ?data .
}
order by (?nome)
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('filmes.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/filmes/<nome>')
def filme(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?duracao ?data ?atores ?realizadores ?produtores ?escritores ?argumentistas ?compositores ?genero ?book where {{
    ?s a tp:Film .
    ?s tp:movie_title "{nome}" .
         optional {{?s tp:duration ?duracao .}}
         optional {{?s tp:date ?data .}}
         optional {{?s tp:hasActor ?atores .}}
         optional {{?s tp:hasDirector ?realizadores .}}
         optional {{?s tp:hasProducer ?produtores .}}
         optional {{?s tp:hasWriter ?escritores .}}
         optional {{?s tp:hasScreenwriter ?argumentistas .}}
         optional {{?s tp:hasComposer ?compositores .}}
         optional {{?s tp:hasGenre ?genero .}}
         optional {{?s tp:basedOf ?book .}}
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('filme.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/pessoas')
def pessoas():
    return render_template('pessoas.html', data = {"data": data_iso_formatada})

@app.route('/atores')
def atores():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Actor ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''

    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('atores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/atores/<nome>')
def ator(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasActor tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('ator.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/realizadores')
def realizadores():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Director ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''

    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('realizdores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/realizadores/<nome>')
def realizador(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasDirector tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('realizador.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/produtores')
def produtores():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Producer ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('produtores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/produtores/<nome>')
def produtor(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasProducer tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('produtor.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/escritores')
def escritores():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Writer ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('escritores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/escritores/<nome>')
def escritor(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasWriter tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('escritor.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/argumentistas')
def argumentistas():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Screenwriter ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('argumentistas.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/argumentistas/<nome>')
def argumentista(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasScreenwriter tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('argumentista.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/compositores')
def bandas_sonoras():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Musician ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('compositores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/compositores/<nome>')
def compositor(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasComposer tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('compositor.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

@app.route('/generos')
def generos():
    sparql_query = '''
prefix tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?s where {
    ?s a tp:Genre .
}'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('generos.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/generos/<nome>')
def genero(nome):
    sparql_query = f'''
PREFIX tp: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>
select ?film_title where {{
?film_title a tp:Film .
?film_title tp:hasGenre tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('genero.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })

if __name__ == '__main__':
    app.run(debug=True)