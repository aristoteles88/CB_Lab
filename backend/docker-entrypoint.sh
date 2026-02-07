#!/usr/bin/env bash
set -e

: "${DATABASE_HOST}"
: "${DATABASE_PORT}"
: "${DATABASE_USER}"
: "${DATABASE_PASSWORD}"
: "${DATABASE_NAME}"
: "${SUPERUSER_NAME:=Admin}"
: "${SUPERUSER_EMAIL:=admin@cb-lab.com}"
: "${SUPERUSER_PASSWORD:=admin123}"

export PGPASSWORD="$DATABASE_PASSWORD"

echo "Aguardando Postgres em ${DATABASE_HOST}:${DATABASE_PORT}..."
until pg_isready -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USER" -d "$DATABASE_NAME" >/dev/null 2>&1; do
  sleep 1
done
echo "Postgres está pronto!."

# Cria superusuário (Ignora erros e cria o container mesmo se o superusuário já existir)
python /app/create_superuser.py --name "$SUPERUSER_NAME" --email "$SUPERUSER_EMAIL" --password "$SUPERUSER_PASSWORD" || true

# Executa o CMD passado
exec "$@"
