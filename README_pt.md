# Backpack Exchange SDK

![PyPI - Version](https://img.shields.io/pypi/v/backpack-exchange-sdk?)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)

[English](./README.md) | [简体中文](./README_zh-Hans.md) | [繁體中文](./README_zh-Hant.md) | [日本語](./README_ja.md) | [한국어](./README_ko.md) | [Español](./README_es.md) | **Português**

SDK Python completo para [Backpack Exchange](https://backpack.exchange/). Suporta todos os 70 endpoints da API incluindo REST e WebSocket.

## Recursos

- **Cliente Autenticado**: Acesso completo aos endpoints autenticados (ordens, capital, histórico, RFQ, estratégias)
- **Cliente Público**: Acesso a dados públicos de mercado, status do sistema e dados de negociação
- **Cliente WebSocket**: Streaming em tempo real de dados de mercado e atualizações de conta
- **Cobertura Completa**: Implementação de todos os 70 endpoints da API
- **Type Hints**: Anotações de tipo completas para melhor suporte de IDE
- **Enums**: Enumerações abrangentes para chamadas de API com tipagem segura

## Instalação

```bash
pip install backpack-exchange-sdk
```

Ou instalar a partir do código fonte:

```bash
git clone https://github.com/solomeowl/backpack_exchange_sdk.git
cd backpack_exchange_sdk
pip install .
```

## Início Rápido

### Cliente Público

```python
from backpack_exchange_sdk import PublicClient

client = PublicClient()

# Obter todos os mercados
markets = client.get_markets()

# Obter ticker
ticker = client.get_ticker("SOL_USDC")

# Obter profundidade do livro de ordens
depth = client.get_depth("SOL_USDC")
```

### Cliente Autenticado

```python
from backpack_exchange_sdk import AuthenticationClient

client = AuthenticationClient("<API_KEY>", "<SECRET_KEY>")

# Obter saldos da conta
balances = client.get_balances()

# Executar uma ordem
order = client.execute_order(
    orderType="Limit",
    side="Bid",
    symbol="SOL_USDC",
    price="100",
    quantity="1"
)

# Obter histórico de ordens
history = client.get_order_history(symbol="SOL_USDC")
```

### Usando Enums

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

## Referência da API

### Métodos do Cliente Público

| Categoria | Método | Descrição |
|-----------|--------|-----------|
| **Sistema** | `get_status()` | Obter status do sistema |
| | `send_ping()` | Ping ao servidor |
| | `get_system_time()` | Obter hora do servidor |
| | `get_wallets()` | Obter carteiras suportadas |
| **Ativos** | `get_assets()` | Obter todos os ativos |
| | `get_collateral()` | Obter info de colateral |
| **Mercados** | `get_markets()` | Obter todos os mercados |
| | `get_market(symbol)` | Obter mercado específico |
| | `get_ticker(symbol)` | Obter ticker |
| | `get_tickers()` | Obter todos os tickers |
| | `get_depth(symbol)` | Obter livro de ordens |
| | `get_klines(symbol, interval, startTime)` | Obter candles |
| | `get_mark_price(symbol)` | Obter preço mark |
| | `get_open_interest(symbol)` | Obter interesse aberto |
| | `get_funding_interval_rates(symbol)` | Obter taxas de funding |
| **Negociações** | `get_recent_trades(symbol)` | Obter negociações recentes |
| | `get_historical_trades(symbol, limit, offset)` | Obter histórico de negociações |
| **Empréstimos** | `get_borrow_lend_markets()` | Obter mercados de empréstimo |
| | `get_borrow_lend_market_history(interval)` | Obter histórico de empréstimos |
| **Previsão** | `get_prediction_markets()` | Obter mercados de previsão |
| | `get_prediction_tags()` | Obter tags de previsão |

### Métodos do Cliente Autenticado

| Categoria | Método | Descrição |
|-----------|--------|-----------|
| **Conta** | `get_account()` | Obter configurações da conta |
| | `update_account(...)` | Atualizar configurações |
| | `get_max_borrow_quantity(symbol)` | Obter quantidade máx. de empréstimo |
| | `get_max_order_quantity(symbol, side)` | Obter quantidade máx. de ordem |
| | `get_max_withdrawal_quantity(symbol)` | Obter quantidade máx. de saque |
| **Capital** | `get_balances()` | Obter saldos |
| | `get_collateral()` | Obter colateral |
| | `get_deposits()` | Obter histórico de depósitos |
| | `get_deposit_address(blockchain)` | Obter endereço de depósito |
| | `get_withdrawals()` | Obter histórico de saques |
| | `request_withdrawal(...)` | Solicitar saque |
| | `convert_dust(symbol)` | Converter dust para USDC |
| | `get_withdrawal_delay()` | Obter atraso de saque |
| | `create_withdrawal_delay(hours, token)` | Criar atraso de saque |
| | `update_withdrawal_delay(hours, token)` | Atualizar atraso de saque |
| **Ordens** | `execute_order(...)` | Executar ordem |
| | `execute_batch_orders(orders)` | Executar ordens em lote |
| | `get_users_open_orders(symbol)` | Obter ordens abertas do usuário |
| | `get_open_orders(symbol)` | Obter ordens abertas |
| | `cancel_open_order(symbol, orderId)` | Cancelar ordem individual |
| | `cancel_open_orders(symbol)` | Cancelar todas as ordens |
| **Histórico** | `get_order_history(symbol)` | Obter histórico de ordens |
| | `get_fill_history(symbol)` | Obter histórico de execuções |
| | `get_borrow_history()` | Obter histórico de empréstimos |
| | `get_interest_history()` | Obter histórico de juros |
| | `get_borrow_position_history()` | Obter histórico de posições |
| | `get_funding_payments()` | Obter pagamentos de funding |
| | `get_settlement_history()` | Obter histórico de liquidações |
| | `get_dust_history()` | Obter histórico de conversão dust |
| | `get_position_history()` | Obter histórico de posições |
| | `get_strategy_history()` | Obter histórico de estratégias |
| | `get_rfq_history()` | Obter histórico RFQ |
| | `get_quote_history()` | Obter histórico de cotações |
| | `get_rfq_fill_history()` | Obter histórico de execuções RFQ |
| | `get_quote_fill_history()` | Obter histórico de execuções de cotações |
| **Empréstimos** | `get_borrow_lend_positions()` | Obter posições |
| | `execute_borrow_lend(quantity, side, symbol)` | Emprestar ou tomar emprestado |
| | `get_estimated_liquidation_price(borrow)` | Obter preço de liquidação estimado |
| **Posições** | `get_open_positions()` | Obter posições abertas |
| **RFQ** | `submit_rfq(symbol, side, quantity)` | Enviar RFQ |
| | `submit_quote(rfqId, price)` | Enviar cotação |
| | `accept_quote(rfqId, quoteId)` | Aceitar cotação |
| | `refresh_rfq(rfqId)` | Atualizar RFQ |
| | `cancel_rfq(rfqId)` | Cancelar RFQ |
| **Estratégia** | `create_strategy(...)` | Criar estratégia |
| | `get_strategy(symbol, strategyId)` | Obter estratégia |
| | `get_open_strategies()` | Obter estratégias ativas |
| | `cancel_strategy(symbol, strategyId)` | Cancelar estratégia |
| | `cancel_all_strategies(symbol)` | Cancelar todas as estratégias |

### Cliente WebSocket

```python
from backpack_exchange_sdk import WebSocketClient

# Streams públicos (sem autenticação)
ws = WebSocketClient()

# Streams privados (requer autenticação)
ws = WebSocketClient(api_key="<API_KEY>", secret_key="<SECRET_KEY>")

# Inscrever-se em streams
def on_message(data):
    print(data)

ws.subscribe(
    streams=["bookTicker.SOL_USDC"],
    callback=on_message
)

# Exemplo de stream privado
ws.subscribe(
    streams=["account.orderUpdate"],
    callback=on_message,
    is_private=True
)
```

## Enums Disponíveis

```python
from backpack_exchange_sdk.enums import (
    # Relacionados a ordens
    OrderType,          # Limit, Market
    Side,               # Bid, Ask
    TimeInForce,        # GTC, IOC, FOK
    SelfTradePrevention,
    TriggerBy,

    # Relacionados a mercado
    MarketType,         # Spot, Perp
    FillType,
    KlineInterval,

    # Relacionados a status
    OrderStatus,
    DepositStatus,
    WithdrawalStatus,

    # E mais...
)
```

## Exemplos

Consulte o diretório [examples](./examples) para exemplos completos:

- `example_public.py` - Exemplos de API pública
- `example_authenticated.py` - Exemplos de API autenticada
- `example_websocket.py` - Exemplos de streaming WebSocket

## Documentação

Para documentação detalhada da API, visite [Backpack Exchange API Docs](https://docs.backpack.exchange/).

## Registro de Alterações

### v1.1.0
- Adicionados 21 novos endpoints de API (RFQ, Estratégia, Mercados de Previsão, etc.)
- Adicionados 25+ novos tipos de enumeração
- Arquitetura do SDK refatorada usando mixins
- 100% de cobertura da API (70 endpoints)
- Suporte completo a type hints

### v1.0.x
- Lançamento inicial com suporte básico de API

## Suporte

Se este SDK foi útil para você, considere:

1. Usar meu link de indicação para se registrar: [Registrar no Backpack Exchange](https://backpack.exchange/refer/solomeowl)
2. Dar uma estrela a este projeto no GitHub

## Licença

MIT License
