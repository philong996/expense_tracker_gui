import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.controllers.user_controller import UserController

from test.base import BaseTestCase

class TestUserController(BaseTestCase):
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
        self.controller.delete_user(delete_user.user_id)
        self.assertIsNone(self.controller.get_user(delete_user.user_id))

    def test_update_user_password(self):
        """Test updating a user's password."""
        # Create a user
        user = self.controller.create_user(
            username="update_password_user",
            email="update_password_user@example.com",
            password_hash="oldpasswordhash"
        )

        # Update the password
        updated_user = self.controller.update_user_password(user.user_id, "newpasswordhash")
        self.assertEqual(updated_user.password_hash, "newpasswordhash")

        # Verify the password was updated in the database
        retrieved_user = self.controller.get_user(user.user_id)
        self.assertEqual(retrieved_user.password_hash, "newpasswordhash")

    def test_update_user_password_user_not_found(self):
        """Test updating the password of a non-existent user."""
        with self.assertRaises(Exception) as context:
            self.controller.update_user_password(user_id=999, new_password_hash="newhash")
        self.assertIn("User with ID 999 not found", str(context.exception))

if __name__ == "__main__":
    unittest.main()
