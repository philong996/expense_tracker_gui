import tkinter as tk
import logging

from tkinter import messagebox
from src.controllers.category_controller import CategoryController
from src.models.schema import SessionLocal

from .base_page import BasePage
class CategoryPage(BasePage):
    def __init__(self, master, navigate_to_page, logout_callback):
        super().__init__(master, navigate_to_page, logout_callback)
        self.logger = logging.getLogger(__name__)
        self.logger.info("loading the expense page")
        self.navigate_to_page = navigate_to_page
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI components."""
        title = tk.Label(self, text="Log an Category", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        tk.Label(self, text="name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self, text="description:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.description_entry = tk.Entry(self)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)
        
        log_button = tk.Button(self, text="Log Category", command=self.log_category)
        log_button.grid(row=6, column=0, columnspan=2, pady=10)

        
        # add the navigation and logout buttons
        self.add_navigation_buttons()

    def log_category(self):
        """Validate inputs and save the Category to the database."""
        # Retrieve values from inputs
        try:
            name = float(self.name_entry.get())
            description = self.description_entry.get()
            
        except ValueError:
            messagebox.showerror(
                "Input Error", 
                "Invalid input! Please ensure all fields are filled correctly.")
            return
        
        
        try:
            messagebox.showinfo("Success", "Category logged successfully!")
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to log category: {e}")
   
    def clear_inputs(self):
        """Clear all input fields."""
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        