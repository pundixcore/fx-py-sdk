# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/order.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/v1/order.proto',
  package='fx.dex.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/marginxio/marginx/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x66x/dex/v1/order.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x17\n\x08OrderIDs\x12\x0b\n\x03ids\x18\x01 \x03(\t\"\xa3\x06\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x05owner\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x03 \x01(\t\x12\'\n\tdirection\x18\x04 \x01(\x0e\x32\x14.fx.dex.v1.Direction\x12=\n\x05price\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rbase_quantity\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x46\n\x0equote_quantity\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12G\n\x0f\x66illed_quantity\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12H\n\x10\x66illed_avg_price\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rremain_locked\x18\n \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x10\n\x08leverage\x18\x0b \x01(\x03\x12&\n\x06status\x18\x0c \x01(\x0e\x32\x16.fx.dex.v1.OrderStatus\x12(\n\norder_type\x18\r \x01(\x0e\x32\x14.fx.dex.v1.OrderType\x12\x41\n\x08\x63ost_fee\x18\x0e \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\x12\x43\n\nlocked_fee\x18\x0f \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\xc8\xde\x1f\x00\"0\n\x06Orders\x12&\n\x06orders\x18\x01 \x03(\x0b\x32\x10.fx.dex.v1.OrderB\x04\xc8\xde\x1f\x00*\x8d\x01\n\tDirection\x12\x12\n\x04\x42OTH\x10\x00\x1a\x08\x8a\x9d \x04\x42OTH\x12\x10\n\x03\x42UY\x10\x01\x1a\x07\x8a\x9d \x03\x42UY\x12\x12\n\x04SELL\x10\x02\x1a\x08\x8a\x9d \x04SELL\x12\x1c\n\tMarketBuy\x10\x03\x1a\r\x8a\x9d \tMarketBuy\x12\x1e\n\nMarketSell\x10\x04\x1a\x0e\x8a\x9d \nMarketSell\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00*\xc3\x03\n\x0bOrderStatus\x12$\n\rORDER_PENDING\x10\x00\x1a\x11\x8a\x9d \rORDER_PENDING\x12\"\n\x0cORDER_FILLED\x10\x01\x1a\x10\x8a\x9d \x0cORDER_FILLED\x12\x32\n\x14ORDER_PARTIAL_FILLED\x10\x02\x1a\x18\x8a\x9d \x14ORDER_PARTIAL_FILLED\x12(\n\x0fORDER_CANCELLED\x10\x03\x1a\x13\x8a\x9d \x0fORDER_CANCELLED\x12\x46\n\x1eORDER_PARTIAL_FILLED_CANCELLED\x10\x04\x1a\"\x8a\x9d \x1eORDER_PARTIAL_FILLED_CANCELLED\x12\x42\n\x1cORDER_PARTIAL_FILLED_EXPIRED\x10\x05\x1a \x8a\x9d \x1cORDER_PARTIAL_FILLED_EXPIRED\x12$\n\rORDER_EXPIRED\x10\x06\x1a\x11\x8a\x9d \rORDER_EXPIRED\x12\"\n\x0cORDER_GASOUT\x10\x07\x1a\x10\x8a\x9d \x0cORDER_GASOUT\x12,\n\x11ORDER_PRICE_LIMIT\x10\x08\x1a\x15\x8a\x9d \x11ORDER_PRICE_LIMIT\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00*\xc7\x01\n\tOrderType\x12:\n\x18ORDER_TYPE_OPEN_POSITION\x10\x00\x1a\x1c\x8a\x9d \x18ORDER_TYPE_OPEN_POSITION\x12<\n\x19ORDER_TYPE_CLOSE_POSITION\x10\x01\x1a\x1d\x8a\x9d \x19ORDER_TYPE_CLOSE_POSITION\x12\x36\n\x16ORDER_TYPE_LIQUIDATION\x10\x02\x1a\x1a\x8a\x9d \x16ORDER_TYPE_LIQUIDATION\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00\x42*Z(github.com/marginxio/marginx/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='fx.dex.v1.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=0, number=0,
      serialized_options=b'\212\235 \004BOTH',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUY', index=1, number=1,
      serialized_options=b'\212\235 \003BUY',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELL', index=2, number=2,
      serialized_options=b'\212\235 \004SELL',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MarketBuy', index=3, number=3,
      serialized_options=b'\212\235 \tMarketBuy',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MarketSell', index=4, number=4,
      serialized_options=b'\212\235 \nMarketSell',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\250\244\036\001\210\243\036\000',
  serialized_start=972,
  serialized_end=1113,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
