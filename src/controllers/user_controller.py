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

    def delete_user(self, user_id):
        """Delete user method"""
        user = self.get_user(user_id)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()

    # def update_user(self, user_id):
