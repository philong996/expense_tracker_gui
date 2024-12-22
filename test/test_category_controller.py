import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from src.controllers.category_controller import CategoryController
from base import BaseTestCase

class TestCategory (BaseTestCase):
    def setUp(self):
        """Set up the test database and session."""
        super().setUp()  # Call base setUp
        self.controller = CategoryController(self.session)
        
    def test_create_category (self):
        category = self.controller.create_category(
            category_name = "name 1",
            description = "des 2"
            )
        self.assertEqual(category.category_name, "name 1")
        self.assertEqual(category.description, "des 2")
        
    def test_get_category(self): 
        test_category = self.controller.create_category(
            category_name = "name 4",
            description = "des 2"
            )
        category = self.controller.get_category_by_id (test_category.category_id)
        self.assertEqual(category.category_name, "name 4")
       
    def test_delete_category(self):
        delete_category = self.controller.create_category(
            category_name="delete_name",
            description="delete_des"
            )
        self.controller.delete_category(delete_category.category_id)
        self.assertIsNone(self.controller.get_category_by_id(delete_category.category_id))
    
    def test_update_category(self):
        update_category = self.controller.update_category(category_id=10, category_name="name3", description="des3")
        self.assertEqual(update_category.category_id, 10)
        self.assertEqual(update_category.category_name, "name3")
        self.assertEqual(update_category.description, "des3")  
        

if __name__ == "__main__":
    unittest.main()      
        