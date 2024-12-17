from src.controllers import ExpenseController
from src.models.schema import Expense
from datetime import datetime
from base import BaseTestCase  # Import the base test case

class TestExpenseController(BaseTestCase):
    """Unit tests for the ExpenseController."""

    def setUp(self):
        """Call the base setup and initialize the controller."""
        super().setUp()
        self.controller = ExpenseController(self.session)

    def test_create_expense(self):
        """Test creating a new expense."""
        expense = self.controller.create_expense(
            amount=50.25,
            description="Test Expense",
            date="2024-06-04",
            user_id=8
        )
        self.assertIsNotNone(expense.expense_id)
        self.assertEqual(expense.amount, 50.25)
        self.assertEqual(expense.description, "Test Expense")
        self.assertEqual(expense.user_id, 8)

    def test_get_expense_by_id(self):
        """Test retrieving an expense by ID."""
        created_expense = self.controller.create_expense(
            amount=100.00,
            description="Retrieve Test",
            date="2024-06-05",
            user_id=8
        )
        retrieved_expense = self.controller.get_expense_by_id(created_expense.expense_id)
        self.assertIsNotNone(retrieved_expense)
        self.assertEqual(retrieved_expense.amount, 100.00)

if __name__ == "__main__":
    unittest.main()
