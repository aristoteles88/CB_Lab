from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from .database import SessionLocal
from . import models

from .config import SECRET_KEY, ALGORITHM

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return email
    except JWTError:
        raise credentials_exception


def superuser_required(
    current_user_email: str = Depends(get_current_user),
    db=Depends(get_db)
):
    user = db.query(models.User)\
        .filter(models.User.email == current_user_email)\
        .first()
    if not user or not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado. Superusuário necessário.",
        )
    return user
