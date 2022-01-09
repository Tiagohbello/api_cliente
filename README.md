﻿# api_cliente
 
##Introdução ao Projeto:
 O projeto tem como objetivo criar uma API de cadastro de clientes protegida por login de autenticação. Criado usando apenas Django e Django Rest Framework.

## Como rodar o projeto:
 ### instalar a venv:
 ```
  python -m venv venv 
  venv\Scripts\activate
 ```
 ### Baixar as libs :
 ```
  pip install -r requirements.txt
 ```
### fazer as migrations:
```
  python manage.py makemigrations
  python manage.py migrate 
```
### criar o user e rodar projeto:
```
  python manage.py createsuperuser 
```
```
  python manage.py runserver
```
## conclusão:
Agora só abrir a collection do postman e consumir as apis, pegando a autenticação na api de login. 

