# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

[English](./README.md) | **简体中文** | [繁體中文](./README_zh-Hant.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md) | [Español](./README_es.md) | [Português](./README_pt.md)

完整的 [Backpack Exchange](https://backpack.exchange/) Python SDK，支持全部 70 个 API 端点，包含 REST 和 WebSocket。

## 功能特性

- **认证客户端**: 完整访问认证端点（订单、资金、历史记录、RFQ、策略）
- **公开客户端**: 访问公开市场数据、系统状态和交易数据
- **WebSocket 客户端**: 实时流式市场数据和账户更新
- **完整覆盖**: 实现全部 70 个 API 端点
- **类型提示**: 完整的类型标注，提供更好的 IDE 支持
- **枚举类型**: 完整的枚举类型，确保类型安全的 API 调用

## 安装

```bash
pip install backpack-exchange-sdk
```

或从源码安装：

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## 快速开始

### 公开客户端

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# 获取所有市场
markets = client.get_markets()

# 获取行情
ticker = client.get_ticker("SOL_USDC")

# 获取订单簿深度
depth = client.get_depth("SOL_USDC")
```

### 认证客户端

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# 获取账户余额
balances = client.get_balances()

# 下单
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# 获取订单历史
history = client.get_order_history(symbol="SOL_USDC")
```

### 使用枚举

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

## API 参考

### 公开客户端方法

| 类别 | 方法 | 说明 |
|------|------|------|
| **系统** | `get_status()` | 获取系统状态 |
| | `send_ping()` | Ping 服务器 |
| | `get_system_time()` | 获取服务器时间 |
| | `get_wallets()` | 获取支持的钱包 |
| **资产** | `get_assets()` | 获取所有资产 |
| | `get_collateral()` | 获取抵押品信息 |
| **市场** | `get_markets()` | 获取所有市场 |
| | `get_market(symbol)` | 获取特定市场 |
| | `get_ticker(symbol)` | 获取行情 |
| | `get_tickers()` | 获取所有行情 |
| | `get_depth(symbol)` | 获取订单簿 |
| | `get_klines(symbol, interval, startTime)` | 获取 K 线 |
| | `get_mark_price(symbol)` | 获取标记价格 |
| | `get_open_interest(symbol)` | 获取未平仓量 |
| | `get_funding_interval_rates(symbol)` | 获取资金费率 |
| **交易** | `get_recent_trades(symbol)` | 获取最近成交 |
| | `get_historical_trades(symbol, limit, offset)` | 获取历史成交 |
| **借贷** | `get_borrow_lend_markets()` | 获取借贷市场 |
| | `get_borrow_lend_market_history(interval)` | 获取借贷历史 |
| **预测市场** | `get_prediction_markets()` | 获取预测市场 |
| | `get_prediction_tags()` | 获取预测标签 |

### 认证客户端方法

| 类别 | 方法 | 说明 |
|------|------|------|
| **账户** | `get_account()` | 获取账户设置 |
| | `update_account(...)` | 更新账户设置 |
| | `get_max_borrow_quantity(symbol)` | 获取最大借款数量 |
| | `get_max_order_quantity(symbol, side)` | 获取最大下单数量 |
| | `get_max_withdrawal_quantity(symbol)` | 获取最大提款数量 |
| **资金** | `get_balances()` | 获取余额 |
| | `get_collateral()` | 获取抵押品 |
| | `get_deposits()` | 获取存款历史 |
| | `get_deposit_address(blockchain)` | 获取存款地址 |
| | `get_withdrawals()` | 获取提款历史 |
| | `request_withdrawal(...)` | 请求提款 |
| | `convert_dust(symbol)` | 转换粉尘为 USDC |
| | `get_withdrawal_delay()` | 获取提款延迟设置 |
| | `create_withdrawal_delay(hours, token)` | 创建提款延迟 |
| | `update_withdrawal_delay(hours, token)` | 更新提款延迟 |
| **订单** | `execute_order(...)` | 下单 |
| | `execute_batch_orders(orders)` | 批量下单 |
| | `get_users_open_orders(symbol)` | 获取用户未成交订单 |
| | `get_open_orders(symbol)` | 获取未成交订单 |
| | `cancel_open_order(symbol, orderId)` | 取消单个订单 |
| | `cancel_open_orders(symbol)` | 取消所有订单 |
| **历史** | `get_order_history(symbol)` | 获取订单历史 |
| | `get_fill_history(symbol)` | 获取成交历史 |
| | `get_borrow_history()` | 获取借款历史 |
| | `get_interest_history()` | 获取利息历史 |
| | `get_borrow_position_history()` | 获取借款仓位历史 |
| | `get_funding_payments()` | 获取资金费用 |
| | `get_settlement_history()` | 获取结算历史 |
| | `get_dust_history()` | 获取粉尘转换历史 |
| | `get_position_history()` | 获取仓位历史 |
| | `get_strategy_history()` | 获取策略历史 |
| | `get_rfq_history()` | 获取 RFQ 历史 |
| | `get_quote_history()` | 获取报价历史 |
| | `get_rfq_fill_history()` | 获取 RFQ 成交历史 |
| | `get_quote_fill_history()` | 获取报价成交历史 |
| **借贷** | `get_borrow_lend_positions()` | 获取仓位 |
| | `execute_borrow_lend(quantity, side, symbol)` | 借款或放贷 |
| | `get_estimated_liquidation_price(borrow)` | 获取预估清算价格 |
| **仓位** | `get_open_positions()` | 获取未平仓仓位 |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | 提交 RFQ |
| | `submit_quote(rfqId, price)` | 提交报价 |
| | `accept_quote(rfqId, quoteId)` | 接受报价 |
| | `refresh_rfq(rfqId)` | 刷新 RFQ |
| | `cancel_rfq(rfqId)` | 取消 RFQ |
| **策略** | `create_strategy(...)` | 创建策略 |
| | `get_strategy(symbol, strategyId)` | 获取策略 |
| | `get_open_strategies()` | 获取进行中策略 |
| | `cancel_strategy(symbol, strategyId)` | 取消策略 |
| | `cancel_all_strategies(symbol)` | 取消所有策略 |

### WebSocket 客户端

```python
from backpack_exchange_sdk import WebSocketClient

# 公开流（不需认证）
ws = WebSocketClient()

# 私有流（需要认证）
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# 订阅流
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# 私有流示例
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## 可用枚举

```python
from backpack_exchange_sdk.enums import (
    # 订单相关
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # 市场相关
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # 状态相关
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # 更多...
)
```

## 示例

请参阅 [examples](./examples) 目录获取完整使用示例：

- `example_public.py` - 公开 API 示例
- `example_authenticated.py` - 认证 API 示例
- `example_websocket.py` - WebSocket 流示例

## 文档

详细 API 文档请参阅 [Backpack Exchange API Docs](https://docs.backpack.exchange/)。

## 更新日志

### v1.1.0
- 新增 21 个 API 端点（RFQ、策略、预测市场等）
- 新增 25+ 个枚举类型
- 使用 mixin 重构 SDK 架构
- 100% API 覆盖率（70 个端点）
- 完整类型提示支持

### v1.0.x
- 初始版本，基本 API 支持

## 支持

如果这个 SDK 对你有帮助，请考虑：

1. 使用我的推荐链接注册：[注册 Backpack Exchange](https://backpack.exchange/refer/solomeowl)
2. 在 GitHub 给这个项目一颗星

## 许可证

MIT License
