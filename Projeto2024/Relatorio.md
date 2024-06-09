# Relatório do trabalho prático de RPCW 2024

## Autores
* André Freitas PG54707
* Daniel Azevedo PG50311
* Gonçalo Vale PG53849

### Introdução 
Este trabalho foi desenvolvido a teor da disciplina de Representação e Processamento de Conhecimento Web e funciona como uma condensação de todos os conhecimentos obtidos ao longo do semestre.  

O nosso projeto é baseado na proposta número dois dada pelo professor e foca-se na criação de uma aplicação web capaz de recolher e adicionar informação de uma ontologia desenvolvida pela equipa de trabalho. Esta ontologia é composta pela informação recolhida ao longo dos anos do site do Diário da República.

### Ontologia desenvolvida
Neste capítulo iremos focar no processo por trás da ontologia criada, abordando a estrutura da mesma e a recolha dos dados.

Neste momento a ontologia desenvolvida encontra-se fora dorepositório por ser demasiado grande, para poder acedê-la basta clicar no link: https://drive.google.com/file/d/10smwo4RDShTUYqr9VcTpOQyPkf9wsito/view?usp=sharing

#### Estrutura da ontologia
Baseado no conteúdo disponibilizado pelo professor chegamos a um acordo de como deveria ser a estrutura da ontologia. Em primeiro lugar ponderamos o contexto na qual a ontologia se encaixa e daí determinamos o domínio como sendo a publicação de documentos associados a uma ou mais entidade.

Por isso foram criadas duas classes: *Document* e *Emitter*, sendo que o relacionamento entre si funciona da seguinte forma, um documento tem um ou mais emissores e consequentemente cada emissor poderá ter vários documentos. 

Um documento é composto pelo seguinte atributos:
* **id**: Identificação do documento
* **date**: Data de publicação
* **docType**: Tipo de documento
* **notes**: Notas informacionais do documento
* **number**:  Número de referência
* **numberDR**: Número com dia de publicação
* **series**: Série
* **source**: Origem de publicação

Por outro lado um emissor apenas comtém um campo sendo ele o **emitter_name** que representa o nome do mesmo.

#### Recolha de dados 
Após a criação da ontologia foi necessário passar para a povoação da mesma, daí a necessidade da criação de um script em Python capaz de recolher a informação disponibilizada no ficheiro JSON "*2024-04-14-DRE_dump*" cedido pelo professor. Devido ao tamanho do mesmo mostrou-se complicado processar um ficheiro de tamanha dimensão de forma a recolher a informação necessária.

Este problema levou-nos ao desenvolvimento da script [split.py](tratamento_dados/split.py) responsável por pegar no ficheiro JSON e dividir este em 10 partes espalhadas por outros ficheiros JSON como o ficheiro [2024-04-14-DRE_dump_part1.json](tratamento_dados/2024-04-14-DRE_dump_part1.json) até ao ficheiro [2024-04-14-DRE_dump_part10.json](tratamento_dados/2024-04-14-DRE_dump_part10.json).

Este processo acelerou drasticamente a script de povoamento [povoamento.py](tratamento_dados/povoamento.py). Nesta script fazemos um ciclo que acede a todos os fiheiros JSON e anexa toda a informação num só ficheiro TTL.

É importante salientar a existência de um ficheiro **2024-04-14-DRE.sql** com um tamanho de 8.4gb. A primeira parte deste ficheiro é comp+odsto por milhares de inserts que representam a informação já especificada no ficheiro JSON. O resto trata-se de inserts de novos documentos, mas estas entradas não contém todos os campos e valores existentes nos documentos já importados. 

Mesmo assim o grupo tentou recolher esta informação tentando separar até o ficheiro em vários, mas isto revelou-se impossivel na falta de poder computacional. Com isto acabamos por desistir e apenas ficar com os dados já recolhidos.

#### Tratamento de dados 
Todo o processo descrito na secção anterior não foi assim tão simples devido aos mútliplos casos de erros detetados pela aplicação que processa um ficheiro TTL. 

Antes de falar deste tópico seria relevante falar de alguns campos existentes nos ficheiros JSON que não foram transportados para o ficheiro TTL, como por exemplo: o **dre_key** que se encontrava vazio em quase todas as entradas, as variáveis boleanas **conditional**, **processing**, **in_force** e **pdf_error** que não contribuem em nada para os objetivos da ontologia e os campos **plain_text** e **dre_pdf** que representam links dedicados ao aramazenamento da informação do documento em texto plano e PDF respetivamente. Estes dois últimos campos poderia ser engraçados de abordar mas os links não funcionam.

