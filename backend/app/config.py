import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

DATABASE_USER = os.getenv("DATABASE_USER", "admin")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "admin123")
DATABASE_NAME = os.getenv("DATABASE_NAME", "cb_lab_db")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")  # Porta padrão do PostgreSQL
DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    dbname=DATABASE_NAME
)
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))