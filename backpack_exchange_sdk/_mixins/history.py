"""
History operations mixin for AuthenticationClient.
"""

from typing import Any, Dict, List, Optional, Union

from backpack_exchange_sdk.enums import FillType, MarketType, SettlementSourceFilter


class HistoryMixin:
    """Mixin providing historical data operations."""

    def get_borrow_history(
        self,
        type: Optional[str] = None,
        sources: Optional[str] = None,
        positionId: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of borrow and lend operations for the account.

        Args:
            type: Filter by event type.
            sources: Filter by sources.
            positionId: Filter by position ID.
            symbol: Filter by asset symbol.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of borrow/lend history records.
        """
        params = {"limit": limit, "offset": offset}
        if type:
            params["type"] = type
        if sources:
            params["sources"] = sources
        if positionId:
            params["positionId"] = positionId
        if symbol:
            params["symbol"] = symbol
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/borrowLend", "borrowHistoryQueryAll", params
        )

    def get_interest_history(
        self,
        asset: Optional[str] = None,
        symbol: Optional[str] = None,
        positionId: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        source: Optional[str] = None,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of interest payments for borrows and lends.

        Args:
            asset: Filter by asset.
            symbol: Filter by asset symbol.
            positionId: Filter by position ID.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            source: Filter by source.
            sortDirection: Sort direction.

        Returns:
            List of interest payment records.
        """
        params = {"limit": limit, "offset": offset}
        if asset:
            params["asset"] = asset
        if symbol:
            params["symbol"] = symbol
        if positionId:
            params["positionId"] = positionId
        if source:
            params["source"] = source
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/interest", "interestHistoryQueryAll", params
        )

    def get_borrow_position_history(
        self,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        state: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of borrow and lend positions for the account.

        Args:
            symbol: Filter by asset symbol.
            side: Filter by side ('Borrow' or 'Lend').
            state: Filter by state ('Open' or 'Closed').
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of position history records.
        """
        params = {"limit": limit, "offset": offset}
        if symbol:
            params["symbol"] = symbol
        if side:
            params["side"] = side
        if state:
            params["state"] = state
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/borrowLend/positions",
            "borrowPositionHistoryQueryAll", params
        )

    def get_fill_history(
        self,
        orderId: Optional[str] = None,
        strategyId: Optional[str] = None,
        fromTimestamp: Optional[int] = None,
        toTimestamp: Optional[int] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        fillType: Optional[Union[FillType, str]] = None,
        marketType: Optional[Union[MarketType, str]] = None,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Retrieves historical fills.

        Args:
            orderId: Filter by order ID.
            strategyId: Filter by strategy ID.
            fromTimestamp: Start timestamp filter.
            toTimestamp: End timestamp filter.
            symbol: Filter by market symbol.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            fillType: Filter by fill type.
            marketType: Filter by market type.
            sortDirection: Sort direction.

        Returns:
            List of fill records.
        """
        params = {"limit": limit, "offset": offset}
        if orderId:
            params["orderId"] = orderId
        if strategyId:
            params["strategyId"] = strategyId
        if fromTimestamp:
            params["from"] = fromTimestamp
        if toTimestamp:
            params["to"] = toTimestamp
        if symbol:
            params["symbol"] = symbol
        if fillType:
            params["fillType"] = fillType.value if isinstance(fillType, FillType) else fillType
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/fills", "fillHistoryQueryAll", params
        )

    def get_funding_payments(
        self,
        subaccountId: Optional[int] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        User's funding payment history for futures.

        Args:
            subaccountId: Filter by subaccount.
            symbol: Filter by market symbol.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of funding payment records.
        """
        params = {"limit": limit, "offset": offset}
        if subaccountId:
            params["subaccountId"] = subaccountId
        if symbol:
            params["symbol"] = symbol
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/funding", "fundingHistoryQueryAll", params
        )

    def get_order_history(
        self,
        orderId: Optional[str] = None,
        strategyId: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        marketType: Optional[Union[MarketType, str]] = None,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Retrieves the order history for the user.

        Args:
            orderId: Filter by order ID.
            strategyId: Filter by strategy ID.
            symbol: Filter by market symbol.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            marketType: Filter by market type.
            sortDirection: Sort direction.

        Returns:
            List of historical orders.
        """
        params = {"limit": limit, "offset": offset}
        if symbol:
            params["symbol"] = symbol
        if orderId:
            params["orderId"] = orderId
        if strategyId:
            params["strategyId"] = strategyId
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/orders", "orderHistoryQueryAll", params
        )

    def get_settlement_history(
        self,
        limit: int = 100,
        offset: int = 0,
        source: Optional[Union[SettlementSourceFilter, str]] = None,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of settlement operations for the account.

        Args:
            limit: Maximum results (default 100).
            offset: Pagination offset.
            source: Filter by settlement source.
            sortDirection: Sort direction.

        Returns:
            List of settlement records.
        """
        params = {"limit": limit, "offset": offset}
        if source:
            params["source"] = (
                source.value if isinstance(source, SettlementSourceFilter) else source
            )
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/settlement", "settlementHistoryQueryAll", params
        )

    def get_dust_history(
        self,
        id: Optional[str] = None,
        symbol: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of dust conversion operations.

        Args:
            id: Filter by dust conversion ID.
            symbol: Filter by market symbol.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of dust conversion records.
        """
        params = {"limit": limit, "offset": offset}
        if id:
            params["id"] = id
        if symbol:
            params["symbol"] = symbol
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/dust", "dustHistoryQueryAll", params
        )

    def get_rfq_history(
        self,
        rfqId: Optional[str] = None,
        symbol: Optional[str] = None,
        status: Optional[str] = None,
        side: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of RFQ (Request For Quote) operations.

        Args:
            rfqId: Filter by RFQ ID.
            symbol: Filter by market symbol.
            status: Filter by RFQ status.
            side: Filter by side.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of RFQ history records.
        """
        params = {"limit": limit, "offset": offset}
        if rfqId:
            params["rfqId"] = rfqId
        if symbol:
            params["symbol"] = symbol
        if status:
            params["status"] = status
        if side:
            params["side"] = side
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/rfq", "rfqHistoryQueryAll", params
        )

    def get_quote_history(
        self,
        quoteId: Optional[str] = None,
        symbol: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of quote operations.

        Args:
            quoteId: Filter by quote ID.
            symbol: Filter by market symbol.
            status: Filter by quote status.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of quote history records.
        """
        params = {"limit": limit, "offset": offset}
        if quoteId:
            params["quoteId"] = quoteId
        if symbol:
            params["symbol"] = symbol
        if status:
            params["status"] = status
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/quote", "quoteHistoryQueryAll", params
        )

    def get_rfq_fill_history(
        self,
        quoteId: Optional[str] = None,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        fillType: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of RFQ fill operations.

        Args:
            quoteId: Filter by quote ID.
            symbol: Filter by market symbol.
            side: Filter by side.
            fillType: Filter by fill type.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of RFQ fill records.
        """
        params = {"limit": limit, "offset": offset}
        if quoteId:
            params["quoteId"] = quoteId
        if symbol:
            params["symbol"] = symbol
        if side:
            params["side"] = side
        if fillType:
            params["fillType"] = fillType
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/rfq/fill", "rfqFillHistoryQueryAll", params
        )

    def get_quote_fill_history(
        self,
        quoteId: Optional[str] = None,
        symbol: Optional[str] = None,
        side: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of quote fill operations.

        Args:
            quoteId: Filter by quote ID.
            symbol: Filter by market symbol.
            side: Filter by side.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of quote fill records.
        """
        params = {"limit": limit, "offset": offset}
        if quoteId:
            params["quoteId"] = quoteId
        if symbol:
            params["symbol"] = symbol
        if side:
            params["side"] = side
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/quote/fill", "quoteFillHistoryQueryAll", params
        )

    def get_strategy_history(
        self,
        strategyId: Optional[str] = None,
        symbol: Optional[str] = None,
        marketType: Optional[Union[MarketType, str]] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of strategy operations.

        Args:
            strategyId: Filter by strategy ID.
            symbol: Filter by market symbol.
            marketType: Filter by market type.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of strategy history records.
        """
        params = {"limit": limit, "offset": offset}
        if strategyId:
            params["strategyId"] = strategyId
        if symbol:
            params["symbol"] = symbol
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/strategies", "strategyHistoryQueryAll", params
        )

    def get_position_history(
        self,
        symbol: Optional[str] = None,
        state: Optional[str] = None,
        marketType: Optional[Union[MarketType, str]] = None,
        limit: int = 100,
        offset: int = 0,
        sortDirection: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        History of positions.

        Args:
            symbol: Filter by market symbol.
            state: Filter by position state.
            marketType: Filter by market type.
            limit: Maximum results (default 100).
            offset: Pagination offset.
            sortDirection: Sort direction.

        Returns:
            List of position history records.
        """
        params = {"limit": limit, "offset": offset}
        if symbol:
            params["symbol"] = symbol
        if state:
            params["state"] = state
        if marketType:
            params["marketType"] = (
                marketType.value if isinstance(marketType, MarketType) else marketType
            )
        if sortDirection:
            params["sortDirection"] = sortDirection
        return self._send_request(
            "GET", "wapi/v1/history/position", "positionHistoryQueryAll", params
        )
