"""
Base client classes for Backpack Exchange SDK.
"""

import json
import time
from typing import Any, Dict, List, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from cryptography.hazmat.primitives.asymmetric import ed25519

from backpack_exchange_sdk._base.errors import (
    BackpackAPIError,
    BackpackRequestError,
    get_error_class,
)
from backpack_exchange_sdk._base.utils import (
    generate_auth_headers,
    generate_batch_auth_headers,
    load_private_key,
)


class BaseClient:
    """
    Base client with common HTTP functionality.

    Provides session management, error handling, and response parsing.
    """

    DEFAULT_BASE_URL = "https://api.backpack.exchange/"

    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: int = 0,
        backoff_factor: float = 0.1,
        status_forcelist: Optional[List[int]] = None,
    ):
        """
        Initialize the base client.

        Args:
            base_url: Optional custom base URL for the API
            timeout: Optional request timeout in seconds
            max_retries: Number of retries for transient errors (default 0)
            backoff_factor: Backoff factor between retries
            status_forcelist: HTTP status codes that trigger retries
        """
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.timeout = timeout
        self.session = requests.Session()

        if max_retries > 0:
            retry = Retry(
                total=max_retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist or [429, 500, 502, 503, 504],
                allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
                raise_on_status=False,
            )
            adapter = HTTPAdapter(max_retries=retry)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)

    def _handle_response(self, response: requests.Response) -> Any:
        """
        Handle API response and parse JSON.

        Args:
            response: The requests Response object

        Returns:
            Parsed JSON response or None for 204 responses

        Raises:
            BackpackAPIError: If the API returns an error response
        """
        if 200 <= response.status_code < 300:
            if response.status_code == 204:
                return None
            try:
                return response.json()
            except ValueError:
                return response.text
        else:
            try:
                error = response.json()
                error_code = error.get("code")
                error_class = get_error_class(error_code)
                raise error_class(
                    code=error_code,
                    message=error.get("message"),
                    status_code=response.status_code,
                )
            except ValueError:
                raise BackpackAPIError(
                    message=response.text,
                    status_code=response.status_code
                )

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        """
        Make a GET request.

        Args:
            endpoint: API endpoint (relative to base URL)
            params: Optional query parameters

        Returns:
            Parsed API response

        Raises:
            BackpackAPIError: If the API returns an error
            BackpackRequestError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            raise BackpackRequestError(str(e))


class AuthenticatedBaseClient(BaseClient):
    """
    Base client with authentication support.

    Provides ED25519 signature generation and authenticated request methods.
    """

    def __init__(
        self,
        public_key: str,
        secret_key: str,
        window: int = 5000,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
        max_retries: int = 0,
        backoff_factor: float = 0.1,
        status_forcelist: Optional[List[int]] = None,
    ):
        """
        Initialize the authenticated client.

        Args:
            public_key: Base64-encoded public key (API key)
            secret_key: Base64-encoded private key (secret)
            window: Request validity window in milliseconds (default 5000)
            base_url: Optional custom base URL for the API
            timeout: Optional request timeout in seconds
            max_retries: Number of retries for transient errors (default 0)
            backoff_factor: Backoff factor between retries
            status_forcelist: HTTP status codes that trigger retries
        """
        super().__init__(
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        self.key = public_key
        self.private_key_obj = load_private_key(secret_key)
        self.window = window

    def _generate_signature(
        self,
        action: str,
        timestamp: int,
        params: Optional[Dict] = None
    ) -> Dict[str, str]:
        """
        Generate authentication headers for a request.

        This method is kept for backward compatibility with existing code.

        Args:
            action: The API instruction (e.g., 'orderExecute')
            timestamp: Unix timestamp in milliseconds
            params: Optional request parameters

        Returns:
            Dictionary of authentication headers
        """
        return generate_auth_headers(
            self.key,
            self.private_key_obj,
            action,
            timestamp,
            self.window,
            params
        )

    def _send_request(
        self,
        method: str,
        endpoint: str,
        action: str,
        params: Optional[Dict] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Send an authenticated request to the API.

        Args:
            method: HTTP method (GET, POST, DELETE, PATCH, PUT)
            endpoint: API endpoint (relative to base URL)
            action: The API instruction for signing
            params: Optional request parameters
            extra_headers: Optional extra headers to include

        Returns:
            Parsed API response

        Raises:
            BackpackAPIError: If the API returns an error
            BackpackRequestError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        ts = int(time.time() * 1e3)
        headers = self._generate_signature(action, ts, params)
        if extra_headers:
            headers.update(extra_headers)

        try:
            if method == "GET":
                response = self.session.get(
                    url, headers=headers, params=params, timeout=self.timeout
                )
            elif method == "DELETE":
                response = self.session.delete(
                    url,
                    headers=headers,
                    data=json.dumps(params) if params else None,
                    timeout=self.timeout,
                )
            elif method == "PATCH":
                response = self.session.patch(
                    url,
                    headers=headers,
                    data=json.dumps(params) if params else None,
                    timeout=self.timeout,
                )
            elif method == "PUT":
                response = self.session.put(
                    url,
                    headers=headers,
                    data=json.dumps(params) if params else None,
                    timeout=self.timeout,
                )
            else:  # POST
                response = self.session.post(
                    url,
                    headers=headers,
                    data=json.dumps(params) if params else None,
                    timeout=self.timeout,
                )

            return self._handle_response(response)

        except requests.exceptions.RequestException as e:
            raise BackpackRequestError(str(e))

    def _send_batch_request(
        self,
        endpoint: str,
        orders: List[Dict[str, Any]],
        extra_headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        """
        Send a batch order request with special signature handling.

        Args:
            endpoint: API endpoint (relative to base URL)
            orders: List of order parameter dictionaries
            extra_headers: Optional extra headers to include

        Returns:
            Parsed API response

        Raises:
            BackpackAPIError: If the API returns an error
            BackpackRequestError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        ts = int(time.time() * 1e3)
        headers = generate_batch_auth_headers(
            self.key,
            self.private_key_obj,
            orders,
            ts,
            self.window
        )
        if extra_headers:
            headers.update(extra_headers)

        try:
            response = self.session.post(
                url, headers=headers, data=json.dumps(orders), timeout=self.timeout
            )
            return self._handle_response(response)
        except requests.exceptions.RequestException as e:
            raise BackpackRequestError(str(e))
