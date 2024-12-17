from src.models.schema import init_db
from src.views.gui_app import ExpenseApp 


def main():
    """Main function to run the GUI application"""
    # Initialize the database
    init_db()

    # Create an instance of the MenuPage
    app = ExpenseApp()
    app.mainloop()
    

if __name__ == "__main__":
    main()