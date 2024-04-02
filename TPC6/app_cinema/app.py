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
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?titulo where {
    ?s a tp:Film ;
       tp:movie_title ?titulo .
}
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
    PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
    select ?nome ?duracao ?data ?atores ?realizadores ?produtores ?escritores ?argumentistas ?compositores ?generos ?books where {{
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
             optional {{?s tp:hasGenre ?generos .}}
             optional {{?s tp:basedOf ?books .}}
    }}
    '''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'duracao': list(set(item['duracao']['value'] for item in dados if 'duracao' in item)),
            'data': list(set(item['data']['value'] for item in dados if 'data' in item)),
            'atores': list(set(item['atores']['value'] for item in dados if 'atores' in item)),
            'realizadores': list(set(item['realizadores']['value'] for item in dados if 'realizadores' in item)),
            'produtores': list(set(item['produtores']['value'] for item in dados if 'produtores' in item)),
            'escritores': list(set(item['escritores']['value'] for item in dados if 'escritores' in item)),
            'argumentistas': list(set(item['argumentistas']['value'] for item in dados if 'argumentistas' in item)),
            'compositores': list(set(item['compositores']['value'] for item in dados if 'compositores' in item)),
            'generos': list(set(item['generos']['value'] for item in dados if 'generos' in item)),
            'books': list(set(item['books']['value'] for item in dados if 'books' in item)),
        }
        
        return render_template('filme.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})


@app.route('/pessoas')
def pessoas():
    return render_template('pessoas.html', data = {"data": data_iso_formatada})

@app.route('/atores')
def atores():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
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
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasActor tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('ator.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/realizadores')
def realizadores():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?nome ?data_nascimento where {
    ?s a tp:Director ;
       tp:name ?nome ;
       tp:birthDate ?data_nascimento .
}'''

    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('realizadores.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/realizadores/<nome>')
def realizador(nome):
    sparql_query = f'''
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasDirector tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('realizador.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/produtores')
def produtores():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
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
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasProducer tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('produtor.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/escritores')
def escritores():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
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
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasWriter tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('escritor.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/argumentistas')
def argumentistas():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
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
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasScreenwriter tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('argumentista.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/compositores')
def bandas_sonoras():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
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
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasComposer tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('compositor.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

@app.route('/generos')
def generos():
    sparql_query = '''
prefix tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?generos where {
    ?generos a tp:Genre .
}order by ?generos'''
    resposta = requests.get(graphdb_endpoint, params={ 'query': sparql_query }, headers={ 'Accept': 'application/sparql-results+json' })
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('generos.html', data = dados)
    else:
        return render_template('empty.html', data = { 'data': data_iso_formatada })
    
@app.route('/generos/<nome>')
def genero(nome):
    sparql_query = f'''
PREFIX tp: <http://rpcw.di.uminho.pt/2024/cinema/>
select ?film_title where {{
?film a tp:Film .
?film tp:movie_title ?film_title .
?film tp:hasGenre tp:{nome} .
}}
'''
    resposta = requests.get(graphdb_endpoint, params={'query': sparql_query}, headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200 or resposta.status_code == 304:
        dados = resposta.json()['results']['bindings']
        
        # Extracting data for easier access in the template
        filme_data = {
            'nome': nome,
            'film_title': list(set(item['film_title']['value'] for item in dados if 'film_title' in item))
        }
        
        return render_template('genero.html', filme_data=filme_data, nome=nome)
    else:
        return render_template('empty.html', data={'data': data_iso_formatada})

if __name__ == '__main__':
    app.run(debug=True)