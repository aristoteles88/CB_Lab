#!/usr/bin/env python3
"""
Script para criar um superusuário no banco de dados.
Suporta modo não interativo via variáveis de ambiente ou argumentos da linha de comando.
"""
import sys
import os
import argparse

from app.database import SessionLocal
from app.models import User
from app import auth


DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
DB_HOST = os.getenv('DATABASE_HOST')
DB_PORT = os.getenv('DATABASE_PORT')
DB_NAME = os.getenv('DATABASE_NAME')

os.environ['DATABASE_URL'] = os.environ.get('DATABASE_URL', f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def create_superuser(name: str, email: str, password: str) -> bool:
    """Cria um superusuário no banco de dados"""
    db = SessionLocal()
    try:
        # Verifica se o usuário já existe para evitar duplicatas
        existing_user = db.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"⚠️  Usuário com email '{email}' já existe. Pulando criação.")
            return True

        # Utiliza a função de hash de senha do módulo auth para garantir segurança
        hashed_password = auth.hash_password(password)
        superuser = User(
            name=name,
            email=email,
            hashed_password=hashed_password,
            is_superuser=True
        )

        db.add(superuser)
        db.commit()
        db.refresh(superuser)

        print("✅ Superusuário criado com sucesso!")
        print(f"   Nome: {superuser.name}")
        print(f"   Email: {superuser.email}")
        print(f"   ID: {superuser.id}")
        print(f"   É Superusuário: {superuser.is_superuser}")

        return True

    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao criar superusuário: {str(e)}")
        return False

    finally:
        db.close()


def parse_args():
    parser = argparse.ArgumentParser(description="Cria um superusuário no banco de dados")
    parser.add_argument("--name", help="Nome do superusuário")
    parser.add_argument("--email", help="Email do superusuário")
    parser.add_argument("--password", help="Senha do superusuário")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # Priority: CLI args -> ENV vars -> defaults
    name = args.name or os.getenv('SUPERUSER_NAME') or 'Admin'
    email = args.email or os.getenv('SUPERUSER_EMAIL') or 'admin@cb-lab.com'
    password = args.password or os.getenv('SUPERUSER_PASSWORD') or 'admin123'

    success = create_superuser(name, email, password)
    sys.exit(0 if success else 1)
