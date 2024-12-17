from src.models.schema import Category
from .base import BaseController




class CategoryController  (BaseController):
    """Controller to manage User-related operations (CRUD)"""
    def Create_Category(self, category_name, description, role='category'):
        "Create category method"
        new_category = Category (category_name=category_name, description=description, role=role)
        try:
            self.db_session.add(new_category)
            self.db_session.commit()
            return new_category
        except Exception as e:
            self.db_session.rollback()
            raise e

    def get_Category(self, catrgory_id):
        "Get user method"
        return self.db_session.query(Category).get(catrgory_id)

    def delete_Category(self, category_id):
        """Delete user method"""
        user = self.get_user(category_id)
        if user:
            self.db_session.delete(Category)
            self.db_session.commit()
            
    #def expenses 