import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.controllers.user_controller import UserController

class TestUserController(unittest.TestCase):
    """User controller tests"""
    def setUp(self):
        """Set up the test database and session."""
        # In-memory SQLite database
        # self.engine = create_engine('sqlite:///:memory:')  
        self.engine = create_engine("postgresql+psycopg2://postgres:changeme@localhost/expense_gui")  
        
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.user_controller = UserController(self.session)

    def tearDown(self):
        """Tear down the test database."""
        self.session.close()

    def test_create_user(self):
        """Test creating a new user."""
        user = self.user_controller.create_user(
            username="testuser2",
            email="test2@example.com",
            password_hash="hashed_password",
            role="user"
        )
        self.assertEqual(user.username, "testuser2")
        self.assertEqual(user.email, "test2@example.com")
        self.assertEqual(user.role, "user")

    def test_create_duplicate_user(self):
        """Test that creating a user with duplicate username or email raises an error."""
        with self.assertRaises(IntegrityError):
            self.user_controller.create_user(
                username="testuser",
                email="test2@example.com",
                password_hash="hashed_password2",
            )
        with self.assertRaises(IntegrityError):
            self.user_controller.create_user(
                username="testuser2",
                email="test@example.com",
                password_hash="hashed_password2",
            )

    def test_get_user(self):
        """Test retrieving a user by ID."""
        user = self.user_controller.get_user_by_email('test@example.com')

        retrieved_user = self.user_controller.get_user(user.user_id)
        self.assertEqual(retrieved_user.username, "testuser")

    def test_delete_user(self):
        """Test deleting a user by ID."""
        delete_user = self.user_controller.create_user(
            username="deleted_testuser",
            email="deleted_test@example.com",
            password_hash="hashed_password2",
        )
        self.user_controller.delete_user(delete_user.user_id)
        self.assertIsNone(self.user_controller.get_user(delete_user.user_id))

if __name__ == "__main__":
    unittest.main()
