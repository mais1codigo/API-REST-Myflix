# API-REST-Myflix
PROJETO API 

O projeto utiliza:

- Linguagem: **Python** :contentReference[oaicite:0]{index=0}  
- Framework/web server para REST (ex: Django REST Framework, Flask ou FastAPI)  
- Banco de dados relacional (ex: PostgreSQL, SQLite, MySQL)  
- Controle de versão com Git & GitHub  
- Possíveis dependências de autenticação (JWT ou outra)  

---

## Guia passo a passo pra rodar localmente:

```bash
# 1. Clone o repositório
git clone https://github.com/mais1codigo/API-REST-Myflix.git

# 2. Acesse a pasta do projeto
cd API-REST-Myflix

# 3. Crie e ative um ambiente virtual (Python)
python -m venv venv
# No Windows
venv\Scripts\activate
# No macOS / Linux
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Configure variáveis de ambiente
cp .env.example .env
# edite .env com suas configurações (banco de dados, secret keys, etc.)

# 6. Rode migrações (se aplicável)
python manage.py migrate

# 7. Inicie o servidor
python manage.py runserver
