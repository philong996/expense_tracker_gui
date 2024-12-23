import logging
from datetime import datetime, timedelta
from src.models.schema import init_db, SessionLocal
from src.controllers.user_controller import UserController
from src.controllers.category_controller import CategoryController
from src.controllers.expense_controller import ExpenseController

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def setup_dummy_data():
    """Set up dummy data for users, categories, and expenses."""
    session = SessionLocal()
    
    try:
        # Create tables
        init_db()
        logger.info("Database tables created.")

        # Initialize controllers
        user_controller = UserController(session)
        category_controller = CategoryController(session)
        expense_controller = ExpenseController(session)

        # Add dummy users
        logger.info("Adding dummy users...")
        users = [
            {"username": "admin"
            , "email": "admin@example.com"
            , "password_hash": "123"
            , "role": "admin"},
            {"username": "user1"
            , "email": "user1@example.com"
            , "password_hash": "123"
            , "role": "user"},
            {"username": "user2"
            , "email": "user2@example.com"
            , "password_hash": "123"
            , "role": "user"},
        ]
        for user in users:
            user_controller.create_user(**user)
        logger.info("Dummy users added.")

        # Add dummy categories
        logger.info("Adding dummy categories...")
        categories = ["Groceries"
        , "Transportation"
        , "Entertainment"
        , "Utilities"
        , "Healthcare"]
        for category in categories:
            category_controller.create_category(category_name=category, description=None)
        logger.info("Dummy categories added.")

        # Add dummy expenses
        logger.info("Adding dummy expenses...")
        expenses = [
            {"user_id": 1
            , "amount": 50.0
            , "description": "Weekly groceries"
            , "date": datetime.now()
            , "category_id": 1},
            {"user_id": 1
            , "amount": 20.0
            , "description": "Bus ticket"
            , "date": datetime.now() - timedelta(days=1)
            , "category_id": 2},
            {"user_id": 2
            , "amount": 100.0
            , "description": "Concert tickets"
            , "date": datetime.now() - timedelta(days=2)
            , "category_id": 3},
            {"user_id": 2
            , "amount": 30.0
            , "description": "Electricity bill"
            , "date": datetime.now() - timedelta(days=3)
            , "category_id": 4},
            {"user_id": 3
            , "amount": 25.0
            , "description": "Doctor visit"
            , "date": datetime.now() - timedelta(days=4)
            , "category_id": 5},
        ]
        for expense in expenses:
            expense_controller.create_expense(**expense)
        logger.info("Dummy expenses added.")

        # Commit changes
        session.commit()
        logger.info("Dummy data successfully committed to the database.")

    except Exception as e:
        logger.error(f"An error occurred while setting up dummy data: {e}")
        session.rollback()
    finally:
        session.close()
        logger.info("Database session closed.")

if __name__ == "__main__":
    setup_dummy_data()
