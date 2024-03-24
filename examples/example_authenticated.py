from backpack_exchange_sdk.authenticated import AuthenticationClient
from enums import RequestEnums
client = AuthenticationClient('public_key', 'secret_key')


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
print(client.execute_order(RequestEnums.OrderType.LIMIT.value, RequestEnums.Side.ASK.value,
                           "SOL_USDC", True, 200, "0.1"))
print(client.execute_order(RequestEnums.OrderType.LIMIT.value, RequestEnums.Side.BID.value,
                           "SOL_USDC", timeInForce=RequestEnums.TimeInForce.IOC.value))
print(client.get_users_open_orders('SOL_USDC', 9999))
print(client.cancel_open_orders('SOL_USDC'))
print(client.get_open_orders('SOL_USDC'))
print(client.cancel_open_orders('SOL_USDC'))