Dos campos recolhidos várias coisas tiveram de ser mudadas devido à intolerância mostrada pelo TTL aos caracteres representados nos ficheiros JSON que por sinal apresentavam códigos unicode em vez da sua representação caractérica. Com isto forma alteradas algumas informações diretamente nos ficheiros JSON e foi usada alguams vezes a função *replace* na script em Python.

#### Disponibilização dos dados
Após tudo isto foi colocado o ficheiro TTL *DR_povoada.ttl* no repositório criado no GraphDB dedicado ao aramazenamento da informação deste trabalho prático. Isto torna possível o acesso à informação, através da chamada de queries em SPARQL.

### Desenvolvimento do Backend
Nesta seção do relatório, abordaremos o desenvolvimento do backend da aplicação. Descreveremos as tecnologias e ferramentas utilizadas, como o framework Flask e o GraphDB, e especificaremos os métodos implementados no servidor.  

#### Tecnologias e ferramentas utilizadas
Para o desenvolvimento do servidor, utilizamos o framework **Flask**, que é uma estrutura leve e flexível para construir aplicativos web em *Python*. O **Flask** oferece uma abordagem simples e direta para o desenvolvimento de servidores, permitindo que os desenvolvedores criem rotas, gerem solicitações e respostas *HTTP*, e implementem a lógica do projeto de forma eficiente.

Além do *Flask*, também utilizamos outras ferramentas e tecnologias para auxiliar no desenvolvimento do servidor, como:

- **Python**: A linguagem de programação principal utilizada para escrever o código do servidor. *Python* é conhecido por sua simplicidade e legibilidade, o que facilita o desenvolvimento e a manutenção do código.

- **Virtualenv**: Uma ferramenta que permite criar ambientes virtuais isolados para cada projeto, garantindo a independência das dependências e evitando conflitos entre diferentes projetos.

- **GraphDB**: Uma base de dados de grafo utilizado para armazenar a ontologia desenvolvida. O *GraphDB* permite o armazenamento e a consulta eficiente de dados em formato de grafo, o que é especialmente adequado para representar relações complexas entre entidades.

Essas ferramentas e tecnologias foram escolhidas com base na sua eficiência, facilidade de uso e integração com o *Flask*, garantindo um desenvolvimento suave e uma aplicação web robusta.

#### Especificação dos métodos

**GET/documentos**: Retorna a página com a lista de todos os documentos.

**GET/documentos/by_author**: Retorna documentos emitidos por um autor específico, paginados. Parâmetros de Rota: 
* **id**: Identificador do autor.
* **np**: Número da página.

**GET/documentos/by_day**: Retorna documentos emitidos num dia específico, paginados. Parâmetros de Rota:
* **day**: Data dos documentos no formato "AAAA-MM-DD".
* **np**: Número da página.

