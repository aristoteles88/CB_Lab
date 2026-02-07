from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import routes

app = FastAPI(title="API de autenticação do CB Lab")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://frontend.cb-lab",
        "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
