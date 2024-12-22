import logging

from src.models.schema import init_db
from src.views import ExpenseApp 
from src.models.schema import SessionLocal


# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        # logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

def main():
    """Main function to run the GUI application"""
    # Shared logger instance
    logger = logging.getLogger("ExpenseApp")
    logger.info("Starting the app")

    # Initialize the database
    init_db()

    # Create an instance of the MenuPage
    db_session = SessionLocal()
    app = ExpenseApp(db_session)
    app.mainloop()
    

if __name__ == "__main__":
    main()