**GET/documentos/by_type/**: Retorna documentos de um tipo específico, paginados. Parâmetros de Rota:
* **type**: Tipo do documento.
* **np**: Número da página.

**GET/documento**: Retorna os detalhes de um documento específico. Parâmetros de Rota:
* **id**: Identificador do documento.

**POST/documentos/add**: Adiciona um novo documento. Parâmetros do Formulário:
* **documentID**: Identificador do documento.
* **documentType**: Tipo do documento.
* **emitter**: Emissor do documento.
* **documentNumber**: Número do documento.
* **documentNumberdr (opcional)**: Número DR do documento.
* **documentDate (opcional)**: Data do documento.
* **documentSeries (opcional)**: Série do documento.
* **documentSource (opcional)**: Fonte do documento.
* **documentNotes (opcional)**: Notas sobre o documento.

**GET/autores**: Retorna a página com a lista de autores.

**POST/autores/add**: Adiciona um novo autor. Parâmetros do Formulário:
* **authorName**: Nome do autor.
* **issuedDocument (opcional)**: Documento emitido pelo autor.

### Frontend e estrutura da aplicação 
Nesta secção do relatório será descrito o processo da cosntrução do frontend, bem como as necessidades associados ao desenvolvimento do mesmo. Além disso iremos falar um pouco sobre como se apresenta a estrutura da aplicação desenvolvida.

#### Tecnologias e ferramentas utilizadas
Como resultado da utilização da linguagem Python para o desenvolvimento do código backend, não existe uma grande escolha de ferramentas e *frameworks* para desenvolver o frontend. Portanto simplesmente decidimos em fazer o desenvolvimento da nossa área visual usando *HTML* e *CSS* nativos. 

Desta maneira é possivel fazer uma comunicação coerente com a framework Flask, no sentido de passar a informação de uma camada para outra.

#### Arquitetura da Web app
A arquitetura da aplicação segue uma abordagem de arquitetura em camadas, onde cada camada tem uma responsabilidade específica. A camada de frontend é responsável pela interface do usuário e utiliza HTML e CSS nativos para criar a aparência visual da aplicação. A camada de backend é desenvolvida em Python e utiliza o framework Flask para lidar com as requisições do cliente e processar a lógica de negócio. A camada de dados é composta pela ontologia desenvolvida e armazenada no GraphDB, permitindo o acesso aos dados através de consultas SPARQL. Essa arquitetura permite uma separação clara de responsabilidades e facilita a manutenção e evolução da aplicação. 

Ao abrir a web app desenvolvida, os utilizadores têm acesso a diversas funcionalidades que permitem interagir com a ontologia e obter informações relevantes. Algumas das principais funcionalidades são:

1. **Pesquisa de documentos**: Os utilizadores podem realizar pesquisas na ontologia com base em critérios como data de publicação, tipo de documento, número de referência, entre outros. Isso permite encontrar documentos específicos de forma rápida e eficiente.

2. **Visualização de detalhes do documento**: Ao selecionar um documento na lista de resultados da pesquisa, os utilizadores podem visualizar os detalhes completos do documento, incluindo informações como data de publicação, tipo de documento, emissor, notas e origem de publicação.

3. **Adição de novos documentos**: A aplicação também permite aos utiliuzadores adicionar novos documentos à ontologia. Eles podem preencher os campos necessários, como data de publicação, tipo de documento e emissor, e enviar as informações para serem incorporadas à ontologia.

5. **Consultas SPARQL personalizadas**: A aplicação oferece aos utilizadores a possibilidade de realizar consultas SPARQL personalizadas na ontologia. Isso permite a obtenção de informações mais complexas e a realização de análises específicas com base nos dados armazenados.

### Conclusão
Concluindo, o trabalho prático de RPCW 2024 foi uma oportunidade de aplicar os conhecimentos adquiridos ao longo do semestre na disciplina de Representação e Processamento de Conhecimento Web. O projeto consistiu na criação de uma aplicação web capaz de recolher e adicionar informações de uma ontologia desenvolvida pela equipe de trabalho, baseada nos dados do Diário da República.

Durante o desenvolvimento do projeto, foram enfrentados desafios como a estruturação da ontologia, a recolha e tratamento dos dados, e a implementação do backend e frontend da aplicação. Foram utilizadas tecnologias como o framework *Flask*, *GraphDB* e linguagem *Python* para alcançar os objetivos propostos.

A estrutura da ontologia foi definida com base no contexto de publicação de documentos associados a entidades. Foram criadas classes como *Document* e *Emitter*, estabelecendo relacionamentos entre elas. A recolha dos dados foi realizada através de um script em *Python*, que dividiu o arquivo *JSON* em partes menores para facilitar o processamento. O tratamento dos dados envolveu a correção de erros e a adaptação dos campos para a compatibilidade com a ontologia.

O desenvolvimento do backend foi realizado utilizando o framework *Flask*, que permitiu a criação de rotas e a implementação dos métodos necessários para a interação com a ontologia. O *GraphDB* foi utilizado como base de dados de grafo para armazenar a ontologia e permitir consultas *SPARQL* eficientes.

O frontend da aplicação foi desenvolvido utilizando *HTML* e *CSS* nativos, garantindo uma comunicação coerente com o backend. A arquitetura da aplicação seguiu uma abordagem em camadas, separando as responsabilidades de cada componente.

No geral, o projeto foi bem-sucedido na criação de uma aplicação web funcional, capaz de recolher, adicionar e consultar informações da ontologia desenvolvida. Foram alcançados os objetivos propostos e a equipa adquiriu conhecimentos práticos valiosos no campo da Representação e Processamento de Conhecimento Web.
