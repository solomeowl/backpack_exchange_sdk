import base64
import json
import time
import requests
from cryptography.hazmat.primitives.asymmetric import ed25519


class AuthenticationClient:
    base_url = 'https://api.backpack.exchange/'
    private_key_obj: ed25519.Ed25519PrivateKey

    def __init__(self):
        self.is_debug_mode = False
        self.network_proxies = {'http': '', 'https': ''}
        self.key = ''
        self.secret = ''

    def setup(self, key, secret):
        self.key = key
        self.secret = secret
        self.private_key_obj = ed25519.Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(secret)
        )

    def get_balances(self):
        return self._send_request('GET', 'api/v1/capital', 'balanceQuery', {})

    def get_deposits(self):
        return self._send_request('GET', 'wapi/v1/capital/deposits', 'depositQueryAll', {})

    def get_deposit_address(self, blockchain_name: str):
        params = {'blockchain': blockchain_name}
        return self._send_request('GET', 'wapi/v1/capital/deposit/address', 'depositAddressQuery', params)

    def get_withdrawals(self, num: int, start: int):
        params = {'limit': num, 'offset': start}
        return self._send_request('GET', 'wapi/v1/capital/withdrawals', 'withdrawalQueryAll', params)

    def make_withdrawal(self, wallet_address: str, asset_symbol: str, chain_name: str, amount: str):
        data = {
            'address': wallet_address,
            'blockchain': chain_name,
            'quantity': amount,
            'symbol': asset_symbol,
        }
        return self._send_request('POST', 'wapi/v1/capital/withdrawals', 'withdraw', data)

    def _send_request(self, method, endpoint, action, params):
        url = f'{self.base_url}{endpoint}'
        ts = int(time.time() * 1e3)
        headers = self._generate_signature(action, ts, params)
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params, proxies=self.network_proxies)
        else:
            response = requests.post(url, headers=headers, data=json.dumps(params), proxies=self.network_proxies)
        return response.json()

    def _generate_signature(self, action: str, timestamp: int, params=None):
        if params is None:
            params = {}
        if 'postOnly' in params:
            params = params.copy()
            params['postOnly'] = str(params['postOnly']).lower()
        param_str = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        sign_str = f"instruction={action}&{param_str}&timestamp={timestamp}&window={self.window}"
        signature = base64.b64encode(self.private_key_obj.sign(sign_str.encode())).decode()
        return {
            "X-API-Key": self.key,
            "X-Signature": signature,
            "X-Timestamp": str(timestamp),
            "Content-Type": "application/json; charset=utf-8",
        }
