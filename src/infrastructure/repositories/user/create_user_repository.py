from domain.models.user import User
from infrastructure.db import get_db_connection


class CreateUserRepository:
    
    def create_user(self, user: User):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password, type) VALUES (%s, %s, %s)", (user.email, user.password, user.type))
            connection.commit()
        except Exception as e:
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()