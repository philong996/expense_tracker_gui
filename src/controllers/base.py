
class BaseController:
    """A base class for controllers to handle common functionality."""
    def __init__(self, db_session):
        self.db_session = db_session