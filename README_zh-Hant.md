# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

[English](./README.md) | [简体中文](./README_zh-Hans.md) | **繁體中文** | [日本語](./README_ja.md) | [한국어](./README_ko.md) | [Español](./README_es.md) | [Português](./README_pt.md)

完整的 [Backpack Exchange](https://backpack.exchange/) Python SDK，支援全部 70 個 API 端點，包含 REST 和 WebSocket。

## 功能特色

- **認證客戶端**: 完整存取認證端點（訂單、資金、歷史紀錄、RFQ、策略）
- **公開客戶端**: 存取公開市場資料、系統狀態和交易資料
- **WebSocket 客戶端**: 即時串流市場資料和帳戶更新
- **完整覆蓋**: 實作全部 70 個 API 端點
- **型別提示**: 完整的型別標註，提供更好的 IDE 支援
- **列舉類型**: 完整的列舉類型，確保型別安全的 API 呼叫

## 安裝

```bash
pip install backpack-exchange-sdk
```

或從原始碼安裝：

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## 快速開始

### 公開客戶端

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# 取得所有市場
markets = client.get_markets()

# 取得行情
ticker = client.get_ticker("SOL_USDC")

# 取得訂單簿深度
depth = client.get_depth("SOL_USDC")
```

### 認證客戶端

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# 取得帳戶餘額
balances = client.get_balances()

# 下單
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# 取得訂單歷史
history = client.get_order_history(symbol="SOL_USDC")
```

### 使用列舉

```python
from backpack_exchange_sdk import AuthenticationClient
from backpack_exchange_sdk.enums import OrderType, Side, TimeInForce

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

order = client.execute_order(
    orderType=OrderType.LIMIT.value,
    side=Side.BID.value,
    symbol="SOL_USDC",
    price="100",
    quantity="1",
    timeInForce=TimeInForce.GTC.value
)
```

## API 參考

### 公開客戶端方法

| 類別 | 方法 | 說明 |
|------|------|------|
| **系統** | `get_status()` | 取得系統狀態 |
| | `send_ping()` | Ping 伺服器 |
| | `get_system_time()` | 取得伺服器時間 |
| | `get_wallets()` | 取得支援的錢包 |
| **資產** | `get_assets()` | 取得所有資產 |
| | `get_collateral()` | 取得抵押品資訊 |
| **市場** | `get_markets()` | 取得所有市場 |
| | `get_market(symbol)` | 取得特定市場 |
| | `get_ticker(symbol)` | 取得行情 |
| | `get_tickers()` | 取得所有行情 |
| | `get_depth(symbol)` | 取得訂單簿 |
| | `get_klines(symbol, interval, startTime)` | 取得 K 線 |
| | `get_mark_price(symbol)` | 取得標記價格 |
| | `get_open_interest(symbol)` | 取得未平倉量 |
| | `get_funding_interval_rates(symbol)` | 取得資金費率 |
| **交易** | `get_recent_trades(symbol)` | 取得最近成交 |
| | `get_historical_trades(symbol, limit, offset)` | 取得歷史成交 |
| **借貸** | `get_borrow_lend_markets()` | 取得借貸市場 |
| | `get_borrow_lend_market_history(interval)` | 取得借貸歷史 |
| **預測市場** | `get_prediction_markets()` | 取得預測市場 |
| | `get_prediction_tags()` | 取得預測標籤 |

### 認證客戶端方法

| 類別 | 方法 | 說明 |
|------|------|------|
| **帳戶** | `get_account()` | 取得帳戶設定 |
| | `update_account(...)` | 更新帳戶設定 |
| | `get_max_borrow_quantity(symbol)` | 取得最大借款數量 |
| | `get_max_order_quantity(symbol, side)` | 取得最大下單數量 |
| | `get_max_withdrawal_quantity(symbol)` | 取得最大提款數量 |
| **資金** | `get_balances()` | 取得餘額 |
| | `get_collateral()` | 取得抵押品 |
| | `get_deposits()` | 取得存款歷史 |
| | `get_deposit_address(blockchain)` | 取得存款地址 |
| | `get_withdrawals()` | 取得提款歷史 |
| | `request_withdrawal(...)` | 請求提款 |
| | `convert_dust(symbol)` | 轉換粉塵為 USDC |
| | `get_withdrawal_delay()` | 取得提款延遲設定 |
| | `create_withdrawal_delay(hours, token)` | 建立提款延遲 |
| | `update_withdrawal_delay(hours, token)` | 更新提款延遲 |
| **訂單** | `execute_order(...)` | 下單 |
| | `execute_batch_orders(orders)` | 批量下單 |
| | `get_users_open_orders(symbol)` | 取得用戶未成交訂單 |
| | `get_open_orders(symbol)` | 取得未成交訂單 |
| | `cancel_open_order(symbol, orderId)` | 取消單一訂單 |
| | `cancel_open_orders(symbol)` | 取消所有訂單 |
| **歷史** | `get_order_history(symbol)` | 取得訂單歷史 |
| | `get_fill_history(symbol)` | 取得成交歷史 |
| | `get_borrow_history()` | 取得借款歷史 |
| | `get_interest_history()` | 取得利息歷史 |
| | `get_borrow_position_history()` | 取得借款部位歷史 |
| | `get_funding_payments()` | 取得資金費用 |
| | `get_settlement_history()` | 取得結算歷史 |
| | `get_dust_history()` | 取得粉塵轉換歷史 |
| | `get_position_history()` | 取得部位歷史 |
| | `get_strategy_history()` | 取得策略歷史 |
| | `get_rfq_history()` | 取得 RFQ 歷史 |
| | `get_quote_history()` | 取得報價歷史 |
| | `get_rfq_fill_history()` | 取得 RFQ 成交歷史 |
| | `get_quote_fill_history()` | 取得報價成交歷史 |
| **借貸** | `get_borrow_lend_positions()` | 取得部位 |
| | `execute_borrow_lend(quantity, side, symbol)` | 借款或放貸 |
| | `get_estimated_liquidation_price(borrow)` | 取得預估清算價格 |
| **部位** | `get_open_positions()` | 取得未平倉部位 |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | 提交 RFQ |
| | `submit_quote(rfqId, price)` | 提交報價 |
| | `accept_quote(rfqId, quoteId)` | 接受報價 |
| | `refresh_rfq(rfqId)` | 刷新 RFQ |
| | `cancel_rfq(rfqId)` | 取消 RFQ |
| **策略** | `create_strategy(...)` | 建立策略 |
| | `get_strategy(symbol, strategyId)` | 取得策略 |
| | `get_open_strategies()` | 取得進行中策略 |
| | `cancel_strategy(symbol, strategyId)` | 取消策略 |
| | `cancel_all_strategies(symbol)` | 取消所有策略 |

### WebSocket 客戶端

```python
from backpack_exchange_sdk import WebSocketClient

# 公開串流（不需認證）
ws = WebSocketClient()

# 私有串流（需要認證）
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# 訂閱串流
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# 私有串流範例
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## 可用列舉

```python
from backpack_exchange_sdk.enums import (
    # 訂單相關
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # 市場相關
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # 狀態相關
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # 更多...
)
```

## 範例

請參閱 [examples](./examples) 目錄取得完整使用範例：

- `example_public.py` - 公開 API 範例
- `example_authenticated.py` - 認證 API 範例
- `example_websocket.py` - WebSocket 串流範例

## 文件

詳細 API 文件請參閱 [Backpack Exchange API Docs](https://docs.backpack.exchange/)。

## 更新日誌

### v1.1.0
- 新增 21 個 API 端點（RFQ、策略、預測市場等）
- 新增 25+ 個列舉類型
- 使用 mixin 重構 SDK 架構
- 100% API 覆蓋率（70 個端點）
- 完整型別提示支援

### v1.0.x
- 初始版本，基本 API 支援

## 支持

如果這個 SDK 對你有幫助，請考慮：

1. 使用我的推薦連結註冊：[註冊 Backpack Exchange](https://backpack.exchange/refer/solomeowl)
2. 在 GitHub 給這個專案一顆星

## 授權

MIT License
