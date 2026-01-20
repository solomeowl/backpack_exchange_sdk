"""
RFQ (Request For Quote) operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, Optional


class RFQMixin:
    """Mixin providing RFQ (Request For Quote) operations."""

    def submit_rfq(
        self,
        symbol: str,
        side: str,
        quantity: Optional[str] = None,
        quoteQuantity: Optional[str] = None,
        price: Optional[str] = None,
        executionMode: Optional[str] = None,
        clientId: Optional[str] = None,
        autoBorrow: Optional[bool] = None,
        autoBorrowRepay: Optional[bool] = None,
        autoLend: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Submit an RFQ (Request For Quote).

        Either quantity or quoteQuantity must be specified, but not both.

        Args:
            symbol: Market symbol (e.g., 'SOL_USDC_RFQ').
            side: RFQ side ('Bid' or 'Ask').
            quantity: Quantity in base asset.
            quoteQuantity: Quantity in quote asset.
            price: Optional RFQ price.
            executionMode: Optional execution mode.
            clientId: Optional client-provided RFQ ID.
            autoBorrow: Enable auto borrow.
            autoBorrowRepay: Enable auto borrow repay.
            autoLend: Enable auto lend.
            autoLendRedeem: Enable auto lend redeem.

        Returns:
            RFQ details including rfqId, status, etc.
        """
        data = {"symbol": symbol, "side": side}
        if quantity:
            data["quantity"] = quantity
        if quoteQuantity:
            data["quoteQuantity"] = quoteQuantity
        if price:
            data["price"] = price
        if executionMode:
            data["executionMode"] = executionMode
        if clientId:
            data["clientId"] = clientId
        if autoBorrow is not None:
            data["autoBorrow"] = autoBorrow
        if autoBorrowRepay is not None:
            data["autoBorrowRepay"] = autoBorrowRepay
        if autoLend is not None:
            data["autoLend"] = autoLend
        if autoLendRedeem is not None:
            data["autoLendRedeem"] = autoLendRedeem
        return self._send_request("POST", "api/v1/rfq", "rfqSubmit", data)

    def submit_quote(
        self,
        rfqId: str,
        bidPrice: str,
        askPrice: str,
        clientId: Optional[str] = None,
        autoBorrow: Optional[bool] = None,
        autoBorrowRepay: Optional[bool] = None,
        autoLend: Optional[bool] = None,
        autoLendRedeem: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Submit a quote in response to an RFQ.

        This is used by market makers to provide quotes.

        Args:
            rfqId: The RFQ ID to quote on.
            bidPrice: Bid price.
            askPrice: Ask price.
            clientId: Optional client-provided quote ID.
            autoBorrow: Enable auto borrow.
            autoBorrowRepay: Enable auto borrow repay.
            autoLend: Enable auto lend.
            autoLendRedeem: Enable auto lend redeem.

        Returns:
            Quote details including quoteId, status, etc.
        """
        data = {"rfqId": rfqId, "bidPrice": bidPrice, "askPrice": askPrice}
        if clientId:
            data["clientId"] = clientId
        if autoBorrow is not None:
            data["autoBorrow"] = autoBorrow
        if autoBorrowRepay is not None:
            data["autoBorrowRepay"] = autoBorrowRepay
        if autoLend is not None:
            data["autoLend"] = autoLend
        if autoLendRedeem is not None:
            data["autoLendRedeem"] = autoLendRedeem
        return self._send_request("POST", "api/v1/rfq/quote", "quoteSubmit", data)

    def accept_quote(
        self,
        quoteId: str,
        rfqId: Optional[str] = None,
        clientId: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Accept a quote from a market maker.

        Args:
            quoteId: The quote ID to accept.
            rfqId: Optional RFQ ID.
            clientId: Optional client-provided RFQ ID.

        Returns:
            Accepted quote information.
        """
        data = {"quoteId": quoteId}
        if rfqId:
            data["rfqId"] = rfqId
        if clientId:
            data["clientId"] = clientId
        return self._send_request("POST", "api/v1/rfq/accept", "quoteAccept", data)

    def refresh_rfq(self, rfqId: str) -> Dict[str, Any]:
        """
        Refresh an RFQ, extending its time window.

        Args:
            rfqId: The RFQ ID to refresh.

        Returns:
            Refreshed RFQ information.
        """
        data = {"rfqId": rfqId}
        return self._send_request("POST", "api/v1/rfq/refresh", "rfqRefresh", data)

    def cancel_rfq(
        self,
        rfqId: Optional[str] = None,
        clientId: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cancel an open RFQ.

        Args:
            rfqId: Optional RFQ ID to cancel.
            clientId: Optional client-provided RFQ ID.

        Returns:
            Cancelled RFQ information.
        """
        data = {}
        if rfqId:
            data["rfqId"] = rfqId
        if clientId:
            data["clientId"] = clientId
        return self._send_request("POST", "api/v1/rfq/cancel", "rfqCancel", data)
