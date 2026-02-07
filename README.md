# 📌 CB_Lab

Projeto **CB_Lab** — aplicação web full-stack com backend em Python, frontend em TypeScript, banco de dados Postgres e suporte à execução via Docker-Compose.

Essa aplicação foi desenvolvida para o processo seletivo da Coco Bambu Lab.

🔗 Repositório: https://github.com/aristoteles88/CB_Lab

---

## 🧩 Stack Tecnológica

Este projeto utiliza:

| Camada | Tecnologia |
|--------|------------|
| Backend | **Python** (FastAPI) |
| Frontend | **TypeScript** (Angular) |
| Banco de dados | **Postgres** |
| Containerização | **Docker & Docker-Compose** |
| Build & Scripts | npm(frontend), pip (backend) |
| Serviços auxiliares | Variáveis de ambiente para configuração|

---

## 🚀 Pré-requisitos

Antes de rodar o projeto localmente, instale:

✔️ Python 3.10+  
✔️ Node.js 16+ e npm  
✔️ Postgres 16
✔️ Docker & Docker-Compose *(se for rodar em containers)*

---

## 🛠️ Executando Localmente

### 🧪 Backend

1. Navegue até a pasta backend:

   ```bash
   cd backend
2. Crie e ative um ambiente virtual:
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
3. Instale as dependencias:

   ```bash
   pip install -r requirements.txt
4. Copie o arquivo .env.example para .env

   ```bash
   cp .env.example .env
5. Configure variáveis de ambiente (veja tabela abaixo) no arquivo .env

6. Rode:

   ```bash
   fastapi dev app/main.py
### ⚛️ Frontend

1. Entre na pasta frontend:

    ```bash
    cd frontend
2. Instale pacotes:

    ```bash
    npm install
3. Rode o servidor de desenvolvimento:

    ```bash
    npm serve
Após isso, o frontend deve estar disponível em http://localhost:4200 (ou porta configurada) e o backend em http://localhost:8000 (ou porta configurada).

---

### 🐳 Executando com Docker-Compose

Para executar toda a aplicação com Docker:
1. Copie o exemplo de ambiente:

    ```bash
    cp docker-compose-example.yml docker-compose.yml
2. Ajuste variáveis de ambiente no arquivo docker-compose.yaml conforme necessário.
3. Construa e suba os containers:

   ```bash
   docker compose up --build
4. Acesse:
- Backend: http://localhost:8000
- Frontend: http://localhost:4200

*** Os serviços e portas podem variar conforme configuração no docker-compose.yml.

---
### 🔐 Variáveis de Ambiente

Abaixo está a tabela com variáveis de ambiente importantes para configuração do projeto.

Ajuste os valores conforme sua necessidade.

#### docker-compose.yaml

|Variável|	Descrição|	Valor Default / Exemplo|
|--------|-----------|-------------------------|
|DB_USER|	Usuário admin do banco de dados |	admin|
|DB_PASSWORD|	Senha do suário admin do banco de dados|	admin123|
|DB_NAME|	Nome do banco de dados |	cb_lab_db|
|DB_HOST|	Endereço do banco de dados |	localhost|
|SECRET_KEY|	chave secreta para encode do token |	'your-secret-key'*|
|SU_NAME|	Nome do superusuário criado junto do BD|	Admin|
|SU_EMAIL|	Email do superusuário criado junto do BD|	admin@cb-lab.com|
|SU_PWD|	Senha do superusuário criado junto do BD|	admin123|



#### .env

|Variável|	Descrição|	Valor Default / Exemplo|
|--------|-----------|-------------------------|
|DATABASE_USER|	Usuário admin do banco de dados |	admin|
|DATABASE_PASSWORD|	Senha do suário admin do banco de dados|	admin123|
|DATABASE_NAME|	Nome do banco de dados |	cb_lab_db|
|DATABASE_HOST|	Endereço do banco de dados |	localhost|
|DATABASE_PORT|	Porta do banco de dados |	5432|
|SECRET_KEY|	chave secreta para encode do token |	'your-secret-key'*|

###### * Sugestão para a criação da secret key:

    python3 -c "import secrets; print(secrets.token_urlsafe(32))"