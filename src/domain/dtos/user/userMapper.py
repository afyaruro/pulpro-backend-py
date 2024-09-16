
from domain.dtos.user.user_dto import UserCreateDTO, UserLoginDTO
from domain.models.user import User


class UserMapper:
    
    @staticmethod
    def userCreateDTO_to_User(user_createDTO: UserCreateDTO) -> User:
        return User(id=0, email=user_createDTO.email, password=user_createDTO.password, type="")