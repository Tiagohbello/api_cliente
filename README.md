# api_cliente
 
## Introdução ao Projeto:
 O projeto tem como objetivo criar uma API de cadastro de clientes protegida por login de autenticação. Criado usando apenas Django e Django Rest Framework.

## Como rodar o projeto:
 ### Instalar a venv:
 ```
  python -m venv venv 
  venv\Scripts\activate
 ```
 ### Baixar as libs :
 ```
  pip install -r requirements.txt
 ```
### Fazer as migrations:
```
  python manage.py makemigrations
  python manage.py migrate 
```
### Criar o user e rodar projeto:
```
  python manage.py createsuperuser 
```
```
  python manage.py runserver
```
## Tutorial de como autenticar o token no Postman:
### Exportando o arquivo:
Primeiro copiar o arquivo **postman_collection.json** no projeto ir em **import** no **Postman** colocar a opção **raw text** e colar o código.
### Fazendo o token funcionar:
Depois de ir na aba login e colocar o usuario e senha, é necessário seguir os seguintes passos, copiar o **token** , no folder **cliente** 
clicar nos três pontinhos e em seguida em **editar** ir na opção de **Pre-request cripts** e colar o token no **"Authorization: Token ..."**. 

