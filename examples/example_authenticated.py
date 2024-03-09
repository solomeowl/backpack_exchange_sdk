from backpack_exchange_sdk.authenticated import AuthenticationClient

client = AuthenticationClient()
client.setup('key', 'secret')

# ================================================================
# Capital - Capital management.
# ================================================================
print(client.get_balances())
print(client.get_deposits())
print(client.get_deposit_address('Solana'))
print(client.get_withdrawals())
print(client.request_withdrawal('xxxxxxxxxx',
      'Solana', '0.1', 'SOL', None, "999999"))

# ================================================================
# History - Historical account data.
# ================================================================
print(client.get_order_history('SOL_USDC'))
print(client.get_fill_history('SOL_USDC'))

# ================================================================
# Order - Order management.
# ================================================================
print(client.execute_order("Limit", "Ask", "SOL_USDC", True, 9999, "200", "0.1"))
print(client.execute_order("Limit", "Ask", "SOL_USDC", True, 9998, "200", "0.1"))
print(client.execute_order("Limit", "Ask", "SOL_USDC", True, 9997, "200", "0.1"))
print(client.get_open_orders('SOL_USDC', 9999))
print(client.cancel_open_orders('SOL_USDC', 9999))
print(client.get_open_orders('SOL_USDC'))
print(client.cancel_open_orders('SOL_USDC'))
