import logging
import tkinter as tk
from tkinter import messagebox

from src.views import AdminPage, LoginPage, MenuPage, ExpensePage, CategoryPage
from src.controllers import UserController, ExpenseController, CategoryController
from .state import AppState

class ExpenseApp(tk.Tk):
    """Expense main application"""
    def __init__(self, db_session):
        super().__init__()

        self.logger = logging.getLogger(__name__)
        self.logger.info("ExpenseApp initialized successfully.")
        self.title("Expense Tracker")
        self.geometry("800x600")

        self.container = tk.Frame(self)

        # Place the container in the main window
        self.container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)  # Make the container expandable
        self.grid_columnconfigure(0, weight=1)

        # Center placement
        self.container.place(relx=0.5, rely=0.3, anchor="center")

        self.state = AppState.get_instance()

        # Initialize Controllers
        self.db_session = db_session
        self.user_controller = UserController(self.db_session)
        self.expense_controller = ExpenseController(self.db_session)
        self.category_controller = CategoryController(self.db_session)

        self.current_page = None
        self.show_page('login')


    def show_page(self, page_name):
        """Bring the specified page to the front."""
        if page_name == "menu":
            self.current_page = MenuPage(self.container, self.show_page, self.logout)
        elif page_name == "login":
            self.current_page = LoginPage(
                self.container, self.user_controller, self.on_login_success)
        elif page_name == "admin":
            self.current_page = AdminPage(
                self.container, self.show_page, self.logout, self.user_controller)
        elif page_name == "expense":
            self.current_page = ExpensePage(
                self.container, self.show_page, self.logout, self.expense_controller)
        elif page_name == "category":
            self.current_page = CategoryPage(
                self.container, self.show_page, self.logout)
        else:
            messagebox.showwarning("Navigation", "Unknown page!")
            return

        self.current_page.grid(row=0, column=0, sticky="nsew")
        self.current_page.tkraise()

    def on_login_success(self, user):
        """
        Callback after successful login.
        """
        self.state.current_user = user  # Save the logged-in user
        self.logger.info(
            "Login successful for user: %s role: %s",
            AppState.get_instance().current_user.username,
            AppState.get_instance().current_user.role)
        self.show_page("menu")

    def logout(self):
        """Logout the current user and navigate to the login page."""
        self.state.current_user = None  # Clear the logged-in user
        self.show_page('login')