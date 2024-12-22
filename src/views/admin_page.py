import tkinter as tk
from tkinter import messagebox
from .base_page import BasePage

class AdminPage(BasePage):
    "Admin page widget to manage users"
    def __init__(self, master, navigate_to_page, logout_callback, user_controller):
        super().__init__(master, navigate_to_page, logout_callback)
        self.navigate_to_page = navigate_to_page
        self.logout_callback = logout_callback
        self.user_controller = user_controller
        self.init_ui()

    def init_ui(self):
        """Loading page method"""
        # Configure grid columns
        self.grid_columnconfigure(0, weight=1)  # Center-align all content

        # Title
        title_label = tk.Label(self, text="Admin Panel", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Username Label and Input
        username_label = tk.Label(self, text="Username:")
        username_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.username_input = tk.Entry(self)
        self.username_input.grid(row=1, column=1, sticky="w", padx=10, pady=5)

        # Password Label and Input
        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.password_input = tk.Entry(self, show="*")
        self.password_input.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        # Buttons
        add_user_button = tk.Button(self, text="Add User", command=self.add_user)
        add_user_button.grid(row=3, column=0, columnspan=2, pady=10)

        delete_user_button = tk.Button(self, text="Delete User", command=self.delete_user)
        delete_user_button.grid(row=4, column=0, columnspan=2, pady=10)

        reset_password_button = tk.Button(self, text="Reset Password", command=self.reset_password)
        reset_password_button.grid(row=5, column=0, columnspan=2, pady=10)

        # add the navigation and logout buttons
        self.add_navigation_buttons()


    def add_user(self):
        """ Add user functionality"""
        username = self.username_input.get()
        password = self.password_input.get()
        if username and password:
            messagebox.showinfo("Success", f"User {username} added.")
        else:
            messagebox.showerror("Error", "Please enter both username and password.")

    def delete_user(self):
        """ Delete user functionality"""
        username = self.username_input.get()
        if username:
            messagebox.showinfo("Success", f"User {username} deleted.")
        else:
            messagebox.showerror("Error", "Please enter a username to delete.")

    def reset_password(self):
        """Reset password functionality"""
        username = self.username_input.get()
        password = self.password_input.get()
        if username and password:
            
            messagebox.showinfo("Success", f"Password for {username} reset.")
        else:
            messagebox.showerror("Error", "Please enter both username and new password.")

