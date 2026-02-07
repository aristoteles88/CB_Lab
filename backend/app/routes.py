from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .deps import get_db, get_current_user, superuser_required
from . import crud, auth, schemas

token_router = APIRouter(tags=["Autenticação"])


@token_router.post(
        "/token",
        summary="Obter token de acesso",
        description=""""
            Autentica o usuário e retorna um token JWT
            para acesso às rotas protegidas.
        """
    )
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db)
):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not auth.verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


users_router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@users_router.post(
        "/users/",
        response_model=schemas.UserRead,
        summary="Criar novo usuário",
        description="Cria um novo usuário com os dados fornecidos.",
        tags=["Usuários"]
    )
def create_user(
    user: schemas.UserCreate,
    db=Depends(get_db),
    current_user=Depends(superuser_required)
):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    return crud.create_user(db=db, user=user)


@users_router.get(
        "/users/",
        response_model=list[schemas.UserRead],
        summary="Listar usuários",
        description="""
            Retorna uma lista de todos os usuários cadastrados.
            Acesso restrito a superusuários.
        """,
        tags=["Usuários"]
    )
def list_users(
    db=Depends(get_db),
    current_user=Depends(superuser_required)
):
    return crud.list_users(db)


@users_router.get(
        "/users/me/",
        response_model=schemas.UserRead,
        summary="Obter dados do usuário atual",
        description="Retorna os dados do usuário autenticado atualmente.",
        tags=["Usuários"]
    )
def read_current_user(
    current_user_email: str = Depends(get_current_user),
    db=Depends(get_db)
):
    user = crud.get_user_by_email(db, email=current_user_email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user
