from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

app = FastAPI(title="API de autenticação do CB Lab")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo a API de autenticacao do CB Lab!"}