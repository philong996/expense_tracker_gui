class AppState:
    """Singleton application state."""
    _instance = None

    @staticmethod
    def get_instance():
        "Get the current instance"
        if AppState._instance is None:
            AppState._instance = AppState()
        return AppState._instance

    def __init__(self):
        if AppState._instance is not None:
            raise Exception("This is a singleton class!")
        self.current_user = None  # Shared variable