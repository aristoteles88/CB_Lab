import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient
from testcontainers.postgres import PostgresContainer

from app.main import app as fastapi_app
from app.database import Base
from app.deps import get_db
import app.models

# ==============================
#  POSTGRES PARA TESTES (DOCKER)
# ==============================

@pytest.fixture(scope="session")
def postgres_container():
    """Sobe um PostgreSQL real em Docker só para os testes."""
    with PostgresContainer("postgres:16-alpine") as postgres:
        os.environ["DATABASE_URL"] = postgres.get_connection_url()
        yield postgres

@pytest.fixture(scope="session")
def engine(postgres_container):
    """Cria engine apontando para o Postgres de testes."""
    engine = create_engine(
        os.environ["DATABASE_URL"],
        pool_pre_ping=True,
    )

    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)

    yield engine

    # Limpa tudo ao final da sessão
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(engine):
    """Sessão limpa por teste."""
    TestingSessionLocal = sessionmaker(bind=engine)
    db = TestingSessionLocal()

    yield db

    db.rollback()
    db.close()

# ==============================
#  CLIENTE FASTAPI
# ==============================

@pytest.fixture
def client(db_session):
    """Sobrescreve get_db para usar o Postgres de teste."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    fastapi_app.dependency_overrides[get_db] = override_get_db

    with TestClient(fastapi_app) as c:
        yield c

    fastapi_app.dependency_overrides.clear()

# ==============================
#  DADOS DE TESTE
# ==============================

@pytest.fixture
def superuser(db_session):
    user = app.models.User(
        name="Admin",
        email="admin@test.com",
        hashed_password="$2b$12$testhash",
        is_superuser=True,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def normal_user(db_session):
    user = app.models.User(
        name="User",
        email="user@test.com",
        hashed_password="$2b$12$testhash",
        is_superuser=False,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
