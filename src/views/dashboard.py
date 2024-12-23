import logging
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from .state import AppState
from .base_page import BasePage

class DashboardPage(BasePage):
    """Dashboard Page for displaying statistics."""

    def __init__(self, master, navigate_to_page, logout_callback, expense_controller):
        super().__init__(master, navigate_to_page, logout_callback)
        self.logger = logging.getLogger(__name__)
        self.logger.info("loading the menu page")
        self.state = AppState.get_instance()
        self.expense_controller = expense_controller
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        # Title
        title_label = tk.Label(self, text="Dashboard", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Total Expenses
        self.total_expenses_label = tk.Label(self, text="Total Expenses: $0.00", font=("Arial", 16))
        self.total_expenses_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Fetch total expenses
        total_expenses = self.expense_controller.get_total_expenses(
            user_id=self.state.current_user.user_id)
        self.total_expenses_label.config(text=f"Total Expenses: ${total_expenses:.2f}")

        # Expense by Category Table
        tk.Label(self, text="Expenses by Category", font=("Arial", 14, "bold")).grid(row=2, column=0, columnspan=2)
        self.expense_table = ttk.Treeview(self, columns=("Category", "Amount"), show="headings", height=5)
        self.expense_table.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

        # Configure table columns
        self.expense_table.heading("Category", text="Category")
        self.expense_table.heading("Amount", text="Amount")
        self.expense_table.column("Category", anchor="w", width=150)
        self.expense_table.column("Amount", anchor="e", width=100)

        # Fetch expenses by category
        expenses_by_category = self.expense_controller.get_expenses_by_category(
            user_id=self.state.current_user.user_id
        )
        self.expense_table.delete(*self.expense_table.get_children())  # Clear existing rows
        for category, amount in expenses_by_category:
            self.expense_table.insert("", "end", values=(category, f"${amount:.2f}"))


        # Navigation Buttons
        self.add_navigation_buttons()