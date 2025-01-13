from pydantic import BaseModel, RootModel
from typing import List, Tuple, Dict, Optional


class Token(BaseModel):
    blockchain: str
    contractAddress: Optional[str] = None
    depositEnabled: bool
    minimumDeposit: str
    withdrawEnabled: bool
    minimumWithdrawal: str
    maximumWithdrawal: Optional[str] = None
    withdrawalFee: str


class Asset(BaseModel):
    symbol: str
    tokens: List[Token]


class ApiError(BaseModel):
    code: str
    message: str


class SqrtFunction(BaseModel):
    type: str
    base: str
    factor: str


class CollateralFunctionKind(BaseModel):
    type: str


class CollateralFunction(BaseModel):
    type: str
    base: str
    factor: str


class HaircutFunction(BaseModel):
    weight: str
    kind: CollateralFunctionKind


class CollateralInfo(BaseModel):
    symbol: str
    imfFunction: CollateralFunction
    mmfFunction: CollateralFunction
    haircutFunction: HaircutFunction


class PriceBand(BaseModel):
    maxMultiplier: str
    minMultiplier: str


class PremiumBand(BaseModel):
    tolerancePct: str


class QuantityFilter(BaseModel):
    minQuantity: str
    maxQuantity: Optional[str] = None
    stepSize: str


class LeverageFilter(BaseModel):
    minLeverage: Optional[int] = None
    maxLeverage: Optional[int] = None
    stepSize: Optional[int] = None


class PriceFilter(BaseModel):
    minPrice: str
    maxPrice: Optional[str] = None
    tickSize: str
    maxMultiplier: Optional[str] = None
    minMultiplier: Optional[str] = None
    maxImpactMultiplier: Optional[str] = None
    minImpactMultiplier: Optional[str] = None
    meanMarkPriceBand: Optional[PriceBand] = None
    meanPremiumBand: Optional[PremiumBand] = None


class MarketFilters(BaseModel):
    price: PriceFilter
    quantity: QuantityFilter
    leverage: Optional[LeverageFilter] = None


class Market(BaseModel):
    symbol: str
    baseSymbol: str
    quoteSymbol: str
    filters: MarketFilters
    fundingInterval: Optional[int] = None
    imfFunction: Optional[dict] = None
    mmfFunction: Optional[dict] = None
    marketType: str


class Ticker(BaseModel):
    symbol: str
    firstPrice: str
    lastPrice: str
    priceChange: str
    priceChangePercent: str
    high: str
    low: str
    volume: str
    quoteVolume: str
    trades: str


class Depth(BaseModel):
    asks: List[Tuple[str, str]]
    bids: List[Tuple[str, str]]
    lastUpdateId: str
    timestamp: int


class Kline(BaseModel):
    start: str
    end: str
    open: str = None
    high: str = None
    low: str = None
    close: str = None
    volume: str
    quoteVolume: str
    trades: str


class MarkPrice(BaseModel):
    fundingRate: str
    indexPrice: str
    markPrice: str
    nextFundingTimestamp: int
    symbol: str


class OpenInterest(BaseModel):
    symbol: str
    openInterest: str = None
    timestamp: int


class FundingRate(BaseModel):
    symbol: str
    intervalEndTimestamp: str
    fundingRate: str


class SystemStatus(BaseModel):
    status: str
    message: Optional[str] = None


class Trade(BaseModel):
    id: Optional[int] = None
    price: str
    quantity: str
    quoteQuantity: str
    timestamp: int
    isBuyerMaker: bool


class Balance(BaseModel):
    available: str
    locked: str
    staked: str


class Balances(RootModel):
    root: Dict[str, Balance]


class CollateralAsset(BaseModel):
    symbol: str
    assetMarkPrice: str
    totalQuantity: str
    balanceNotional: str
    collateralWeight: str
    collateralValue: str
    openOrderQuantity: str
    lendQuantity: str
    availableQuantity: str
    imf: str
    unsettledEquity: str


class CollateralInfo(BaseModel):
    symbol: str
    imfFunction: CollateralFunction
    mmfFunction: CollateralFunction
    haircutFunction: HaircutFunction


class Deposit(BaseModel):
    id: int
    toAddress: str = None
    fromAddress: str = None
    confirmationBlockNumber: int = None
    source: str
    status: str
    transactionHash: str = None
    symbol: str
    quantity: str
    createdAt: str


class DepositAddress(BaseModel):
    address: str


class Withdrawal(BaseModel):
    id: int
    blockchain: str
    clientId: str = None
    identifier: str = None
    quantity: str
    fee: str
    symbol: str
    status: str
    subaccountId: int = None
    toAddress: str
    transactionHash: str = None
    createdAt: str
    isInternal: bool


class BorrowHistory(BaseModel):
    eventType: str
    positionId: str
    positionQuantity: str = None
    quantity: str
    source: str
    symbol: str
    timestamp: str
    spotMarginOrderId: str = None


class InterestHistory(BaseModel):
    paymentType: str
    interestRate: str
    interval: int
    marketSymbol: str
    positionId: str
    quantity: str
    symbol: str
    timestamp: str


class BorrowPosition(BaseModel):
    positionId: str
    quantity: str
    symbol: str
    source: str
    cumulativeInterest: str
    avgInterestRate: str
    side: str
    createdAt: str


class Fill(BaseModel):
    fee: str
    feeSymbol: str
    isMaker: bool
    orderId: str
    price: str
    quantity: str
    side: str
    symbol: str
    systemOrderType: str = None
    timestamp: str
    tradeId: int = None


class FundingPayment(BaseModel):
    userId: int
    subaccountId: int = None
    symbol: str
    quantity: str
    intervalEndTimestamp: str
    fundingRate: str


class OrderHistory(BaseModel):
    id: str
    executedQuantity: str = None
    executedQuoteQuantity: str = None
    expiryReason: str = None
    orderType: str
    postOnly: bool = None
    price: str = None
    quantity: str = None
    quoteQuantity: str = None
    selfTradePrevention: str
    status: str
    side: str
    symbol: str
    timeInForce: str
    triggerPrice: str = None


class PnlHistory(BaseModel):
    pnlRealized: str
    symbol: str
    timestamp: str


class Settlement(BaseModel):
    quantity: str
    source: str
    subaccountId: int = None
    timestamp: str
    userId: int


class Order(BaseModel):
    orderType: str
    id: str
    clientId: int = None
    createdAt: int
    executedQuantity: str
    executedQuoteQuantity: str
    quantity: str = None
    quoteQuantity: str = None
    timeInForce: str
    selfTradePrevention: str
    side: str
    status: str
    symbol: str
    triggerPrice: str = None
