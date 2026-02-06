from fastapi import FastAPI

from . import routes

router_paths = routes.router

app = FastAPI(title="API de autenticação do CB Lab")
app.include_router(router_paths)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo a API de autenticacao do CB Lab!"}

@app.get(
        "/health", 
        summary="Verificar saúde da API", 
        description="Endpoint para verificar se a API está funcionando corretamente.", 
        tags=["Saúde"]
    )
def health_check():
    return {"status": "OK"}