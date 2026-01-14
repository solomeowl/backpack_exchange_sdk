"""
Capital-related enums for Backpack Exchange SDK.
"""

from enum import Enum


class DepositStatus(Enum):
    """Deposit status."""
    CANCELLED = "cancelled"
    CONFIRMED = "confirmed"
    DECLINED = "declined"
    EXPIRED = "expired"
    INITIATED = "initiated"
    OWNERSHIP_VERIFICATION_REQUIRED = "ownershipVerificationRequired"
    PENDING = "pending"
    REFUNDED = "refunded"
    SENDER_VERIFICATION_COMPLETED = "senderVerificationCompleted"
    SENDER_VERIFICATION_REQUIRED = "senderVerificationRequired"


class WithdrawalStatus(Enum):
    """Withdrawal status."""
    CONFIRMED = "confirmed"
    OWNERSHIP_VERIFICATION_REQUIRED = "ownershipVerificationRequired"
    PENDING = "pending"
    RECIPIENT_INFORMATION_PROVIDED = "recipientInformationProvided"
    RECIPIENT_INFORMATION_REQUIRED = "recipientInformationRequired"


class DepositSource(Enum):
    """Deposit source."""
    ADMINISTRATOR = "administrator"
    ZERO_G = "0G"
    APTOS = "aptos"
    ARBITRUM = "arbitrum"
    AVALANCHE = "avalanche"
    BASE = "base"
    BERACHAIN = "berachain"
    BITCOIN = "bitcoin"
    BITCOIN_CASH = "bitcoinCash"
    BSC = "bsc"
    CARDANO = "cardano"
    COSMOS = "cosmos"
    DOGE = "doge"
    ECLIPSE = "eclipse"
    ETHEREUM = "ethereum"
    HYPERLIQUID = "hyperliquid"
    INJECTIVE = "injective"
    LITECOIN = "litecoin"
    MONAD = "monad"
    NEAR = "near"
    OPTIMISM = "optimism"
    POLKADOT = "polkadot"
    POLYGON = "polygon"
    RIPPLE = "ripple"
    SEI = "sei"
    SOLANA = "solana"
    SONIC = "sonic"
    STELLAR = "stellar"
    SUI = "sui"
    TON = "ton"
    TRON = "tron"
    INTERNAL = "internal"
