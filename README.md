# Flask App With DB And Nginx

Exemplo simplificado de uma aplicação web usando o Flask que menipula dados de um banco de dados (Postgres) rodando com Gunicorn e Nginx.
É possível ver a criação completa dessa aplicação na postagem [Aplicação Flask usando Nginx e Gunicorn](https://programero.blogspot.com/2025/01/aplicacao-flask-usando-nginx-e-gunicorn.html)

## Configuração do Ambiente

### Requisitos
- Docker
- Docker Compose

### Passos para Rodar a Aplicação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/app_flask_with_db_and_nginx.git
   cd xxx
   ```
2. Inicie os contêiners usando o Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. A aplicação estará disponível em `http://localhost:5000`.

