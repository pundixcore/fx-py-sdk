
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
    TxResult = "TxResult"

class EventTypes:
    # EndBlock
    Add_position = "dex.add_position"
    Order_fill = "dex.order_fill"
    New_position = "fx.dex.Position"
    Part_close_position = "dex.part_close_position"
    Full_close_position = "dex.full_close_position"
    Cancel_order_expire = "dex.cancel_order" # expire block
    Cancel_order_partial_order = "dex.cancel_order" # will not happen from 2021/12/21

    # BeginBlock
    Forced_liquidation_position = "dex.forced_liquidation_position"
    Liq_cancel_order = "dex.liq_cancel_order"
    Liquidation_position_order = "dex.liquidation_position_order"

    # Tx event
    Order = "fx.dex.Order"
    Cancel_order = "dex.cancel_order"
    Close_position_order = "dex.close_position_order"


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

