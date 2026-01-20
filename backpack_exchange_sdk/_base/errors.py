"""
Custom exceptions for Backpack Exchange SDK.
"""

from typing import Optional, Type, Dict


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


class BackpackUnauthorizedError(BackpackAPIError):
    """Unauthorized error from API."""


class BackpackForbiddenError(BackpackAPIError):
    """Forbidden error from API."""


class BackpackRateLimitError(BackpackAPIError):
    """Rate limit error from API."""


class BackpackNotFoundError(BackpackAPIError):
    """Resource not found error from API."""


class BackpackInvalidRequestError(BackpackAPIError):
    """Invalid request error from API."""


class BackpackInsufficientFundsError(BackpackAPIError):
    """Insufficient funds error from API."""


class BackpackMaintenanceError(BackpackAPIError):
    """Maintenance error from API."""


class BackpackTradingPausedError(BackpackAPIError):
    """Trading paused error from API."""


_ERROR_CODE_CLASS_MAP: Dict[str, Type[BackpackAPIError]] = {
    "UNAUTHORIZED": BackpackUnauthorizedError,
    "FORBIDDEN": BackpackForbiddenError,
    "TOO_MANY_REQUESTS": BackpackRateLimitError,
    "RESOURCE_NOT_FOUND": BackpackNotFoundError,
    "INVALID_CLIENT_REQUEST": BackpackInvalidRequestError,
    "INVALID_ORDER": BackpackInvalidRequestError,
    "INVALID_MARKET": BackpackInvalidRequestError,
    "INVALID_SYMBOL": BackpackInvalidRequestError,
    "INVALID_PRICE": BackpackInvalidRequestError,
    "INVALID_QUANTITY": BackpackInvalidRequestError,
    "INSUFFICIENT_FUNDS": BackpackInsufficientFundsError,
    "MAINTENANCE": BackpackMaintenanceError,
    "TRADING_PAUSED": BackpackTradingPausedError,
}


def get_error_class(code: Optional[str]) -> Type[BackpackAPIError]:
    """Return the mapped error class for a given API error code."""
    if not code:
        return BackpackAPIError
    return _ERROR_CODE_CLASS_MAP.get(code, BackpackAPIError)
