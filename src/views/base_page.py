import tkinter as tk

class BasePage(tk.Frame):
    """Base Page class with a logout button."""

    def __init__(self, master, navigate_to_page, logout_callback):
        super().__init__(master)
        self.navigate_to_page = navigate_to_page
        self.logout_callback = logout_callback
    

    def add_navigation_buttons(self):
        "Util function to add navigation buttons and logout"
        # Navigation Buttons
        nav_frame = tk.Frame(self)
        nav_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

        back_button = tk.Button(
            nav_frame
            , text="Back to Menu"
            , command=lambda: self.navigate_to_page("menu"))
        back_button.pack(side="left", padx=10)

        logout_button = tk.Button(
            nav_frame
            , text="Logout"
            , command=self.logout_callback)
        logout_button.pack(side="right", padx=10)
