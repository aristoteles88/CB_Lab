FROM python:3.12-slim

WORKDIR /app

# Instala dependências de sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copia requirements.txt
COPY requirements.txt .

# Instala dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY . .

# Copia entrypoint e o torna executável
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expõe porta
EXPOSE 8000

# Entrypoint aguarda o banco de dados, cria o superusuário e executa o CMD
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]
