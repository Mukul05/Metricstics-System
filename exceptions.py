# exceptions.py

class DataFileError(Exception):
    """Exception raised for errors in the data file."""
    def __init__(self, message="Data file is invalid or corrupted"):
        self.message = message
        super().__init__(self.message)

class CalculationError(Exception):
    """Exception raised for errors during statistical calculations."""
    def __init__(self, message="Error during statistical calculation"):
        self.message = message
        super().__init__(self.message)

class LoginError(Exception):
    """Exception raised for errors during the login process."""
    def __init__(self, message="Invalid username or password"):
        self.message = message
        super().__init__(self.message)

class SessionError(Exception):
    """Exception raised for errors during session handling."""
    def __init__(self, message="Session handling error"):
        self.message = message
        super().__init__(self.message)
