# Projeto Store

### Configuração do ambiente de desenvolvimento

- Para a criação do ambiente virtual e ativação do mesmo

```bash
python -m venv .venv
```

- Ativação do ambiente virtual no Windows

```bash
.venv\Scripts\activate # Windows users
```

- Ativição do ambiente virtual no Linux

```bash
.venv/bin/activate # Unix users
```

Agora vamos instalar a biblioteca do Django em nosso ambiente virtual

```bash
pip install django
```

- Criar o arquivo requirements.txt com as bibliotecas necessárias para o funcionamento do projeto

```bash
pip freeze > requirements.txt
```

- Criar um projeto no Django `o ponto no final` esta atrelado a criar a pasta no mesmo nível

```bash
django-admin startproject config .
```

- Criar a aplicação gerenciada pelo Django

```bash
python manage.py startapp produtos
```

- Configure em `settings.py` a aplicação criada anteriormente.

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos', # Adicione aqui o nome da sua aplicação
]
```

Após criar seu modelo da aplicação na pasta `models.py` execute o comando abaixo

```bash
python manage.py makemigrations
```

- em seguida iniciamos o comando

```bash
python manage.py migrate
```

- Registraremos agora no arquivo `admin.py` o

```python
from django.contrib import admin

from .models import Produto

admin.site.register(Produto)
```

- Agora criaremos o super usuário para acessar o ambiente admin.

```bash
python manage.py createsuperuser
```

- Vamos iniciar o servidor com o comando abaixo

```bash
python manage.py runserver
```

Agora iniciamos o nosso servidor `python manage.py runserver` e acessamos 127.0.0.1:8000/admin o acesso se dará por parte com o nome de usuário e senha que você definiu anteiormente.
