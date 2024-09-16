from typing import Optional
from domain.dtos.user.user_dto import TokenDTO
from domain.models.user import User


class UserResponse:
    
    def __init__(self,  message: str, code_status: int, user: Optional[User] = None, is_error: bool = False, access_token: str = "", token_type: str = ""):
        self.user = user
        self.is_error = is_error
        self.message = message
        self.access_token = access_token
        self.token_type = token_type
        self.code_status = code_status
    
     