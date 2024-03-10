## Autor
André Freitas (PG54707)

## Abordagem
* Criar um novo repositório no GraphDB
* Importar o ficheiro "ttl" diisponível no BlackBoard 
* Desenvolver a aplicação em Python

## Alterações a efetuar 
### elementos.html
* Acrescentar uma coluna com o grupo
* Grupo é um link para a página do grupo
* O número atómico (na) ou nome são links para  a página elemento

### grupos.html
* Listar os grupos

### grupo.html
* Introduzir informação do grupo 
* Listagem de elementos 

### elementos.html
* Apresentar informação de cada elemento

## Ficheiros 
* [app.py](/TPC4/app_tabela_periodica/app.py): Código Python encarregue de iniciar um servidor usando Flask, fazer as queries do repositório no GraphDB e redirecionar o conteúdo para cada respetiva página
* [w3.css](/TPC4/app_tabela_periodica/static/styles/w3.css): Ficheiro CSS rsponsável por definir as simples cores e formatos presentes na nossa plataforma
* [index.html](/TPC4/app_tabela_periodica/templates/index.html): Página inicial da nossa plataforma
* [empty.html](/TPC4/app_tabela_periodica/templates/empty.html): Página de erro
* [elementos.html](/TPC4/app_tabela_periodica/templates/elementos.html): Página que lista todos os elementos presentes na tabela periódica
* [elemento.html](/TPC4/app_tabela_periodica/templates/elemento.html): Página que apresenta detalhadamente cada elemento
* [grupos.html](/TPC4/app_tabela_periodica/templates/grupos.html): Página que mostra todos os grupos de elementos existentes e o número de elementos presentes neste grupo
* [grupo.html](/TPC4/app_tabela_periodica/templates/grupo.html): Página que apresenta o nome ou o número de um determinado grupo, bem como a listagem dos elementos associados a este grupo