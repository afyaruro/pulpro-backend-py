from passlib.context import CryptContext
from domain.dtos.user.userMapper import UserMapper
from domain.dtos.user.userResponse import UserResponse
from domain.dtos.user.user_dto import  UserCreateDTO
from domain.services.auth.create_token import CreateToken
from infrastructure.repositories.user.user_repository import UserRepository
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.create_token = CreateToken()
        
    
    def create_user(self, user_create_dto: UserCreateDTO, typeUser: str) -> UserResponse:
        
        user_create_dto.email = user_create_dto.email.strip()
        user_create_dto.password = user_create_dto.password.strip()
        
        if not user_create_dto.email:
            return UserResponse(is_error=True, message="empty email", code_status=400)
        elif not user_create_dto.password:
            return UserResponse(is_error=True, message="empty password", code_status=400)
         
        elif len(user_create_dto.password) < 8:
            return UserResponse(is_error=True, message="password must be 8 characters long",  code_status=400)
            
        elif not user_create_dto.email.endswith('@unicesar.edu.co'):
            return UserResponse(is_error=True, message="Invalid email format, must end with '@unicesar.edu.co'",  code_status=400)
        
        user = UserMapper.userCreateDTO_to_User(user_createDTO=user_create_dto)
        user.type = typeUser
        user.password = pwd_context.hash(user.password)
        
        resp = self.repository.get_user_by_username(email=user.email)
        
        if resp.email != "":
            return UserResponse(is_error=True, code_status=400, message="the user is registered")
        
        self.repository.create_user(user=user)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_token.create_access_token(data={"email": user.email, "type": user.type}, expires_delta=access_token_expires)
        return UserResponse(is_error=False, message="created", user=user, code_status=200, token_type="bearer", access_token=access_token)