_ORDERSTATUS = _descriptor.EnumDescriptor(
  name='OrderStatus',
  full_name='fx.dex.v1.OrderStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORDER_PENDING', index=0, number=0,
      serialized_options=b'\212\235 \rORDER_PENDING',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_FILLED', index=1, number=1,
      serialized_options=b'\212\235 \014ORDER_FILLED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PARTIAL_FILLED', index=2, number=2,
      serialized_options=b'\212\235 \024ORDER_PARTIAL_FILLED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_CANCELLED', index=3, number=3,
      serialized_options=b'\212\235 \017ORDER_CANCELLED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PARTIAL_FILLED_CANCELLED', index=4, number=4,
      serialized_options=b'\212\235 \036ORDER_PARTIAL_FILLED_CANCELLED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PARTIAL_FILLED_EXPIRED', index=5, number=5,
      serialized_options=b'\212\235 \034ORDER_PARTIAL_FILLED_EXPIRED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_EXPIRED', index=6, number=6,
      serialized_options=b'\212\235 \rORDER_EXPIRED',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_GASOUT', index=7, number=7,
      serialized_options=b'\212\235 \014ORDER_GASOUT',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PRICE_LIMIT', index=8, number=8,
      serialized_options=b'\212\235 \021ORDER_PRICE_LIMIT',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\250\244\036\001\210\243\036\000',
  serialized_start=1116,
  serialized_end=1567,
)
_sym_db.RegisterEnumDescriptor(_ORDERSTATUS)

OrderStatus = enum_type_wrapper.EnumTypeWrapper(_ORDERSTATUS)
_ORDERTYPE = _descriptor.EnumDescriptor(
  name='OrderType',
  full_name='fx.dex.v1.OrderType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORDER_TYPE_OPEN_POSITION', index=0, number=0,
      serialized_options=b'\212\235 \030ORDER_TYPE_OPEN_POSITION',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_TYPE_CLOSE_POSITION', index=1, number=1,
      serialized_options=b'\212\235 \031ORDER_TYPE_CLOSE_POSITION',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER_TYPE_LIQUIDATION', index=2, number=2,
      serialized_options=b'\212\235 \026ORDER_TYPE_LIQUIDATION',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\250\244\036\001\210\243\036\000',
  serialized_start=1570,
  serialized_end=1769,
)
_sym_db.RegisterEnumDescriptor(_ORDERTYPE)

OrderType = enum_type_wrapper.EnumTypeWrapper(_ORDERTYPE)
BOTH = 0
BUY = 1
SELL = 2
MarketBuy = 3
MarketSell = 4
ORDER_PENDING = 0
ORDER_FILLED = 1
ORDER_PARTIAL_FILLED = 2
ORDER_CANCELLED = 3
ORDER_PARTIAL_FILLED_CANCELLED = 4
ORDER_PARTIAL_FILLED_EXPIRED = 5
ORDER_EXPIRED = 6
ORDER_GASOUT = 7
ORDER_PRICE_LIMIT = 8
ORDER_TYPE_OPEN_POSITION = 0
ORDER_TYPE_CLOSE_POSITION = 1
ORDER_TYPE_LIQUIDATION = 2



_ORDERIDS = _descriptor.Descriptor(
  name='OrderIDs',
  full_name='fx.dex.v1.OrderIDs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='fx.dex.v1.OrderIDs.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=113,
)


