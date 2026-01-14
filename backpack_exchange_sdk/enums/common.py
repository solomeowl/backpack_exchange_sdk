"""
Common enums used across the Backpack Exchange SDK.
"""

from enum import Enum


class Blockchain(Enum):
    """Supported blockchain networks."""
    ZERO_G = "0G"
    APTOS = "Aptos"
    ARBITRUM = "Arbitrum"
    AVALANCHE = "Avalanche"
    BASE = "Base"
    BERACHAIN = "Berachain"
    BITCOIN = "Bitcoin"
    BITCOIN_CASH = "BitcoinCash"
    BSC = "Bsc"
    CARDANO = "Cardano"
    COSMOS = "Cosmos"
    DOGE = "Doge"
    ECLIPSE = "Eclipse"
    ETHEREUM = "Ethereum"
    HYPERLIQUID = "Hyperliquid"
    INJECTIVE = "Injective"
    LITECOIN = "Litecoin"
    MONAD = "Monad"
    NEAR = "Near"
    OPTIMISM = "Optimism"
    POLKADOT = "Polkadot"
    POLYGON = "Polygon"
    RIPPLE = "Ripple"
    SEI = "Sei"
    SOLANA = "Solana"
    SONIC = "Sonic"
    STELLAR = "Stellar"
    SUI = "Sui"
    TON = "Ton"
    TRON = "Tron"


class SortDirection(Enum):
    """Sort direction for queries."""
    ASC = "Asc"
    DESC = "Desc"


class TriggerBy(Enum):
    """Price type to trigger conditional orders."""
    LAST_PRICE = "LastPrice"
    MARK_PRICE = "MarkPrice"
    INDEX_PRICE = "IndexPrice"
