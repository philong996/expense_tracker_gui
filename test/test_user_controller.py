import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.controllers.user_controller import UserController

class TestUserController(unittest.TestCase):
    """User controller tests"""
    def setUp(self):
        """Set up the test database and session."""
        super().setUp()  # Call base setUp
        self.controller = UserController(self.session)

    def test_create_user(self):
        """Test creating a new user."""
        user = self.controller.get_user_by_email('test@example.com')
        if user:
            self.controller.delete_user(user.user_id)
 
        user = self.controller.create_user(
            username="testuser",
            email="test@example.com",
            password_hash="hashed_password",
            role="user"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.role, "user")


        if self.controller.get_user_by_username('admin') is None:
            self.controller.create_user(
                username="admin",
                email="admin@example.com",
                password_hash="admin",
                role="admin"
            )


    def test_create_duplicate_user(self):
        """Test that creating a user with duplicate username or email raises an error."""
        with self.assertRaises(IntegrityError):
            self.controller.create_user(
                username="testuser",
                email="test@example.com",
                password_hash="hashed_password2",
            )

    def test_get_user(self):
        """Test retrieving a user by ID."""
        user = self.controller.get_user_by_email('test@example.com')

        retrieved_user = self.controller.get_user(user.user_id)
        self.assertEqual(retrieved_user.username, "testuser")

    def test_delete_user(self):
        """Test deleting a user by ID."""
        delete_user = self.controller.create_user(
            username="deleted_testuser",
            email="deleted_test@example.com",
            password_hash="hashed_password2",
        )
        self.user_controller.delete_user(delete_user.user_id)
        self.assertIsNone(self.user_controller.get_user(delete_user.user_id))

if __name__ == "__main__":
    unittest.main()
