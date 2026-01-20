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
    DOGECOIN = "Dogecoin"
    ECLIPSE = "Eclipse"
    EQUALS_MONEY = "EqualsMoney"
    ETHEREUM = "Ethereum"
    FOGO = "Fogo"
    HYPER_EVM = "HyperEVM"
    HYPERLIQUID = "Hyperliquid"
    LINEA = "Linea"
    LITECOIN = "Litecoin"
    MONAD = "Monad"
    NEAR = "Near"
    OPTIMISM = "Optimism"
    PLASMA = "Plasma"
    POLYGON = "Polygon"
    SEI = "Sei"
    SUI = "Sui"
    SOLANA = "Solana"
    STABLE = "Stable"
    STORY = "Story"
    TRON = "Tron"
    XRP = "XRP"
    ZCASH = "Zcash"


class SortDirection(Enum):
    """Sort direction for queries."""
    ASC = "Asc"
    DESC = "Desc"

