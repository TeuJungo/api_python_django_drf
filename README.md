Django API com DRF, Swagger e Redoc

Este é um projeto Django configurado para fornecer uma API REST usando Django REST Framework (DRF), com documentação interativa através do Swagger e do ReDoc.

🚀 Tecnologias Utilizadas

Django - Framework web para desenvolvimento rápido e seguro.

Django REST Framework (DRF) - Ferramenta para construção de APIs REST.

SQLite - Banco de dados leve e fácil de configurar.

Swagger - Interface interativa para explorar e testar a API.

ReDoc - Documentação elegante e organizada para a API.

📌 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

Python 3.x

Virtualenv (opcional, mas recomendado)

⚙️ Instalação e Configuração

Clone o repositório:

git clone https://github.com/TeuJungo/api_python_django_drf.git
cd seu-repositorio

Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

Instale as dependências do projeto:

pip install -r requirements.txt

Execute as migrações do banco de dados:

python manage.py migrate

Inicie o servidor de desenvolvimento:

python manage.py runserver

📖 Documentação da API

Após iniciar o servidor, acesse os seguintes endpoints para visualizar a documentação da API:

Swagger UI: http://127.0.0.1:8000/swagger/

ReDoc: http://127.0.0.1:8000/redoc/

📂 Estrutura do Projeto

project_root/
│── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│── business/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
│── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
│── manage.py
│── requirements.txt
│── README.md

📌 Endpoints Principais

/api/ - Endpoints principais da API.

/swagger/ - Interface Swagger para explorar os endpoints.

/redoc/ - Documentação alternativa da API com ReDoc.
/business/ - Endpoints para o crud de empresas.

🔧 Comandos Úteis

Criar um superusuário para acessar o painel admin:

python manage.py createsuperuser

Executar testes:

python manage.py test

Aplicar migrações:

python manage.py makemigrations
python manage.py migrate

🛠 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário!

Desenvolvido por Mateus Massaqui Jungo 🚀
