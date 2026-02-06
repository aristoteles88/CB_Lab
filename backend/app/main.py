from fastapi import FastAPI

from . import routes

app = FastAPI(title="API de autenticação do CB Lab")

# Inclui rotas
app.include_router(routes.token_router)
app.include_router(routes.users_router)


@app.get("/")
def read_root():
    return {"message": "Bem-vindo a API de autenticacao do CB Lab!"}


@app.get(
        "/health",
        summary="Verificar saúde da API",
        description="""
            Endpoint para verificar se a API
            está funcionando corretamente.
    """,
        tags=["Saúde"]
    )
def health_check():
    return {"status": "OK"}
