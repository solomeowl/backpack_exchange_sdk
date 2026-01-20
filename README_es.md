# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?cacheSeconds=300)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/pypi/l/backpack-exchange-sdk?cacheSeconds=300)
![CI](https://github.com/solomeowl/backpack_exchange_sdk/actions/workflows/ci.yml/badge.svg)

[English](./README.md) | [简体中文](./README_zh-Hans.md) | [繁體中文](./README_zh-Hant.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md) | **Español** | [Português](./README_pt.md)

SDK completo de Python para [Backpack Exchange](https://backpack.exchange/). Soporta los 70 endpoints de API incluyendo REST y WebSocket.

## Documentación del proyecto

- [Registro de cambios](./CHANGELOG.md)
- [Política de seguridad](./SECURITY.md)
- [Guía de contribución](./CONTRIBUTING.md)

## Características

- **Cliente Autenticado**: Acceso completo a endpoints autenticados (órdenes, capital, historial, RFQ, estrategias)
- **Cliente Público**: Acceso a datos de mercado públicos, estado del sistema y datos de operaciones
- **Cliente WebSocket**: Streaming en tiempo real de datos de mercado y actualizaciones de cuenta
- **Cobertura Completa**: Implementación de los 70 endpoints de API
- **Type Hints**: Anotaciones de tipo completas para mejor soporte de IDE
- **Enums**: Enumeraciones completas para llamadas API con tipado seguro

## Instalación

```bash
pip install backpack-exchange-sdk
```

O instalar desde el código fuente:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## Inicio Rápido

### Cliente Público

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# Obtener todos los mercados
markets = client.get_markets()

# Obtener ticker
ticker = client.get_ticker("SOL_USDC")

# Obtener profundidad del libro de órdenes
depth = client.get_depth("SOL_USDC")
```

### Cliente Autenticado

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# Obtener saldos de cuenta
balances = client.get_balances()

# Ejecutar una orden
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# Obtener historial de órdenes
history = client.get_order_history(symbol="SOL_USDC")
```

### Uso de Enums

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

## Referencia de API

### Métodos del Cliente Público

| Categoría | Método | Descripción |
|-----------|--------|-------------|
| **Sistema** | `get_status()` | Obtener estado del sistema |
| | `send_ping()` | Ping al servidor |
| | `get_system_time()` | Obtener hora del servidor |
| | `get_wallets()` | Obtener wallets soportadas |
| **Activos** | `get_assets()` | Obtener todos los activos |
| | `get_collateral()` | Obtener info de colateral |
| **Mercados** | `get_markets()` | Obtener todos los mercados |
| | `get_market(symbol)` | Obtener mercado específico |
| | `get_ticker(symbol)` | Obtener ticker |
| | `get_tickers()` | Obtener todos los tickers |
| | `get_depth(symbol)` | Obtener libro de órdenes |
| | `get_klines(symbol, interval, startTime)` | Obtener velas |
| | `get_mark_price(symbol)` | Obtener precio mark |
| | `get_open_interest(symbol)` | Obtener interés abierto |
| | `get_funding_interval_rates(symbol)` | Obtener tasas de funding |
| **Operaciones** | `get_recent_trades(symbol)` | Obtener operaciones recientes |
| | `get_historical_trades(symbol, limit, offset)` | Obtener historial de operaciones |
| **Préstamos** | `get_borrow_lend_markets()` | Obtener mercados de préstamos |
| | `get_borrow_lend_market_history(interval)` | Obtener historial de préstamos |
| **Predicción** | `get_prediction_markets()` | Obtener mercados de predicción |
| | `get_prediction_tags()` | Obtener etiquetas de predicción |

### Métodos del Cliente Autenticado

| Categoría | Método | Descripción |
|-----------|--------|-------------|
| **Cuenta** | `get_account()` | Obtener configuración de cuenta |
| | `update_account(...)` | Actualizar configuración |
| | `get_max_borrow_quantity(symbol)` | Obtener cantidad máx. de préstamo |
| | `get_max_order_quantity(symbol, side)` | Obtener cantidad máx. de orden |
| | `get_max_withdrawal_quantity(symbol)` | Obtener cantidad máx. de retiro |
| **Capital** | `get_balances()` | Obtener saldos |
| | `get_collateral()` | Obtener colateral |
| | `get_deposits()` | Obtener historial de depósitos |
| | `get_deposit_address(blockchain)` | Obtener dirección de depósito |
| | `get_withdrawals()` | Obtener historial de retiros |
| | `request_withdrawal(...)` | Solicitar retiro |
| | `convert_dust(symbol)` | Convertir dust a USDC |
| | `get_withdrawal_delay()` | Obtener retraso de retiro |
| | `create_withdrawal_delay(hours, token)` | Crear retraso de retiro |
| | `update_withdrawal_delay(hours, token)` | Actualizar retraso de retiro |
| **Órdenes** | `execute_order(...)` | Ejecutar orden |
| | `execute_batch_orders(orders)` | Ejecutar órdenes en lote |
| | `get_users_open_orders(symbol)` | Obtener órdenes abiertas del usuario |
| | `get_open_orders(symbol)` | Obtener órdenes abiertas |
| | `cancel_open_order(symbol, orderId)` | Cancelar orden individual |
| | `cancel_open_orders(symbol)` | Cancelar todas las órdenes |
| **Historial** | `get_order_history(symbol)` | Obtener historial de órdenes |
| | `get_fill_history(symbol)` | Obtener historial de ejecuciones |
| | `get_borrow_history()` | Obtener historial de préstamos |
| | `get_interest_history()` | Obtener historial de intereses |
| | `get_borrow_position_history()` | Obtener historial de posiciones |
| | `get_funding_payments()` | Obtener pagos de funding |
| | `get_settlement_history()` | Obtener historial de liquidaciones |
| | `get_dust_history()` | Obtener historial de conversión dust |
| | `get_position_history()` | Obtener historial de posiciones |
| | `get_strategy_history()` | Obtener historial de estrategias |
| | `get_rfq_history()` | Obtener historial RFQ |
| | `get_quote_history()` | Obtener historial de cotizaciones |
| | `get_rfq_fill_history()` | Obtener historial de ejecuciones RFQ |
| | `get_quote_fill_history()` | Obtener historial de ejecuciones de cotizaciones |
| **Préstamos** | `get_borrow_lend_positions()` | Obtener posiciones |
| | `execute_borrow_lend(quantity, side, symbol)` | Prestar o pedir prestado |
| | `get_estimated_liquidation_price(borrow)` | Obtener precio de liquidación estimado |
| **Posiciones** | `get_open_positions()` | Obtener posiciones abiertas |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | Enviar RFQ |
| | `submit_quote(rfqId, price)` | Enviar cotización |
| | `accept_quote(rfqId, quoteId)` | Aceptar cotización |
| | `refresh_rfq(rfqId)` | Actualizar RFQ |
| | `cancel_rfq(rfqId)` | Cancelar RFQ |
| **Estrategia** | `create_strategy(...)` | Crear estrategia |
| | `get_strategy(symbol, strategyId)` | Obtener estrategia |
| | `get_open_strategies()` | Obtener estrategias activas |
| | `cancel_strategy(symbol, strategyId)` | Cancelar estrategia |
| | `cancel_all_strategies(symbol)` | Cancelar todas las estrategias |

### Cliente WebSocket

```python
from backpack_exchange_sdk import WebSocketClient

# Streams públicos (sin autenticación)
ws = WebSocketClient()

# Streams privados (requiere autenticación)
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# Suscribirse a streams
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# Ejemplo de stream privado
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## Enums Disponibles

```python
from backpack_exchange_sdk.enums import (
    # Relacionados con órdenes
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # Relacionados con mercado
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # Relacionados con estado
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # Y más...
)
```

## Ejemplos

Consulta el directorio [examples](./examples) para ejemplos completos:

- `example_public.py` - Ejemplos de API pública
- `example_authenticated.py` - Ejemplos de API autenticada
- `example_websocket.py` - Ejemplos de streaming WebSocket

## Documentación

Para documentación detallada de la API, visita [Backpack Exchange API Docs](https://docs.backpack.exchange/).

## Registro de Cambios

### v1.1.0
- Añadidos 21 nuevos endpoints de API (RFQ, Estrategia, Mercados de Predicción, etc.)
- Añadidos 25+ nuevos tipos de enumeración
- Arquitectura SDK refactorizada usando mixins
- 100% cobertura de API (70 endpoints)
- Soporte completo de type hints

### v1.0.x
- Lanzamiento inicial con soporte básico de API

## Soporte

Si este SDK te ha sido útil, considera:

1. Usar mi enlace de referido para registrarte: [Registrarse en Backpack Exchange](https://backpack.exchange/refer/solomeowl)
2. Dar una estrella a este proyecto en GitHub

## Licencia

MIT License
