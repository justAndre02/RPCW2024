# Manual de uso da aplicação 

### Requisitos:
* Python: "pip install flask", "pip install requests" e "pip install SPARQLWrapper".
* Docker ou GraphDB Desktop

### Preparação 
#### Primeira Abordagem
Fazer download e instalar a aplicação GraphDB Desktop.

#### Segunda Abordagem 
Se tiver docker fazer pull da imagem **khaller/graphdb-free:latest**.

### Iniciar Servidores
#### Se tem o GraphDB Desktop
Basta executar a aplicação e esta vai redirecionar para a interface web da aplicação, no seu navegador.
Aceder ao ficheiro que inicia o nosso servidor para a web app [app/app.py](app/app.py), abrir o terminal e fazer "**python app.py**".

#### Se tem a imagem no Docker
Se já tiver a imagem do GraphDB do Docker então vamos fazer uma abordagem mais no terminal para isso basta aceder ao [app/Dockerfile](app/Dockerfile). É muito importante verificar a linha "CMD [ "python", "app.py" ]", pois dependendo do sistema operativo que estás a usar ela é diferente, se tiveres a usar Windows ela permanece "CMD [ "python", "app.py" ]", mas se tiveres usar Linux ou macOS ela tem de ser mudada para "CMD [ "python3", "app.py" ]". Após isso abrir o terminal e executar o comando: **docker build -t rpcw2024tp/webapp .**
Após isso aceder ao ficheiro [app/docker-compose.yaml](app/docker-compose.yaml), abrir o terminal e executar: **docker-compose build** e **docker-compose up -d**. Esperar cerca de 30 segundos e depois aceder ao navegador e abrir as ligações: "http://localhost:7200/"e "http://127.0.0.1:5000".

### Colocar ontologia no GraphDB 
Após iniciar o GraphDB será aceder à secção "Setup/Repositories" e criar um novo repositório escolhendo a primeira opção "GraphDB Repository". No campo "Repository ID" colocar "DRE" e na descrição algo que quiseres não é obrigatório. Dar scroll para baixo e clicar em "Create". Colocar o repositório ativo e aceder à secção "Import" do lado esquerdo. Normalmente teriuamos de escolhero botão "Upload RDF files" para adicionar o nosso ficheiro TTL, mas como este ultrapassa os 200mb permitidos temos de tentar outra abordagem. 

Selcionamos a aba "Server files" e clicamos no botáo de help do lado direito, este vai nos dar a informação de aonde temos de colcocar o nosso ficheiro localmente de modo a poder dar upload. No nosso caso seria: "Put files or directories you want to import into /root/graphdb-import." Isto significava que teria de aceder à pasat "root" e lá criar o diretório "graphdb-import", onde colcoaria o ficherio TTL. Esta localização depende de cada computador. O ficheiro TTL com a ontologia povoada encontra-se disponível para download nio link:  https://drive.google.com/file/d/1T-HtpgDvD0JAKYtx6B4jlYQJRvZAkSS3/view?usp=sharing.

Este processo de importar demora alguuns minutos. Após a cnclusão do mesmo basta atualizar a página da nossa aplicação web e começar a usufruir dela.