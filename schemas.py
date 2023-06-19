from pydantic import BaseModel


class UserCreatePayload(BaseModel):
    name: str
    cpf: str
    email: str
    phone_number: str


class AlterUserPayload(BaseModel):
    name: str
    cpf: str
    email: str
    phone_number: str


class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class UserListOutput(BaseModel):
    id: int
    cpf: str
    name: str

    class Config:
        orm_mode = True
