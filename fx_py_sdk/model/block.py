
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

