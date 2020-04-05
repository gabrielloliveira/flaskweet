# FlaskWeet

Uma aplicação simples feita em flask para tweets.

<figure>
  <img src="https://raw.githubusercontent.com/gabrielloliveira/flaskweet/master/img/login.png" style="display:block; margin: 0 auto">
  <figcaption style="text-align: center">Tela de login</figcaption>
</figure>

## Requerimento

- Python >= 3.6

## Instalação

- Clone o projeto.

  ```git clone https://github.com/gabrielloliveira/flaskweet.git```

- Entre dentro da pasta ```flaskweet``` e crie um virtualenv.

  ```python -m venv env```

- Ative o virtualenv.

  ```source env/bin/activate```

- Instale os requerimentos do projeto.

  ```pip install -r requirements.txt```

- Crie o banco de dados.

  1. ```python manage.py db migrate```

  2. ```python manage.py db upgrade```

- Inicie o servidor.

  ```python manage.py runserver```

- Acesse [http://localhost:5000/](http://localhost:5000/)

## Imagens do projeto

<figure>
  <img src="https://raw.githubusercontent.com/gabrielloliveira/flaskweet/master/img/cadastro.png" style="display:block; margin: 0 auto">
  <figcaption style="text-align: center">Tela de cadastro de usuário</figcaption>
</figure>

<figure>
  <img src="https://raw.githubusercontent.com/gabrielloliveira/flaskweet/master/img/home.png" style="display:block; margin: 0 auto">
  <figcaption style="text-align: center">Tela home</figcaption>
</figure>

<figure>
  <img src="https://raw.githubusercontent.com/gabrielloliveira/flaskweet/master/img/busca.png" style="display:block; margin: 0 auto">
  <figcaption style="text-align: center">Pesquisa de usuário</figcaption>
</figure>
