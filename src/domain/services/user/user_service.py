from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from domain.dtos.user.userMapper import UserMapper
from domain.dtos.user.userResponse import UserResponse
from domain.dtos.user.user_dto import TokenDTO, UserCreateDTO
from domain.models.user import User
from domain.services.user.create_user_services import CreateUserService
from domain.services.user.login_services import LoginService
from infrastructure.repositories.user.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    
    #Contructor
    def __init__(self, repository: UserRepository):
        self.repository = repository
        self.createUser = CreateUserService(repository=self.repository)
        self.loginUser = LoginService(repository=self.repository)

    #Crear usuario
    def create_user(self, user_create_dto: UserCreateDTO, typeUser: str) -> UserResponse:
        return self.createUser.create_user(user_create_dto=user_create_dto, typeUser=typeUser)

    #login usuario
    def login(self, email: str, password: str) -> UserResponse:
        return self.loginUser.login(email=email, password=password)

