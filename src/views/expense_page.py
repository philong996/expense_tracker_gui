from datetime import datetime
import logging

import tkinter as tk
from tkinter import messagebox

from .base_page import BasePage

class ExpensePage(BasePage):
    """Expense Logging Page to insert expenses into the database."""

    def __init__(self, master, navigate_to_page, logout_callback, expense_controller):
        """
        Initialize the Expense Logging Page.
        """
        super().__init__(master, navigate_to_page, logout_callback)
        self.logger = logging.getLogger(__name__)
        self.logger.info("loading the expense page")
        self.navigate_to_page = navigate_to_page
        self.expense_controller = expense_controller
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        title = tk.Label(self, text="Log an Expense", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Amount Input
        tk.Label(self, text="Amount:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Description Input
        tk.Label(self, text="Description:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        # Date Input
        tk.Label(self, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        # Group ID Input
        tk.Label(self, text="Group ID:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.group_id_entry = tk.Entry(self)
        self.group_id_entry.grid(row=4, column=1, padx=5, pady=5)

        # Category ID Input
        tk.Label(self, text="Category ID:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.category_id_entry = tk.Entry(self)
        self.category_id_entry.grid(row=5, column=1, padx=5, pady=5)

        # Buttons
        log_button = tk.Button(self, text="Log Expense", command=self.log_expense)
        log_button.grid(row=6, column=0, columnspan=2, pady=10)

        back_button = tk.Button(self
            , text="Back to Menu"
            , command=lambda: self.navigate_to_page("menu"))
        back_button.grid(row=7, column=0, columnspan=2, pady=5)

    def log_expense(self):
        """Validate inputs and save the expense to the database."""
        # Retrieve values from inputs
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            date = self.date_entry.get()
            group_id = int(self.group_id_entry.get()) if self.group_id_entry.get() else None
            category_id = int(self.category_id_entry.get()) if self.category_id_entry.get() else None
        except ValueError:
            messagebox.showerror(
                "Input Error", 
                "Invalid input! Please ensure all fields are filled correctly.")
            return

        # Insert expense via controller
        # session = SessionLocal()
        # controller = ExpenseController(session)
        try:
            # controller.create_expense(
            #     user_id=self.user_id,
            #     amount=amount,
            #     description=description,
            #     date=date,
            #     group_id=group_id,
            #     category_id=category_id,
            # )
            # session.commit()
            messagebox.showinfo("Success", "Expense logged successfully!")
            self.clear_inputs()
        except Exception as e:
            session.rollback()
            messagebox.showerror("Error", f"Failed to log expense: {e}")
        finally:
            session.close()

    def clear_inputs(self):
        """Clear all input fields."""
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.group_id_entry.delete(0, tk.END)
        self.category_id_entry.delete(0, tk.END)