_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='fx.dex.v1.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fx.dex.v1.Order.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.v1.Order.owner', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.v1.Order.pair_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='fx.dex.v1.Order.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='fx.dex.v1.Order.price', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_quantity', full_name='fx.dex.v1.Order.base_quantity', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote_quantity', full_name='fx.dex.v1.Order.quote_quantity', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filled_quantity', full_name='fx.dex.v1.Order.filled_quantity', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filled_avg_price', full_name='fx.dex.v1.Order.filled_avg_price', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remain_locked', full_name='fx.dex.v1.Order.remain_locked', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leverage', full_name='fx.dex.v1.Order.leverage', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='fx.dex.v1.Order.status', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_type', full_name='fx.dex.v1.Order.order_type', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost_fee', full_name='fx.dex.v1.Order.cost_fee', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locked_fee', full_name='fx.dex.v1.Order.locked_fee', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=919,
)


_ORDERS = _descriptor.Descriptor(
  name='Orders',
  full_name='fx.dex.v1.Orders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='orders', full_name='fx.dex.v1.Orders.orders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=921,
  serialized_end=969,
)

_ORDER.fields_by_name['direction'].enum_type = _DIRECTION
_ORDER.fields_by_name['status'].enum_type = _ORDERSTATUS
_ORDER.fields_by_name['order_type'].enum_type = _ORDERTYPE
_ORDERS.fields_by_name['orders'].message_type = _ORDER
DESCRIPTOR.message_types_by_name['OrderIDs'] = _ORDERIDS
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['Orders'] = _ORDERS
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
DESCRIPTOR.enum_types_by_name['OrderStatus'] = _ORDERSTATUS
DESCRIPTOR.enum_types_by_name['OrderType'] = _ORDERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderIDs = _reflection.GeneratedProtocolMessageType('OrderIDs', (_message.Message,), {
  'DESCRIPTOR' : _ORDERIDS,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.OrderIDs)
  })
_sym_db.RegisterMessage(OrderIDs)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Order)
  })
_sym_db.RegisterMessage(Order)

Orders = _reflection.GeneratedProtocolMessageType('Orders', (_message.Message,), {
  'DESCRIPTOR' : _ORDERS,
  '__module__' : 'fx.dex.v1.order_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Orders)
  })
_sym_db.RegisterMessage(Orders)


DESCRIPTOR._options = None
_DIRECTION._options = None
_DIRECTION.values_by_name["BOTH"]._options = None
_DIRECTION.values_by_name["BUY"]._options = None
_DIRECTION.values_by_name["SELL"]._options = None
_DIRECTION.values_by_name["MarketBuy"]._options = None
_DIRECTION.values_by_name["MarketSell"]._options = None
_ORDERSTATUS._options = None
_ORDERSTATUS.values_by_name["ORDER_PENDING"]._options = None
_ORDERSTATUS.values_by_name["ORDER_FILLED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_CANCELLED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_CANCELLED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_PARTIAL_FILLED_EXPIRED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_EXPIRED"]._options = None
_ORDERSTATUS.values_by_name["ORDER_GASOUT"]._options = None
_ORDERSTATUS.values_by_name["ORDER_PRICE_LIMIT"]._options = None
_ORDERTYPE._options = None
_ORDERTYPE.values_by_name["ORDER_TYPE_OPEN_POSITION"]._options = None
_ORDERTYPE.values_by_name["ORDER_TYPE_CLOSE_POSITION"]._options = None
_ORDERTYPE.values_by_name["ORDER_TYPE_LIQUIDATION"]._options = None
_ORDER.fields_by_name['owner']._options = None
_ORDER.fields_by_name['price']._options = None
_ORDER.fields_by_name['base_quantity']._options = None
_ORDER.fields_by_name['quote_quantity']._options = None
_ORDER.fields_by_name['filled_quantity']._options = None
_ORDER.fields_by_name['filled_avg_price']._options = None
_ORDER.fields_by_name['remain_locked']._options = None
_ORDER.fields_by_name['cost_fee']._options = None
_ORDER.fields_by_name['locked_fee']._options = None
_ORDERS.fields_by_name['orders']._options = None
# @@protoc_insertion_point(module_scope)
