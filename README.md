#  Store API com TDD | FastAPI + MongoDB

API REST desenvolvida com **FastAPI**, **MongoDB** e **TDD com Pytest**. Projeto prático da DIO com foco em testes unitários e de integração, organização em camadas e boas práticas.

---

##  Funcionalidades

- ✅ Cadastro de produtos
- ✅ Listagem de produtos
- ✅ Validação de dados
- ✅ Integração com MongoDB
- ✅ Testes com Pytest (unitários e integração)
- ✅ Organização em camadas (routes, services, models, db)
- ✅ Isolamento da lógica de negócio
- ✅ Variáveis de ambiente com `python-decouple`

---

##  Testes

O projeto utiliza **TDD** como base, com cobertura de:

- Testes unitários de serviços
- Testes de integração das rotas com o banco de dados

 Testes localizados em:  
```bash
app/test/
Execute com:

pytest

🧰 Tecnologias

FastAPI

MongoDB + Motor

Pytest

Python Decouple

📦 Instalação local

Clone o repositório:

git clone https://github.com/JFS-In2YourMind/store-api.git
cd store-api


Crie o ambiente virtual:

python -m venv .venv


Ative o ambiente:

Windows:

.venv\Scripts\activate


Linux/macOS:

source .venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Crie um arquivo .env:

MONGO_URL=mongodb://localhost:27017
DB_NAME=store_db


Rode a aplicação:

uvicorn app.main:app --reload



Projeto desenvolvido por Jaqueline Felix
