from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    password: str
    email: str
    
class UserLoginDTO(BaseModel):
    password: str
    email: str
    
    
class TokenDTO(BaseModel):
    access_token: str
    token_type: str
