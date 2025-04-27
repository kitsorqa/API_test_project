from pydantic import BaseModel


class ResponseUser(BaseModel):
    code: int
    type: str
    message: str


class ResponseUserByUsername(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int
