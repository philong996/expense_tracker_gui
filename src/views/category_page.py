import tkinter as tk
import logging

from tkinter import messagebox, ttk
from src.controllers.category_controller import CategoryController
from src.models.schema import SessionLocal

from .base_page import BasePage

class CategoryPage(BasePage):
    """Category CRUD page"""
    def __init__(self, master, navigate_to_page, logout_callback, category_controller):
        super().__init__(master, navigate_to_page, logout_callback)
        self.logger = logging.getLogger(__name__)
        self.logger.info("loading the expense page")
        self.navigate_to_page = navigate_to_page
        self.category_controller = category_controller
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
        log_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Category Table
        tk.Label(self, text="Existing Categories", font=("Arial", 14, "bold")
                 ).grid(row=4, column=0, columnspan=2, pady=10)

        self.category_table = ttk.Treeview(self
            , columns=("ID", "Name", "Description")
            , show="headings", height=4)
        self.category_table.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # Configure table columns
        self.category_table.heading("ID", text="ID")
        self.category_table.heading("Name", text="Name")
        self.category_table.heading("Description", text="Description")
        self.category_table.column("ID", width=50, anchor="center")
        self.category_table.column("Name", width=150, anchor="w")
        self.category_table.column("Description", width=300, anchor="w")
        self.load_categories()

        # add the navigation and logout buttons
        self.add_navigation_buttons()


    def load_categories(self):
        """Load all categories into the table."""
        try:
            categories = self.category_controller.get_all_categories()
            self.category_table.delete(*self.category_table.get_children())  # Clear existing rows

            for category in categories:
                self.category_table.insert(
                    ""
                    , "end"
                    , values=(category.category_id, category.category_name, category.description))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load categories: {e}")
            self.logger.error(f"Error loading categories: {e}")

    def log_category(self):
        """Validate inputs and save the Category to the database."""
        # Retrieve values from inputs
        try:
            name = self.name_entry.get()
            description = self.description_entry.get()

        except ValueError:
            messagebox.showerror(
                "Input Error", 
                "Invalid input! Please ensure all fields are filled correctly.")
            return
        
        try:
            self.category_controller.create_category(name, description)
            messagebox.showinfo("Success", f"Category {name} created successfully!")
            self.load_categories()
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to log category: {e}")
   
    def clear_inputs(self):
        """Clear all input fields."""
        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        