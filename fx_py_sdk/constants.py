from typing import NamedTuple
from decimal import Decimal

class Order(NamedTuple):
    TxHash: str
    Id: str
    Owner: str
    PairId: str
    Direction: str
    Price: Decimal
    BaseQuantity: Decimal
    QuoteQuantity: Decimal
    FilledQuantity: Decimal
    FilledAvgPrice: Decimal
    RemainLocked: Decimal
    Leverage: int
    Status: str
    OrderType: str
    CostFee: Decimal
    LockedFee: Decimal
    Created_at: str
    Ttl: int

class Position(NamedTuple):
    Id: int
    Owner: str
    PairId: str
    Direction: str
    EntryPrice: Decimal
    MarkPrice: Decimal
    LiquidationPrice: Decimal
    BaseQuantity: Decimal
    Margin: Decimal
    Leverage: int
    UnrealizedPnl: Decimal
    MarginRate: Decimal
    InitialMargin: Decimal
    PendingOrderQuantity: Decimal

class BackEndApi:
    query_order_page = "http://44.195.213.51:30225/api/address/queryOrderPage"