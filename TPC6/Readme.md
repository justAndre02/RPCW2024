## Autor
André Freitas (PG54707)

## Abordagem
* Pegar no ficheiro TTL criado durante a aula (19_03_2024) e usá-lo como base para a produção da ontologia completa
* Adicionar a base de dados com os filmes desenvolvida no TPC5 que se encontra na forma de um ficheiro JSON
* Desenvolver o código python para povoar a ontologia original invocando as entradas no ficheiro JSON que contém todos os filmes
* Carregar o dataset no endpoint http://epl.di.uminho.pt:7200
* Colocar no repositório: http://epl.di.uminho.pt:7200/repositories/cinema2024
* Construir as queries necessárias para responder às perguntas colocadas
* Usar o flask para geraruma interface web ao repositório de filmes

## Ficheiros
#### Dataset 
[cinema.json](cinema.json)

#### Ficheiro TTL gerado para a primeira instância
[cinema.ttl](cinema.ttl)

#### Código Python usado para gerar o resto das entradas 
[appTPC6.py](appTPC6.py)

## Resultados 
#### TTL final 
[andre_pg54707.ttl](andre_pg54707.ttl)

#### Interface web do repositório de filmes
[app.py](/TPC6/app_cinema/app.py)

## Respostas às perguntas
### 1 - Quantos filmes existem no repositório?
##### SPARQL Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT (COUNT(?film_title) AS ?numFilmes)WHERE {
&emsp;?film_title rdf:type <http://www.semanticweb.org/andre/ontologies/2024/cinema/Film> .
}

### 2 - Qual a distribuição de filmes por ano de lançamento?
##### SPARQL Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ont: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>

SELECT ?release ?film WHERE {
&emsp;?film rdf:type ont:Film .
&emsp;?film ont:date ?release .
}
ORDER BY ?release

### 3 - Qual a distribuição de filmes por género?
##### SPARQL Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ont: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>

SELECT ?genre (COUNT(?film) AS ?numFilmes) WHERE {
&emsp;?film rdf:type ont:Film .
&emsp;?film ont:hasGenre ?genre .
}
GROUP BY ?genre
ORDER BY DESC(?numFilmes)

### 4 - Em que filmes participou o ator "Burt Reynolds"?
##### SPARQL Query
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ont: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>

SELECT ?film_title WHERE {
&emsp;?film_title rdf:type ont:Film .
&emsp;?film_title ont:hasActor ont:Burt_Reynolds .
}

### 5 - Produz uma lista de realizadores com o seu nome e número de filmes que realizou.
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ont: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>

SELECT ?director (COUNT(?film) AS ?numFilmes) WHERE {
&emsp;?film rdf:type ont:Film .
&emsp;?film ont:hasDirector ?director .
}
GROUP BY ?director

### 6 - Qual o título dos livros que aparecem associados aos filmes?
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ont: <http://www.semanticweb.org/andre/ontologies/2024/cinema/>

SELECT ?film ?book WHERE {
&emsp;?film rdf:type ont:Film .
&emsp;?film ont:basedOf ?book .
}