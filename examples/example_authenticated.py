from backpack_exchange_sdk.authenticated import AuthenticationClient
from enums import RequestEnums

client = AuthenticationClient('public_key', 'secret_key')

# ================================================================
# Account - Account settings.
# ================================================================
# Get account settings
print(client.get_account())

# Update account settings
print(client.update_account(autoBorrowSettlements=True, leverageLimit="5"))

# ================================================================
# Capital - Capital management.
# ================================================================
print(client.get_balances())
print(client.get_deposits())
print(client.get_deposit_address('Solana'))
print(client.get_withdrawals())
print(client.request_withdrawal('xxxxxxxxxx',
      'Solana', '0.1', 'SOL', None, "999999"))

# Get collateral information
print(client.get_collateral())

# ================================================================
# History - Historical account data.
# ================================================================
print(client.get_order_history(symbol='SOL_USDC'))
print(client.get_fill_history(symbol='SOL_USDC'))

# Get borrow history
print(client.get_borrow_history())

# Get interest history
print(client.get_interest_history())

# Get borrow position history
print(client.get_borrow_position_history())

# Get funding payments
print(client.get_funding_payments())

# Get PnL history
print(client.get_pnl_history())

# Get settlement history
print(client.get_settlement_history())

# ================================================================
# Order - Order management.
# ================================================================
print(client.execute_order(RequestEnums.OrderType.LIMIT.value, RequestEnums.Side.ASK.value,
                           "SOL_USDC", True, 200, "0.1"))
print(client.execute_order(RequestEnums.OrderType.LIMIT.value, RequestEnums.Side.BID.value,
                           "SOL_USDC", timeInForce=RequestEnums.TimeInForce.IOC.value))
print(client.get_users_open_orders('SOL_USDC', 9999))
print(client.cancel_open_orders('SOL_USDC'))
print(client.get_open_orders('SOL_USDC'))
print(client.cancel_open_orders('SOL_USDC'))

# Cancel a specific open order
print(client.cancel_open_order('SOL_USDC', orderId='123456'))

# ================================================================
# Borrow Lend - Borrowing and lending.
# ================================================================
print(client.get_borrow_lend_positions())
print(client.execute_borrow_lend(quantity="1.0", side="LEND", symbol="SOL"))

# ================================================================
# Futures - Futures data.
# ================================================================
print(client.get_open_positions())
