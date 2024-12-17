import tkinter as tk

class MenuPage(tk.Frame):
    """Menu page with buttons, only shows Admin button for admin users."""

    def __init__(self, master, user, navigate_to_page):
        """
        Initialize the MenuPage.
        """
        super().__init__(master)
        self.navigate_to_page = navigate_to_page
        self.user = user
        self.init_buttons()

    def init_buttons(self):
        """Initialize buttons based on the user role."""
        self.master.place(relx=0.5, rely=0.3, anchor="center")  # Center placement

        # Title
        title = tk.Label(self, text="Expense Tracker", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        row_index = 1  # Starting row index

        # Admin button (only if user is admin)
        if self.user.role == "admin":
            admin_button = tk.Button(
                self, text="Admin", width=20, command=lambda: self.navigate_to_page("admin")
            )
            admin_button.grid(row=row_index, column=0, pady=5)
            row_index += 1  # Move to the next row

        # Expense Logging button
        expense_logging_button = tk.Button(
            self, text="Log Expense", width=20, command=lambda: self.navigate_to_page("expense_logging")
        )
        expense_logging_button.grid(row=row_index, column=0, pady=5)
        row_index += 1

        # Dashboard button
        dashboard_button = tk.Button(
            self, text="Dashboard", width=20, command=lambda: self.navigate_to_page("dashboard")
        )
        dashboard_button.grid(row=row_index, column=0, pady=5)
