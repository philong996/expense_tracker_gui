import tkinter as tk
from tkinter import messagebox

# from src.views.admin import AdminPage
from src.views import AdminPage, LoginPage, MenuPage


class ExpenseApp(tk.Tk):
    """Expense main application"""
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.current_user = None
        self.init_login_page()

    def init_login_page(self):
        """Initialize the login page."""
        login_page = LoginPage(self.container, self.on_login_success)
        login_page.pack(fill="both", expand=True)

    def on_login_success(self, user):
        """
        Callback after successful login.
        """
        self.current_user = user  # Save the logged-in user
        self.load_menu_page()

    def load_menu_page(self):
        """Show the MenuPage based on the user's role."""
        for widget in self.container.winfo_children():
            widget.destroy()

        menu_page = MenuPage(self.container, self.current_user, self.navigate_to_page)
        menu_page.pack(fill="both", expand=True)

    def navigate_to_page(self, page_name):
        """Navigate to a different page"""
        # Destroy any existing page in the container
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_name == "admin":
            page = AdminPage(self.container, self.navigate_to_page)
        else:
            messagebox.showwarning("Navigation", "Unknown page!")
            return

        # Pack the new page
        page.pack(fill="both", expand=True)