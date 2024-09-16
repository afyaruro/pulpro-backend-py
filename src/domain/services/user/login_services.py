from domain.dtos.user.userResponse import UserResponse
from domain.services.auth.create_token import CreateToken
from infrastructure.repositories.user.user_repository import UserRepository
from passlib.context import CryptContext
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginService:
    
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.create_token = CreateToken()
        
        
    #Login
    def login(self, email: str, password: str) -> UserResponse:
        user = self.repository.get_user_by_username(email=email)
        if user.email == "":
            return UserResponse(is_error=True, message="user no register", code_status=400)
        
        elif not user or not self.verify_password(password, user.password):
            return UserResponse(is_error=True, message="password incorrect", code_status=400)
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_token.create_access_token(data={"email": user.email, "type": user.type}, expires_delta=access_token_expires)
        return UserResponse(token_type="bearer", access_token=access_token, message="success", is_error=False, code_status=200)
    
    
    
    #Verifica la contraseña
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
    
    
    