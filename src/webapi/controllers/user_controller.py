from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from domain.dtos.user.user_dto import UserCreateDTO, UserLoginDTO
from domain.services.auth.verificar_token import verify_token
from domain.services.user.user_service import UserService
from infrastructure.repositories.user.user_repository import UserRepository

class UserController:
    def __init__(self, repository: UserRepository):
        
        
        self.services = UserService(repository=repository)
        self.router = APIRouter()  

        self.router.post("/user")(self.create_user)
        self.router.post("/login")(self.login_for_access_token)
        self.router.post("/creators")(self.create_creator)
        
        
    #nuevo user, usuario normal
    def create_user(self, user: UserCreateDTO):
        try:
            resp = self.services.create_user(user_create_dto=user, typeUser="User")
            return JSONResponse(content={"message": resp.message, "access_token": resp.access_token, "token_type": resp.token_type}, status_code=resp.code_status)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
        
    # Crear creador de cuestionarios - solo Admin
    #pendiente mandar un correo estructurado con la informacion de la contraseña de su cuenta
    def create_creator(self, user: UserCreateDTO, token: dict = Depends(verify_token)):
        try:
            #info del token
            user_data = token  
            typeUser = user_data.get("type")
            
            if typeUser != "Admin":
                return JSONResponse(content={"message": "unauthorized user"}, status_code=403)
            
            
            resp = self.services.create_user(user_create_dto=user, typeUser="Creator")
            return JSONResponse(content={"message": resp.message,}, status_code=resp.code_status)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
        
    #login
    def login_for_access_token(self, user: UserLoginDTO):
        try:
            userResponse = self.services.login(email=user.email, password=user.password)
            
            if userResponse.is_error:
                return JSONResponse(content={"message": userResponse.message}, status_code=userResponse.code_status)
            
            return JSONResponse(content={"access_token": userResponse.access_token, "token_type": userResponse.token_type, "message": userResponse.message, }, status_code=userResponse.code_status)
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
