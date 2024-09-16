from domain.models.user import User
from infrastructure.db import get_db_connection


class GetUserByUsernameRepository:
    def get_user_by_username(self, email: str) -> User:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,)) 
            user_data = cursor.fetchone()
            if user_data:
                return User(
                    id=user_data['ID'], 
                    email=user_data['email'], 
                    password=user_data['password'],
                    type=user_data['type']
                )
                
                
            return User(id="", password="", type="", email="")
        except Exception as e:
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()
