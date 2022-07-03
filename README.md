# A aplicação flask mais simples do mundo

## Rodando

Basta seguir os passos abaixo para rodar a aplicação em container Docker. 

A porta 80 já está definida no código, e a variável de ambiente `API_TOKEN` é necessária para definir o token da aplicação.

* Crie o arquivo `.env` com o conteúdo abaixo (ela será carregada pelo pacote `python-dotenv`):

```bash
export API_TOKEN=supersecret
```

> *** O comando export é ignorado pelo `python-dotenv`, mas permite que o `.env` possa ser reaproveitado pelo comando `source .env`.

* Construa a imagem:
  
```bash
$ docker build -f Dockerfile -t topaz-devops-challenge .
```

* Inicie a execução do container:

```bash
$ source .env

$ docker run -it --rm --name topaz-devops-challenge-dev -p 80:80 -e API_TOKEN=$API_TOKEN topaz-devops-challenge
```

* Em outro terminal, acesse a aplicação:

```bash
$ source .env

$ curl -H "Authorization: Token $API_TOKEN" http://localhost/
```
