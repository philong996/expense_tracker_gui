from src.models.schema import Expense
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.controllers.base import BaseController

class ExpenseController(BaseController):
    """Controller for managing expenses in the database."""

    def create_expense(self, amount, description, date, user_id, group_id=None, category_id=None):
        """
        Create a new expense entry in the database.
        """
        try:
            # Parse date if passed as string
            if isinstance(date, str):
                date = datetime.strptime(date, "%Y-%m-%d").date()

            # Create an Expense object
            new_expense = Expense(
                amount=amount,
                description=description,
                date=date,
                user_id=user_id,
                group_id=group_id,
                category_id=category_id,
            )
            self.db_session.add(new_expense)
            self.db_session.commit()
            return new_expense
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise Exception(f"Failed to create expense: {e}")

    def get_expense_by_id(self, expense_id):
        """
        Retrieve an expense by its ID.
        """
        return self.db_session.query(Expense).filter_by(expense_id=expense_id).first()

    def update_expense(self, expense_id, amount=None, description=None, date=None, group_id=None, category_id=None):
        """
        Update an existing expense.
        """
        try:
            expense = self.get_expense_by_id(expense_id)
            if not expense:
                raise Exception(f"Expense with ID {expense_id} not found.")

            # Update fields only if new values are provided
            if amount is not None:
                expense.amount = amount
            if description is not None:
                expense.description = description
            if date is not None:
                if isinstance(date, str):
                    date = datetime.strptime(date, "%Y-%m-%d").date()
                expense.date = date
            if group_id is not None:
                expense.group_id = group_id
            if category_id is not None:
                expense.category_id = category_id

            self.db_session.commit()
            return expense
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise Exception(f"Failed to update expense: {e}")

    def delete_expense(self, expense_id):
        """
        Delete an expense by its ID.
        """
        try:
            expense = self.get_expense_by_id(expense_id)
            if not expense:
                raise Exception(f"Expense with ID {expense_id} not found.")

            self.db_session.delete(expense)
            self.db_session.commit()
            return True
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise Exception(f"Failed to delete expense: {e}")

    def get_all_expenses(self, user_id=None, group_id=None, category_id=None):
        """
        Retrieve all expenses with optional filters.
        """
        query = self.db_session.query(Expense)

        if user_id is not None:
            query = query.filter_by(user_id=user_id)
        if group_id is not None:
            query = query.filter_by(group_id=group_id)
        if category_id is not None:
            query = query.filter_by(category_id=category_id)

        return query.all()
