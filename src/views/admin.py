import tkinter as tk
from tkinter import messagebox


class AdminPage(tk.Frame):
    "Admin page widget to manage users"
    def __init__(self, master, navigate_to_page):
        super().__init__(master)
        self.master = master
        self.navigate_to_page = navigate_to_page
        self.init_ui()

    def init_ui(self):
        """Loading page method"""
        self.title_label = tk.Label(
            self.master, text="Admin Panel", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Username Label and Input
        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_input = tk.Entry(self.master)
        self.username_input.pack()

        # Password Label and Input
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_input = tk.Entry(self.master, show="*")
        self.password_input.pack()

        # Buttons
        self.add_user_button = tk.Button(
            self.master, text="Add User", command=self.add_user)
        self.add_user_button.pack(pady=10)

        self.delete_user_button = tk.Button(
            self.master, text="Delete User", command=self.delete_user)
        self.delete_user_button.pack(pady=10)

        self.reset_password_button = tk.Button(
            self.master, text="Reset Password", command=self.reset_password)
        self.reset_password_button.pack(pady=10)

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

