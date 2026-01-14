"""
Capital operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, List, Optional


class CapitalMixin:
    """Mixin providing capital-related operations."""

    def get_balances(self) -> Dict[str, Any]:
        """
        Retrieves account balances and their state (locked or available).

        Locked assets are those currently in an open order.

        Returns:
            Dictionary of asset balances.
        """
        return self._send_request("GET", "api/v1/capital", "balanceQuery")

    def get_collateral(self, subAccountId: Optional[int] = None) -> Dict[str, Any]:
        """
        Retrieves collateral information for an account.

        Args:
            subAccountId: Optional subaccount ID.

        Returns:
            Collateral information.
        """
        params = {}
        if subAccountId is not None:
            params["subaccountId"] = subAccountId
        return self._send_request(
            "GET", "api/v1/capital/collateral", "collateralQuery", params
        )

    def get_deposits(
        self,
        fromTimestamp: Optional[int] = None,
        toTimestamp: Optional[int] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Retrieves deposit history.

        Args:
            fromTimestamp: Start timestamp filter.
            toTimestamp: End timestamp filter.
            limit: Maximum number of results (default 100).
            offset: Pagination offset (default 0).

        Returns:
            List of deposit records.
        """
        params = {"limit": limit, "offset": offset}
        if fromTimestamp:
            params["from"] = fromTimestamp
        if toTimestamp:
            params["to"] = toTimestamp
        return self._send_request(
            "GET", "wapi/v1/capital/deposits", "depositQueryAll", params
        )

    def get_deposit_address(self, blockchain_name: str) -> Dict[str, Any]:
        """
        Retrieves the user-specific deposit address for a blockchain.

        Args:
            blockchain_name: The blockchain name (e.g., 'Solana', 'Ethereum').

        Returns:
            Deposit address information.
        """
        params = {"blockchain": blockchain_name}
        return self._send_request(
            "GET", "wapi/v1/capital/deposit/address", "depositAddressQuery", params
        )

    def get_withdrawals(
        self,
        fromTimestamp: Optional[int] = None,
        toTimestamp: Optional[int] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Retrieves withdrawal history.

        Args:
            fromTimestamp: Start timestamp filter.
            toTimestamp: End timestamp filter.
            limit: Maximum number of results (default 100).
            offset: Pagination offset (default 0).

        Returns:
            List of withdrawal records.
        """
        params = {"limit": limit, "offset": offset}
        if fromTimestamp:
            params["from"] = fromTimestamp
        if toTimestamp:
            params["to"] = toTimestamp
        return self._send_request(
            "GET", "wapi/v1/capital/withdrawals", "withdrawalQueryAll", params
        )

    def request_withdrawal(
        self,
        address: str,
        blockchain: str,
        quantity: str,
        symbol: str,
        client_id: Optional[str] = None,
        two_factor_token: Optional[str] = None,
        auto_borrow: Optional[bool] = None,
        auto_lend_redeem: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Requests a withdrawal from the exchange.

        Args:
            address: Destination address.
            blockchain: Blockchain to withdraw on.
            quantity: Amount to withdraw.
            symbol: Asset symbol.
            client_id: Optional client-provided ID.
            two_factor_token: 2FA token (required if address not in whitelist).
            auto_borrow: Whether to use auto borrow.
            auto_lend_redeem: Whether to use auto lend redeem.

        Returns:
            Withdrawal information.
        """
        data = {
            "address": address,
            "blockchain": blockchain,
            "quantity": quantity,
            "symbol": symbol,
        }
        if client_id:
            data["clientId"] = client_id
        if two_factor_token:
            data["twoFactorToken"] = two_factor_token
        if auto_borrow is not None:
            data["autoBorrow"] = auto_borrow
        if auto_lend_redeem is not None:
            data["autoLendRedeem"] = auto_lend_redeem

        return self._send_request(
            "POST", "wapi/v1/capital/withdrawals", "withdraw", data
        )

    def convert_dust(self, symbol: str) -> Dict[str, Any]:
        """
        Converts a dust balance to USDC.

        The balance (including lend) must be less than the minimum
        quantity tradable on the spot order book.

        Args:
            symbol: The asset symbol to convert.

        Returns:
            Dust conversion result.
        """
        data = {"symbol": symbol}
        return self._send_request(
            "POST", "api/v1/account/convertDust", "convertDust", data
        )

    def get_withdrawal_delay(self) -> Dict[str, Any]:
        """
        Get withdrawal delay configuration.

        Returns:
            Withdrawal delay settings.
        """
        return self._send_request(
            "GET", "wapi/v1/capital/withdrawals/delay", "withdrawalDelayQuery"
        )

    def create_withdrawal_delay(
        self,
        withdrawalDelayHours: int,
        twoFactorToken: str
    ) -> Dict[str, Any]:
        """
        Enable withdrawal delay for non-whitelisted addresses.

        This security feature adds a time delay before withdrawals are
        processed, allowing time to cancel unauthorized withdrawals.

        Args:
            withdrawalDelayHours: Delay in hours before withdrawals are processed.
            twoFactorToken: 2FA verification token.

        Returns:
            Created withdrawal delay configuration.
        """
        data = {
            "withdrawalDelayHours": withdrawalDelayHours,
            "twoFactorToken": twoFactorToken
        }
        return self._send_request(
            "POST", "wapi/v1/capital/withdrawals/delay", "withdrawalDelayCreate", data
        )

    def update_withdrawal_delay(
        self,
        withdrawalDelayHours: int,
        twoFactorToken: str
    ) -> Dict[str, Any]:
        """
        Update withdrawal delay for non-whitelisted addresses.

        Changes will take effect after the current delay period ends.

        Args:
            withdrawalDelayHours: New delay in hours before withdrawals are processed.
            twoFactorToken: 2FA verification token.

        Returns:
            Updated withdrawal delay configuration.
        """
        data = {
            "withdrawalDelayHours": withdrawalDelayHours,
            "twoFactorToken": twoFactorToken
        }
        return self._send_request(
            "PATCH", "wapi/v1/capital/withdrawals/delay", "withdrawalDelayUpdate", data
        )
