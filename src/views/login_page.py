import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Frame):
    """Login Page to validate user credentials."""
    def __init__(self, master, user_controller, on_login_success):
        super().__init__(master)
        self.on_login_success = on_login_success  # Callback for successful login
        self.user_controller = user_controller
        self.init_ui()

    def init_ui(self):
        """UI for login page."""
        title = tk.Label(self, text="Login", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self, text="Login", command=self.validate_login)
        login_button.pack(pady=10)

    def validate_login(self):
        """Validate user credentials."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.user_controller.validate_user(username, password):
            user = self.user_controller.get_user_by_username(username)
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.on_login_success(user)
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")