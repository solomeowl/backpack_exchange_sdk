# Backpack Exchange SDK
![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)


The Backpack Exchange SDK provides a convenient interface for interacting with the Backpack Exchange API. It includes two main clients: `AuthenticationClient` for authenticated endpoints and `PublicClient` for public endpoints.

## Features

- **Authentication Client**: Interact with authenticated endpoints for managing capital, historical data, and orders.
- **Public Client**: Access public market data, system status, and public trade data.

## Installation

The SDK can be installed directly using pip:

```bash
pip3 install backpack_exchange_sdk
```

Alternatively, you can clone the repository and install the SDK manually:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip3 install .
```

## Usage
### Authentication Client
```python
from backpack_exchange_sdk.authenticated import AuthenticationClient

client = AuthenticationClient('<YOUR_API_KEY>', '<YOUR_SECRET>')

# Get account balances
balances = client.get_balances()
print(balances)

# Request a withdrawal
response = client.request_withdrawal('xxxxaddress', 'Solana', '0,1', 'Sol')
print(response)

```
### Public Client
```python
from backpack_exchange_sdk.public import PublicClient

public_client = PublicClient()

# Get all supported assets
assets = public_client.get_assets()
print(assets)

# Get ticker information for a specific symbol
ticker = public_client.get_ticker('SOL_USDC')
print(ticker)

```

## Documentation
For more detailed information about the API endpoints and their usage, refer to the [Backpack Exchange API documentation](https://docs.backpack.exchange/).

## Support 

If this SDK has been helpful to you 🌟 and you haven't signed up for Backpack Exchange yet, please consider using the following referral link to register: [Register on Backpack Exchange](https://backpack.exchange/refer/solomeowl) 🚀.

Using this referral link is a great way to support this project ❤️, as it helps to grow the community and ensures the continued development of the SDK. 🛠️
