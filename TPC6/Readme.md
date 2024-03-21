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


## Respostas às perguntas
#### 1 - Quantos filmes existem no repositório?

#### 2 - Qual a distribuição de filmes por ano de lançamento?

#### 3 - Qual a distribuição de filmes por género?

#### 4 - Em que filmes participou o ator "Burt Reynolds"?

#### 5 - Produz uma lista de realizadores com o seu nome e número de filmes que realizou.

#### 6 - Qual o título dos livros que aparecem associados aos filmes?