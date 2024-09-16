from fastapi import FastAPI
from domain.services.user.user_service import UserService
from infrastructure.repositories.user.user_repository import UserRepository
from webapi.controllers import user_controller

app = FastAPI()

# Inyectar UserService al controlador
user_repository = UserRepository()
user_controller = user_controller.UserController(repository=user_repository)


# Registrar las rutas del controlador en la app
app.include_router(user_controller.router)
