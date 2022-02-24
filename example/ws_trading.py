#!/usr/bin/env python
# coding='uft8'

from fx_py_sdk.model.model import Order, Trade
from fx_py_sdk.scan import WebsocketScan, tm_event_NewBlock
from fx_py_sdk.scan_block import TradingScanBlock

class CustomScanBlock(TradingScanBlock):
    def on_order_fill(self, order: Order, trade: Trade, block_height: int):
        if order.order_type=='ORDER_TYPE_OPEN_POSITION' and trade.owner=='dex179q82e7fcck4ftfvf4vfpwkg86jmxf7upext3v':
            print(f'Order filled: {order.order_id} ({order.direction}), Filled qty: {trade.matched_quantity:.3f}, Block height: {block_height}')

    def on_order_cancel(self, order: Order, block_height: int):
        print(f'Order cancelled: {order.order_id}, Block height: {block_height}')

if __name__ == "__main__":
    ws_scan = WebsocketScan(subscribe_events=[tm_event_NewBlock],
                            scan=CustomScanBlock())
    