# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

[English](./README.md) | [简体中文](./README_zh-Hans.md) | [繁體中文](./README_zh-Hant.md) | [日本語](./README_ja.md) | **한국어** | [Español](./README_es.md) | [Português](./README_pt.md)

[Backpack Exchange](https://backpack.exchange/)를 위한 완전한 Python SDK. REST와 WebSocket을 포함한 70개의 모든 API 엔드포인트를 지원합니다.

## 기능

- **인증 클라이언트**: 인증 엔드포인트에 대한 완전한 접근 (주문, 자금, 기록, RFQ, 전략)
- **퍼블릭 클라이언트**: 공개 시장 데이터, 시스템 상태 및 거래 데이터 접근
- **WebSocket 클라이언트**: 실시간 시장 데이터 및 계정 업데이트 스트리밍
- **완전한 커버리지**: 모든 70개 API 엔드포인트 구현
- **타입 힌트**: 더 나은 IDE 지원을 위한 완전한 타입 어노테이션
- **열거형**: 타입 안전한 API 호출을 위한 포괄적인 열거형

## 설치

```bash
pip install backpack-exchange-sdk
```

또는 소스에서 설치:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## 빠른 시작

### 퍼블릭 클라이언트

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# 모든 마켓 조회
markets = client.get_markets()

# 티커 조회
ticker = client.get_ticker("SOL_USDC")

# 오더북 깊이 조회
depth = client.get_depth("SOL_USDC")
```

### 인증 클라이언트

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# 계정 잔액 조회
balances = client.get_balances()

# 주문 실행
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# 주문 기록 조회
history = client.get_order_history(symbol="SOL_USDC")
```

### 열거형 사용

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

## API 레퍼런스

### 퍼블릭 클라이언트 메서드

| 카테고리 | 메서드 | 설명 |
|----------|--------|------|
| **시스템** | `get_status()` | 시스템 상태 조회 |
| | `send_ping()` | 서버 Ping |
| | `get_system_time()` | 서버 시간 조회 |
| | `get_wallets()` | 지원되는 지갑 조회 |
| **자산** | `get_assets()` | 모든 자산 조회 |
| | `get_collateral()` | 담보 정보 조회 |
| **마켓** | `get_markets()` | 모든 마켓 조회 |
| | `get_market(symbol)` | 특정 마켓 조회 |
| | `get_ticker(symbol)` | 티커 조회 |
| | `get_tickers()` | 모든 티커 조회 |
| | `get_depth(symbol)` | 오더북 조회 |
| | `get_klines(symbol, interval, startTime)` | 캔들스틱 조회 |
| | `get_mark_price(symbol)` | 마크 가격 조회 |
| | `get_open_interest(symbol)` | 미결제약정 조회 |
| | `get_funding_interval_rates(symbol)` | 펀딩 비율 조회 |
| **거래** | `get_recent_trades(symbol)` | 최근 거래 조회 |
| | `get_historical_trades(symbol, limit, offset)` | 거래 기록 조회 |
| **대출** | `get_borrow_lend_markets()` | 대출 마켓 조회 |
| | `get_borrow_lend_market_history(interval)` | 대출 기록 조회 |
| **예측 마켓** | `get_prediction_markets()` | 예측 마켓 조회 |
| | `get_prediction_tags()` | 예측 태그 조회 |

### 인증 클라이언트 메서드

| 카테고리 | 메서드 | 설명 |
|----------|--------|------|
| **계정** | `get_account()` | 계정 설정 조회 |
| | `update_account(...)` | 계정 설정 업데이트 |
| | `get_max_borrow_quantity(symbol)` | 최대 차입 수량 조회 |
| | `get_max_order_quantity(symbol, side)` | 최대 주문 수량 조회 |
| | `get_max_withdrawal_quantity(symbol)` | 최대 출금 수량 조회 |
| **자금** | `get_balances()` | 잔액 조회 |
| | `get_collateral()` | 담보 조회 |
| | `get_deposits()` | 입금 기록 조회 |
| | `get_deposit_address(blockchain)` | 입금 주소 조회 |
| | `get_withdrawals()` | 출금 기록 조회 |
| | `request_withdrawal(...)` | 출금 요청 |
| | `convert_dust(symbol)` | 더스트를 USDC로 변환 |
| | `get_withdrawal_delay()` | 출금 지연 설정 조회 |
| | `create_withdrawal_delay(hours, token)` | 출금 지연 생성 |
| | `update_withdrawal_delay(hours, token)` | 출금 지연 업데이트 |
| **주문** | `execute_order(...)` | 주문 실행 |
| | `execute_batch_orders(orders)` | 일괄 주문 |
| | `get_users_open_orders(symbol)` | 사용자의 미체결 주문 조회 |
| | `get_open_orders(symbol)` | 미체결 주문 조회 |
| | `cancel_open_order(symbol, orderId)` | 단일 주문 취소 |
| | `cancel_open_orders(symbol)` | 모든 주문 취소 |
| **기록** | `get_order_history(symbol)` | 주문 기록 조회 |
| | `get_fill_history(symbol)` | 체결 기록 조회 |
| | `get_borrow_history()` | 차입 기록 조회 |
| | `get_interest_history()` | 이자 기록 조회 |
| | `get_borrow_position_history()` | 차입 포지션 기록 조회 |
| | `get_funding_payments()` | 펀딩 지불 조회 |
| | `get_settlement_history()` | 정산 기록 조회 |
| | `get_dust_history()` | 더스트 변환 기록 조회 |
| | `get_position_history()` | 포지션 기록 조회 |
| | `get_strategy_history()` | 전략 기록 조회 |
| | `get_rfq_history()` | RFQ 기록 조회 |
| | `get_quote_history()` | 견적 기록 조회 |
| | `get_rfq_fill_history()` | RFQ 체결 기록 조회 |
| | `get_quote_fill_history()` | 견적 체결 기록 조회 |
| **대출** | `get_borrow_lend_positions()` | 포지션 조회 |
| | `execute_borrow_lend(quantity, side, symbol)` | 차입 또는 대출 |
| | `get_estimated_liquidation_price(borrow)` | 예상 청산 가격 조회 |
| **포지션** | `get_open_positions()` | 미결제 포지션 조회 |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | RFQ 제출 |
| | `submit_quote(rfqId, price)` | 견적 제출 |
| | `accept_quote(rfqId, quoteId)` | 견적 수락 |
| | `refresh_rfq(rfqId)` | RFQ 갱신 |
| | `cancel_rfq(rfqId)` | RFQ 취소 |
| **전략** | `create_strategy(...)` | 전략 생성 |
| | `get_strategy(symbol, strategyId)` | 전략 조회 |
| | `get_open_strategies()` | 실행 중인 전략 조회 |
| | `cancel_strategy(symbol, strategyId)` | 전략 취소 |
| | `cancel_all_strategies(symbol)` | 모든 전략 취소 |

### WebSocket 클라이언트

```python
from backpack_exchange_sdk import WebSocketClient

# 퍼블릭 스트림 (인증 불필요)
ws = WebSocketClient()

# 프라이빗 스트림 (인증 필요)
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# 스트림 구독
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# 프라이빗 스트림 예제
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## 사용 가능한 열거형

```python
from backpack_exchange_sdk.enums import (
    # 주문 관련
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # 마켓 관련
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # 상태 관련
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # 기타...
)
```

## 예제

완전한 사용 예제는 [examples](./examples) 디렉토리를 참조하세요:

- `example_public.py` - 퍼블릭 API 예제
- `example_authenticated.py` - 인증 API 예제
- `example_websocket.py` - WebSocket 스트리밍 예제

## 문서

자세한 API 문서는 [Backpack Exchange API Docs](https://docs.backpack.exchange/)를 참조하세요.

## 변경 로그

### v1.1.0
- 21개의 새로운 API 엔드포인트 추가 (RFQ, 전략, 예측 마켓 등)
- 25개 이상의 새로운 열거형 추가
- mixin을 사용한 SDK 아키텍처 리팩토링
- 100% API 커버리지 (70개 엔드포인트)
- 완전한 타입 힌트 지원

### v1.0.x
- 초기 릴리스, 기본 API 지원

## 지원

이 SDK가 도움이 되었다면 다음을 고려해 주세요:

1. 추천 링크로 가입: [Backpack Exchange 가입](https://backpack.exchange/refer/solomeowl)
2. GitHub에서 이 프로젝트에 스타 주기

## 라이선스

MIT License
