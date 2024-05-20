## Abordagem 
* Analisar Dataset
* Criar uma ontologia: classes, object properties e data properties
* Criar um script para povoar a ontologia
* Criar um repositório no graphDB com ontologia
* Adquirir uma representação gráfica da ontologia
* Responder às perguntas com queries de SPARQL

## Autor
André Freitas (PG54707)

## Ficheiros 
#### Dataset  
[mapa.json](mapa.json)

#### Ficheiro TTL gerado para a primeira instância
[fase1.ttl](fase1.ttl)

#### Código Python usado para gerar o resto das entradas 
[geraTTL.py](geraTTL.py)

## Resultados 
#### TTL final 
[fase2.ttl](fase2.ttl)

#### Diagrama gerado no graphDB 
![gráfico_visual](gráfico_visual.png)

## Respostas às perguntas
#### 1 - Quais as cidades de um determinado distrito?
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT ?cidades WERE {
&emsp;?cidade :distrito "Braga" . 
&emsp;?cidade :nome ?cidades .
} 

#### 2 - Distribuição de cidades por distrito?
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT ?distrito (COUNT(DISTINCT ?cidade) AS ?cidades) WHERE {
&emsp;?cidade :distrito ?distrito . 
} GROUP BY ?distrito
ORDER BY ?distrito

#### 3 - Quantas cidades se podem atingir a partir do Porto?
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT (COUNT(DISTINCT ?cidades) AS ?destinosPorto) WHERE {
&emsp;?porto :distrito "Porto" .
&emsp;?ligacao :origemLigacao ?porto . 
&emsp;?ligacao :destinoLigacao ?destino . 
&emsp;?destino :nome ?cidades .
}

#### 4 - Quais as cidades com população acima de um determinado valor?
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT ?cidades ?populacao WHERE {
&emsp;?cidade :populacao ?populacao filter (?populacao > 350000) .
&emsp;?cidade :nome ?cidades .
}

#### 5 - Lista de cidades, ordenada alfabeticamente pelo nome
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT ?cidades WHERE {
&emsp;?cidade :nome ?cidades .
} ORDER BY ?cidades

#### 6 - Que cidades têm ligações diretas com Braga? (Considera Braga como origem mas também como destino)
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

SELECT DISTINCT ?cidades WHERE {
&emsp;{
&emsp;&emsp;?braga :distrito "Braga" .
&emsp;&emsp;?ligacao :origemLigacao ?braga .
&emsp;&emsp;?ligacao :destinoLigacao ?destino .
&emsp;&emsp;?destino :nome ?cidades .
&emsp;}
&emsp;UNION
&emsp;{
&emsp;&emsp;?braga :distrito ?origem .
&emsp;&emsp;?ligacao :destinoLigacao ?braga .
&emsp;&emsp;?origem :nome ?cidades .
&emsp;}
}

#### 7 - Através duma query CONSTRUCT cria uma ligação direta entre Braga e todas as cidades que se conseguem visitar a partir dela.
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

CONSTRUCT {
&emsp;?braga :temLigacaoDiretaCom ?cidade .
}
WHERE {
&emsp;?braga :distrito "Braga" .
&emsp;?ligacao :origemLigacao ?braga .
&emsp;?ligacao :destinoLigacao ?cidade .
}

#### 8 - Através duma query CONSTRUCT cria uma ligação direta entre cada uma das cidades e todas as cidades que se conseguem visitar a partir dela.
PREFIX : <http://rpcw.di.uminho.pt/2024/mapa/>

CONSTRUCT {
&emsp;?origem :temLigacaoDiretaCom ?destino .
}
WHERE {
&emsp;?origem :distrito ?distrito .
&emsp;?ligacao :origemLigacao ?origem .
&emsp;?ligacao :destinoLigacao ?destino .
}