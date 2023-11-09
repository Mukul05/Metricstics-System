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
