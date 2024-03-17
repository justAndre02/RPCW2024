## Autor
André Freitas (PG54707)

## Abordagem
Implementar um script e mpython capaz de recolher a informação necessária da DBpedia através de queries em SPARQL e exportar toda a informação num ficheiro JSON.

A base de dados do ficehiro JSOn corresponde a uma base de dados relacionada ao cinema e necessita de conter as seguintes informaçoes sobre os filmes listados:
* Título
* Elenco
* Realizadores
* Escritores
* Argumentistas
* Compositores musicais

Além disso esta base de dados necessita de responder às seguintes questãoes: 
* "Que filmes são de curta metragem?" = Isto implica determinar a duração de um filme 
* "Que filmes de ação eu tenho?" = Implica recolher  o género de cada filme
* "Qual o elenco do filme?" = Envolve a listagem dos atores presentes no filme
* "Que filmes atou um certo ator?" = Isto vai implicar uma criação de uma base de dados independente contendo toda esta informação

## Ficheiros 
* [cinema.py](cinema.py): Código python responsável por recolher toda a informação associada a um filme necessária e colocá-la num ficheiro JSON.
* [cinema.json](cinema.json): Base de dados com 60000 filmes e a sua informação
* [actors.py](actors.py): ódigo python responsável por recolher todos os atores existentes, bem como o nome dos filmes na quela estes estão envolvidos e colocar toda esta informação num ficheiro JSON.
* [actors.json](actors.json): Base de dados com todos os atores e os filmes que estes participaram