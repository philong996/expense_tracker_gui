from src.models.schema import User
from .base import BaseController


class UserController(BaseController):
    """Controller to manage User-related operations (CRUD)"""
    def create_user(self, username, email, password_hash, role='user'):
        "Create user method"
        new_user = User(username=username, email=email, password_hash=password_hash, role=role)
        try:
            self.db_session.add(new_user)
            self.db_session.commit()
            return new_user
        except Exception as e:
            self.db_session.rollback()
            raise e

    def get_user(self, user_id):
        "Get user method"
        return self.db_session.query(User).get(user_id)

    def get_user_by_email(self, email: str):
        "Get user by email method"
        user = self.db_session.query(User).filter(User.email == email).first()
        return user

    def get_user_by_username(self, username: str):
        "Get user by username method"
        user = self.db_session.query(User).filter(User.username == username).first()
        return user

    def delete_user(self, user_id):
        """Delete user method"""
        user = self.get_user(user_id)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()

    def validate_user(self, username, password):
        """Validate user credentials from database."""
        try:
            user = self.get_user_by_username(username)
            if user and user.password_hash == password:
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            self.db_session.close()
