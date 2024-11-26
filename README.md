## Descrição
Projeto monitora a funcionalidade de uma aplicação web com Selenium e Docker que requer autenticação.
A aplicação monitora um ambiente wordpress implementado com o docker localmente.
- Verifica: Site está acessível.
- Verifica: Credenciais válidas é bem-sucedido.
- Verifica: Credenciais inválidas é corretamente rejeitado.

## Pré-requisitos
É necessária a instalação do:
- Docker >>> https://www.docker.com/products/docker-desktop/
- Python >>> https://www.python.org/downloads/
- Gerenciador de pacotes do Python
- ChromeDriver >>> https://developer.chrome.com/docs/chromedriver/downloads?hl=pt-br

## Executar Aplicação
- Clone o repositório do GitHub na máquina atual
- No terminal digite >>> git clone https://github.com/wesley-amorim/p-integrador-vi-b.git
- Configurar o ambiente Docker e Python ( Iniciar ambiente WordPress com o Docker) >>> docker-compose up -d
- Acessar o WordPress em >>> http://localhost:8000.
- Atualizar credenciais de login no script 'monitoramentoProjetoWesley.py' no bloco de "código principal".
- Verificar se o Docker assim como os containers do wordpress estão operacionais (baixar a versão desktop)
- Configurar o Python >>> python -m venv venv
- Ativar o ambiente virtual ( Depende do sistema operacional usado )
- Instalar dependencias >>> pip install -r requirements.txt
- Executar script >>> monitoramentoProjetoWesley.py ou run python file na pasta selecionada.

# Introdução
  Este documento descreve o desenvolvimento de uma solução em Python para monitorar a funcionalidade de uma aplicação web,
  além de validar a sua disponibilidade e acessibilidade. A aplicação monitorada é um ambiente WordPress,
  implementado usando Docker. O projeto visa garantir que a aplicação funcione dentro da normalidade,
  verificando credenciais de login e disponibilidade do site.

# Metodologia
  O desenvolvimento foi realizado em um ambiente Windows com o editor Visual Studio Code (VS Code).
  
  ### Tecnologias e ferramentas:
  - Python: Principal linguagem.
  - Selenium: Biblioteca para automação de navegação web.
  - Requests: Biblioteca para verificações HTTP.
  - Docker: Criar um ambiente WordPress local.
  - Chromedriver: Simular a interação do usuário.
  
  ### Etapas do projeto:
  - Configuração do ambiente Docker com WordPress.
  - Script desenvolvido em Python com objetivo de monitorar credenciais assim como a disponibilidade do site.
  - Testes de credenciais inválidas e site indisponível.

# Desenvolvimento
  Um arquivo docker-compose.yml foi criado para configurar o ambiente WordPress. "O conteúdo do arquivo está presente no repositório clonado"

  O serviço define dois contêineres:
  - Containers do WordPress ( porta 8000).
  - Banco de dados MySQL.
  
  O script monitoramentoProjetoWesley.py foi desenvolvido para realizar as principais verificações acompanhado de testes:

  - Verificar se o site está disponível: Utilizando a biblioteca requests para acessar a URL principal do site.
  - Testar credenciais válidas: Verifica se o login com as credenciais corretas redireciona para o painel do WordPress.
  - Testar credenciais inválidas: Simula uma tentativa de login com credenciais incorretas.

# Resultado

  O script foi capaz de identificar corretamente a disponibilidade do site e a funcionalidade de login com credenciais válidas e inválidas. Também detectou situações de indisponibilidade do site.
  
# Conclusão

  O projeto demonstrou como foi possivel monitorar uma aplicação web usando Python e Docker. É possivel incluir diveras outras validações ou testar funcionalidades do WordPress.

