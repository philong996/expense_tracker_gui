import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.schema import Base

class BaseTestCase(unittest.TestCase):
    """Base test case class for setting up and tearing down the database."""

    @classmethod
    def setUpClass(cls):
        """Set up the in-memory database and create tables."""
        cls.engine = create_engine("postgresql+psycopg2://postgres:changeme@localhost/expense_gui")
        Base.metadata.create_all(cls.engine)  # Create all tables
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        """Set up a new session for each test case."""
        self.session = self.Session()

    def tearDown(self):
        """Rollback and close the session after each test."""
        self.session.rollback()  # Rollback any changes made during the test
        self.session.close()

