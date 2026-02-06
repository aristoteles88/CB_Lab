from datetime import datetime, timedelta
import os
from jose import JWTError, jwt
from passlib.context import CryptContext

from .config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    try:
        to_encode = data.copy()
        expire = datetime.now() + (expires_delta or timedelta(minutes=30))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        raise ValueError("Falha ao criar token JWT")
    return encoded_jwt