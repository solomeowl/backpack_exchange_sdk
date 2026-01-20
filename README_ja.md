# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?cacheSeconds=300)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/pypi/l/backpack-exchange-sdk?cacheSeconds=300)

[English](./README.md) | [简体中文](./README_zh-Hans.md) | [繁體中文](./README_zh-Hant.md) | **日本語** | [한국어](./README_ko.md) | [Español](./README_es.md) | [Português](./README_pt.md)

[Backpack Exchange](https://backpack.exchange/) の完全な Python SDK。REST と WebSocket を含む全 70 API エンドポイントをサポート。

## プロジェクトドキュメント

- [変更履歴](./CHANGELOG.md)
- [セキュリティポリシー](./SECURITY.md)
- [コントリビューションガイド](./CONTRIBUTING.md)

## 機能

- **認証クライアント**: 認証エンドポイントへの完全アクセス（注文、資金、履歴、RFQ、ストラテジー）
- **パブリッククライアント**: 公開市場データ、システムステータス、取引データへのアクセス
- **WebSocket クライアント**: リアルタイムの市場データとアカウント更新のストリーミング
- **完全カバレッジ**: 全 70 API エンドポイントを実装
- **型ヒント**: より良い IDE サポートのための完全な型アノテーション
- **列挙型**: 型安全な API 呼び出しのための包括的な列挙型

## インストール

```bash
pip install backpack-exchange-sdk
```

またはソースからインストール：

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## クイックスタート

### パブリッククライアント

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# 全マーケットを取得
markets = client.get_markets()

# ティッカーを取得
ticker = client.get_ticker("SOL_USDC")

# オーダーブックの深さを取得
depth = client.get_depth("SOL_USDC")
```

### 認証クライアント

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# アカウント残高を取得
balances = client.get_balances()

# 注文を出す
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# 注文履歴を取得
history = client.get_order_history(symbol="SOL_USDC")
```

### 列挙型の使用

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

## API リファレンス

### パブリッククライアントメソッド

| カテゴリ | メソッド | 説明 |
|----------|--------|------|
| **システム** | `get_status()` | システムステータスを取得 |
| | `send_ping()` | サーバーに Ping |
| | `get_system_time()` | サーバー時刻を取得 |
| | `get_wallets()` | サポートされているウォレットを取得 |
| **アセット** | `get_assets()` | 全アセットを取得 |
| | `get_collateral()` | 担保情報を取得 |
| **マーケット** | `get_markets()` | 全マーケットを取得 |
| | `get_market(symbol)` | 特定のマーケットを取得 |
| | `get_ticker(symbol)` | ティッカーを取得 |
| | `get_tickers()` | 全ティッカーを取得 |
| | `get_depth(symbol)` | オーダーブックを取得 |
| | `get_klines(symbol, interval, startTime)` | ローソク足を取得 |
| | `get_mark_price(symbol)` | マーク価格を取得 |
| | `get_open_interest(symbol)` | 建玉を取得 |
| | `get_funding_interval_rates(symbol)` | ファンディングレートを取得 |
| **取引** | `get_recent_trades(symbol)` | 最近の取引を取得 |
| | `get_historical_trades(symbol, limit, offset)` | 取引履歴を取得 |
| **レンディング** | `get_borrow_lend_markets()` | レンディング市場を取得 |
| | `get_borrow_lend_market_history(interval)` | レンディング履歴を取得 |
| **予測市場** | `get_prediction_markets()` | 予測市場を取得 |
| | `get_prediction_tags()` | 予測タグを取得 |

### 認証クライアントメソッド

| カテゴリ | メソッド | 説明 |
|----------|--------|------|
| **アカウント** | `get_account()` | アカウント設定を取得 |
| | `update_account(...)` | アカウント設定を更新 |
| | `get_max_borrow_quantity(symbol)` | 最大借入数量を取得 |
| | `get_max_order_quantity(symbol, side)` | 最大注文数量を取得 |
| | `get_max_withdrawal_quantity(symbol)` | 最大出金数量を取得 |
| **資金** | `get_balances()` | 残高を取得 |
| | `get_collateral()` | 担保を取得 |
| | `get_deposits()` | 入金履歴を取得 |
| | `get_deposit_address(blockchain)` | 入金アドレスを取得 |
| | `get_withdrawals()` | 出金履歴を取得 |
| | `request_withdrawal(...)` | 出金をリクエスト |
| | `convert_dust(symbol)` | ダストを USDC に変換 |
| | `get_withdrawal_delay()` | 出金遅延設定を取得 |
| | `create_withdrawal_delay(hours, token)` | 出金遅延を作成 |
| | `update_withdrawal_delay(hours, token)` | 出金遅延を更新 |
| **注文** | `execute_order(...)` | 注文を出す |
| | `execute_batch_orders(orders)` | 一括注文 |
| | `get_users_open_orders(symbol)` | ユーザーの未約定注文を取得 |
| | `get_open_orders(symbol)` | 未約定注文を取得 |
| | `cancel_open_order(symbol, orderId)` | 単一注文をキャンセル |
| | `cancel_open_orders(symbol)` | 全注文をキャンセル |
| **履歴** | `get_order_history(symbol)` | 注文履歴を取得 |
| | `get_fill_history(symbol)` | 約定履歴を取得 |
| | `get_borrow_history()` | 借入履歴を取得 |
| | `get_interest_history()` | 金利履歴を取得 |
| | `get_borrow_position_history()` | 借入ポジション履歴を取得 |
| | `get_funding_payments()` | ファンディング支払いを取得 |
| | `get_settlement_history()` | 決済履歴を取得 |
| | `get_dust_history()` | ダスト変換履歴を取得 |
| | `get_position_history()` | ポジション履歴を取得 |
| | `get_strategy_history()` | ストラテジー履歴を取得 |
| | `get_rfq_history()` | RFQ 履歴を取得 |
| | `get_quote_history()` | クォート履歴を取得 |
| | `get_rfq_fill_history()` | RFQ 約定履歴を取得 |
| | `get_quote_fill_history()` | クォート約定履歴を取得 |
| **レンディング** | `get_borrow_lend_positions()` | ポジションを取得 |
| | `execute_borrow_lend(quantity, side, symbol)` | 借入または貸出 |
| | `get_estimated_liquidation_price(borrow)` | 推定清算価格を取得 |
| **ポジション** | `get_open_positions()` | 未決済ポジションを取得 |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | RFQ を提出 |
| | `submit_quote(rfqId, price)` | クォートを提出 |
| | `accept_quote(rfqId, quoteId)` | クォートを受諾 |
| | `refresh_rfq(rfqId)` | RFQ を更新 |
| | `cancel_rfq(rfqId)` | RFQ をキャンセル |
| **ストラテジー** | `create_strategy(...)` | ストラテジーを作成 |
| | `get_strategy(symbol, strategyId)` | ストラテジーを取得 |
| | `get_open_strategies()` | 実行中のストラテジーを取得 |
| | `cancel_strategy(symbol, strategyId)` | ストラテジーをキャンセル |
| | `cancel_all_strategies(symbol)` | 全ストラテジーをキャンセル |

### WebSocket クライアント

```python
from backpack_exchange_sdk import WebSocketClient

# パブリックストリーム（認証不要）
ws = WebSocketClient()

# プライベートストリーム（認証必要）
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# ストリームを購読
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# プライベートストリームの例
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## 利用可能な列挙型

```python
from backpack_exchange_sdk.enums import (
    # 注文関連
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # マーケット関連
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # ステータス関連
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # その他...
)
```

## サンプル

完全な使用例は [examples](./examples) ディレクトリを参照してください：

- `example_public.py` - パブリック API のサンプル
- `example_authenticated.py` - 認証 API のサンプル
- `example_websocket.py` - WebSocket ストリーミングのサンプル

## ドキュメント

詳細な API ドキュメントは [Backpack Exchange API Docs](https://docs.backpack.exchange/) を参照してください。

## 変更履歴

### v1.1.0
- 21 の新しい API エンドポイントを追加（RFQ、ストラテジー、予測市場など）
- 25 以上の新しい列挙型を追加
- mixin を使用して SDK アーキテクチャをリファクタリング
- 100% API カバレッジ（70 エンドポイント）
- 完全な型ヒントサポート

### v1.0.x
- 初期リリース、基本的な API サポート

## サポート

この SDK が役に立った場合は、以下をご検討ください：

1. 紹介リンクから登録：[Backpack Exchange に登録](https://backpack.exchange/refer/solomeowl)
2. GitHub でこのプロジェクトにスターを付ける

## ライセンス

MIT License
