from typing import NamedTuple

class Order(NamedTuple):
    TxHash: str
    Id: str
    Owner: str
    PairId: str
    Direction: str
    Price: float
    BaseQuantity: float
    QuoteQuantity: float
    FilledQuantity: float
    FilledAvgPrice: float
    RemainLocked: float
    Leverage: int
    Status: str
    OrderType: str
    CostFee: float
    LockedFee: float
    Ttl: int

class Position(NamedTuple):
    Id: int
    Owner: str
    PairId: str
    Direction: str
    EntryPrice: float
    MarkPrice: float
    LiquidationPrice: float
    BaseQuantity: float
    Margin: float
    Leverage: int
    UnrealizedPnl: float
    MarginRate: float
    InitialMargin: float
    PendingOrderQuantity: float

