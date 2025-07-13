import sys


class CustomException(Exception):
    """
    A custom exception class that provides detailed error information.

    Attributes:
        error_message (str): The formatted error message including details.
    """
    
    def __init__(self, message: str, error_detail: Exception = None):
        """
        Initialises a new instance of the CustomException.

        Args:
            message (str): A brief description of the error.
            error_detail (Exception): The underlying exception object.

        Raises:
            CustomException: The exception instance with the detailed error message.
        """
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)
        
        
    @staticmethod
    def get_detailed_error_message(message: str, error_detail: Exception) -> str:
        """
        Generates a detailed error message including file name, line number, and the error details.

        Args:
            message (str): The main error message.
            error_detail (Exception): the exception object containing details.

        Returns:
            str: A formatted string containing the detailed error message.
        """
        
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"
    
    
    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Returns:
            str: The formatted error message stored in the `error_message` attribute.
        """
        return self.error_message