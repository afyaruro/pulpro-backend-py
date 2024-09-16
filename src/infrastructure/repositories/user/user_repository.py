from domain.models.user import User
from infrastructure.db import get_db_connection
from infrastructure.repositories.user.create_user_repository import CreateUserRepository
from infrastructure.repositories.user.get_user_by_username_repository import GetUserByUsernameRepository

class UserRepository:
    
    #Contructor
    def __init__(self):
        self.create_user_repository = CreateUserRepository()
        self.get_user_by_username_repository = GetUserByUsernameRepository()
        
    #crear usuario    
    def create_user(self, user: User):
        self.create_user_repository.create_user(user=user)

    #usuario por username
    def get_user_by_username(self, email: str) -> User:
        return self.get_user_by_username_repository.get_user_by_username(email=email)

