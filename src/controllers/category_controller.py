from src.models.schema import Category
from .base import BaseController
from sqlalchemy.exc import SQLAlchemyError
from src.controllers.base import BaseController

class CategoryController(BaseController):
    """Controller to manage User-related operations (CRUD)"""
    def create_category(self, category_name, description):
        "Create category method"
        new_category = Category (category_name=category_name, description=description)
        try:
            self.db_session.add(new_category)
            self.db_session.commit()
            return new_category
        except Exception as e:
            self.db_session.rollback()
            raise e

    def get_category_by_id(self, catrgory_id):
        "Get category method"
        return self.db_session.query(Category).get(catrgory_id)

    def delete_category(self, category_id):
        """Delete category method"""
        category = self.get_category_by_id(category_id)
        if category:
            self.db_session.delete(category)
            self.db_session.commit()
    def update_category(self, category_id, category_name =None, description=None):
        category_update= self.get_category_by_id(category_id)
        try:
            if not category_update:
                raise Exception(f"Category with ID{category_id} not found")
            if category_name is not None:
                category_update.category_name = category_name
            if description is not None:
                category_update.description = description
            self.db_session.commit()
            return category_update
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise Exception(f"Failse to update category: {e}")