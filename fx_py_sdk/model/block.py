from decimal import Decimal

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
    Attributes = "attributes"
    Key = "key"

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

class EventKeys:
    """orders"""
    tx_hash = "tx_hash"
    order_id = "order_id"
    owner = "owner"
    pair_id = "pair_id"
    direction = "direction"
    price = "price"
    base_quantity = "base_quantity"
    quote_quantity = "quote_quantity"
    filled_quantity = "filled_quantity"
    filled_avg_price = "filled_avg_price"
    remain_locked = "remain_locked"
    created_at = "created_at"
    leverage = "leverage"
    status = "status"
    order_type = "order_type"
    cost_fee = "cost_fee"
    locked_fee = "locked_fee"

    """positions"""
    id = "id"
    position_id = "position_id"
    margin = "margin"
    mark_price = "mark_price"
    entry_price = "entry_price"
    liquidation_price = "liquidation_price"
    margin_rate = "margin_rate"
    deal_price = "deal_price"
    unrealized_pnl = "unrealized_pnl"
    initial_margin = "initial_margin"
    pending_order_quantity = "pending_order_quantity"

    matched_quantity = "matched_quantity"
    unfilled_quantity = "unfilled_quantity"


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

