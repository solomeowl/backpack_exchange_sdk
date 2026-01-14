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
        clientRfqId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Submit an RFQ (Request For Quote).

        Either quantity or quoteQuantity must be specified, but not both.

        Args:
            symbol: Market symbol (e.g., 'SOL_USDC_RFQ').
            side: RFQ side ('Bid' or 'Ask').
            quantity: Quantity in base asset.
            quoteQuantity: Quantity in quote asset.
            clientRfqId: Optional client-provided RFQ ID.

        Returns:
            RFQ details including rfqId, status, etc.
        """
        data = {"symbol": symbol, "side": side}
        if quantity:
            data["quantity"] = quantity
        if quoteQuantity:
            data["quoteQuantity"] = quoteQuantity
        if clientRfqId:
            data["clientRfqId"] = clientRfqId
        return self._send_request("POST", "api/v1/rfq", "rfqSubmit", data)

    def submit_quote(
        self,
        rfqId: str,
        price: str,
        clientQuoteId: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Submit a quote in response to an RFQ.

        This is used by market makers to provide quotes.

        Args:
            rfqId: The RFQ ID to quote on.
            price: Quote price.
            clientQuoteId: Optional client-provided quote ID.

        Returns:
            Quote details including quoteId, status, etc.
        """
        data = {"rfqId": rfqId, "price": price}
        if clientQuoteId:
            data["clientQuoteId"] = clientQuoteId
        return self._send_request("POST", "api/v1/rfq/quote", "quoteSubmit", data)

    def accept_quote(self, rfqId: str, quoteId: str) -> Dict[str, Any]:
        """
        Accept a quote from a market maker.

        Args:
            rfqId: The RFQ ID.
            quoteId: The quote ID to accept.

        Returns:
            Accepted quote information.
        """
        data = {"rfqId": rfqId, "quoteId": quoteId}
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

    def cancel_rfq(self, rfqId: str) -> Dict[str, Any]:
        """
        Cancel an open RFQ.

        Args:
            rfqId: The RFQ ID to cancel.

        Returns:
            Cancelled RFQ information.
        """
        data = {"rfqId": rfqId}
        return self._send_request("POST", "api/v1/rfq/cancel", "rfqCancel", data)
