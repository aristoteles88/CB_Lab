from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_superuser: bool = False

class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_superuser: bool

    class Config:
        orm_mode = True