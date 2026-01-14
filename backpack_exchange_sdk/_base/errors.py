"""
Custom exceptions for Backpack Exchange SDK.
"""

from typing import Optional


class BackpackAPIError(Exception):
    """
    Exception raised when the Backpack API returns an error response.

    Attributes:
        code: The error code returned by the API
        message: The error message returned by the API
        status_code: The HTTP status code of the response
    """

    def __init__(
        self,
        code: Optional[str] = None,
        message: Optional[str] = None,
        status_code: Optional[int] = None
    ):
        self.code = code
        self.message = message
        self.status_code = status_code

        error_parts = []
        if code:
            error_parts.append(code)
        if message:
            error_parts.append(message)

        error_str = " - ".join(error_parts) if error_parts else "Unknown API error"
        super().__init__(f"API Error: {error_str}")


class BackpackRequestError(Exception):
    """
    Exception raised when a request to the Backpack API fails.

    This includes network errors, timeouts, and other request-level failures.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Request failed: {message}")
