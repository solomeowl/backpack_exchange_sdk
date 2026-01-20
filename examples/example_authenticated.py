from backpack_exchange_sdk.authenticated import AuthenticationClient
from backpack_exchange_sdk.enums import (
    OrderType,
    Side,
    TimeInForce,
    SelfTradePrevention,
)

client = AuthenticationClient("api_key", "secret_key")

# ================================================================
# Account - Account settings.
# ================================================================
# Get account settings
print(client.get_account())

# Update account settings
print(client.update_account(autoBorrowSettlements=False, leverageLimit="5"))

# Get maximum borrow quantity
print(client.get_max_borrow_quantity("USDC"))

# Get maximum order quantity
print(client.get_max_order_quantity("SOL_USDC", "Bid", price="100"))

# Get maximum withdrawal quantity
print(client.get_max_withdrawal_quantity("USDC"))

# ================================================================
# Capital - Capital management.
# ================================================================
print(client.get_balances())
print(client.get_deposits())
print(client.get_deposit_address("Solana"))
print(client.get_withdrawals())
print(client.request_withdrawal("xxxxxxxxxx", "Solana", "0.1", "SOL", None, "999999"))

# Get collateral information
print(client.get_collateral())

# Convert dust balance to USDC
print(client.convert_dust("BONK"))

# Get withdrawal delay settings
print(client.get_withdrawal_delay())

# Create withdrawal delay (requires 2FA)
print(client.create_withdrawal_delay(withdrawalDelayHours=24, twoFactorToken="123456"))

# Update withdrawal delay (requires 2FA)
print(client.update_withdrawal_delay(withdrawalDelayHours=48, twoFactorToken="123456"))

# ================================================================
# History - Historical account data.
# ================================================================
print(client.get_order_history(symbol="SOL_USDC"))
print(client.get_fill_history(symbol="SOL_USDC"))

# Get borrow history
print(client.get_borrow_history())

# Get interest history
print(client.get_interest_history())

# Get borrow position history
print(client.get_borrow_position_history())

# Get funding payments
print(client.get_funding_payments())

# Get settlement history
print(client.get_settlement_history())

# Get dust conversion history
print(client.get_dust_history())

# Get position history
print(client.get_position_history())

# Get strategy history
print(client.get_strategy_history())

# Get RFQ history
print(client.get_rfq_history())

# Get quote history
print(client.get_quote_history())

# Get RFQ fill history
print(client.get_rfq_fill_history())

# Get quote fill history
print(client.get_quote_fill_history())

# ================================================================
# Order - Order management.
# ================================================================
# Execute a single order
print(
    client.execute_order(
        OrderType.LIMIT,
        Side.ASK,
        "SOL_USDC",
        postOnly=True,
        clientId=12345,
        price="200",
        quantity="0.1",
        timeInForce=TimeInForce.GTC,
        selfTradePrevention=SelfTradePrevention.REJECT_TAKER,
    )
)

# Execute batch orders
print(
    client.execute_batch_orders([
        {
            "orderType": OrderType.LIMIT.value,
            "side": Side.BID.value,
            "symbol": "SOL_USDC",
            "price": "100",
            "quantity": "0.1",
            "timeInForce": TimeInForce.GTC.value,
        },
        {
            "orderType": OrderType.LIMIT.value,
            "side": Side.BID.value,
            "symbol": "SOL_USDC",
            "price": "99",
            "quantity": "0.2",
            "timeInForce": TimeInForce.GTC.value,
        },
    ])
)

print(client.get_users_open_orders("SOL_USDC", clientId=9999))
print(client.get_open_orders("SOL_USDC"))
print(client.cancel_open_orders("SOL_USDC"))

# Cancel a specific open order
print(client.cancel_open_order("SOL_USDC", orderId="123456"))

# ================================================================
# Borrow Lend - Borrowing and lending.
# ================================================================
print(client.get_borrow_lend_positions())
print(client.execute_borrow_lend(quantity="1.0", side="Lend", symbol="SOL"))

# Get estimated liquidation price
print(client.get_estimated_liquidation_price(borrow="base64_encoded_payload"))

# ================================================================
# Futures / Positions
# ================================================================
print(client.get_open_positions())

# ================================================================
# RFQ - Request For Quote (for large trades).
# ================================================================
# Submit an RFQ
print(client.submit_rfq(symbol="SOL_USDC_RFQ", side="Bid", quantity="1000"))

# Submit a quote in response to an RFQ (for market makers)
print(client.submit_quote(rfqId="rfq_123", bidPrice="100.4", askPrice="100.6"))

# Accept a quote
print(client.accept_quote(quoteId="quote_456", rfqId="rfq_123"))

# Refresh an RFQ to extend its time window
print(client.refresh_rfq(rfqId="rfq_123"))

# Cancel an RFQ
print(client.cancel_rfq(rfqId="rfq_123"))

# ================================================================
# Strategy - Algorithmic trading strategies.
# ================================================================
# Create a scheduled strategy (TWAP-like)
print(
    client.create_strategy(
        symbol="SOL_USDC",
        side="Bid",
        strategyType="Scheduled",
        quantity="100",
        interval="1m",
        duration="10m",
    )
)

# Get a specific strategy
print(client.get_strategy(symbol="SOL_USDC", strategyId="strategy_123"))

# Get all open strategies
print(client.get_open_strategies())

# Cancel a specific strategy
print(client.cancel_strategy(symbol="SOL_USDC", strategyId="strategy_123"))

# Cancel all strategies for a market
print(client.cancel_all_strategies(symbol="SOL_USDC"))
