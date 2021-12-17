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


class BlockResponse:
    RESULT = "result"
    DATA = "data"
    VALUE = "value"
    BLOCK = "block"
    HEADER = "header"
    HEIGHT = "height"
    EVENTS = "events"
    RESULT_BEGIN_BLOCK = "result_begin_block"
    RESULT_END_BLOCK = "result_end_block"
    TYPE = "type"

class BlockResponseValue:
    DEX_ORDER_FILL = "dex.order_fill"
    BID = "BID"
    ASK = "ASK"

class OrderFilledFields:
    PRICE = "price"
    BASE_QUANTITY = "base_quantity"
    CREATED_AT = "created_at"
    LOCKED_FEE = "locked_fee"
    MATCHED_QUANTITY = "matched_quantity"
    PAIR_ID = "pair_id"
    DIRECTION = "direction"
    QUOTE_QUANTITY = "quote_quantity"
    ORDER_TYPE = "order_type"
    OWNER = "owner"
    DEAL_PRICE = "deal_price"
    UNFILLED_QUANTITY = "unfilled_quantity"
    STATUS = "status"
    TX_HASH = "tx_hash"
    FILLED_QUANTITY = "filled_quantity"
    COST_FEE = "cost_fee"
    LEVERAGE = "leverage"
    ORDER_ID = "order_id"
    FILLED_AVERAGE_PRICE = "filled_avg_price"
    TTL = "ttl"
