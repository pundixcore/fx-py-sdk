# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.fx.dex import order_pb2 as fx_dot_dex_dot_order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/tx.proto',
  package='fx.dex',
  syntax='proto3',
  serialized_options=b'Z1git.wokoworks.com/blockchain/fx-chain/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x66x/dex/tx.proto\x12\x06\x66x.dex\x1a\x14gogoproto/gogo.proto\x1a\x12\x66x/dex/order.proto\"\xa1\x02\n\x0eMsgCreateOrder\x12@\n\x05owner\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x02 \x01(\t\x12$\n\tdirection\x18\x03 \x01(\x0e\x32\x11.fx.dex.Direction\x12=\n\x05price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rbase_quantity\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x10\n\x08leverage\x18\x06 \x01(\x03\"*\n\x16MsgCreateOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\"d\n\x0eMsgCancelOrder\x12@\n\x05owner\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x10\n\x08order_id\x18\x02 \x01(\t\"\x18\n\x16MsgCancelOrderResponse\"\xe7\x01\n\x0cMsgAddMargin\x12@\n\x05owner\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x02 \x01(\t\x12\x44\n\x0bposition_id\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12>\n\x06margin\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x12\n\x10MsgAddMarginResp\"\xea\x01\n\x0fMsgReduceMargin\x12@\n\x05owner\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x02 \x01(\t\x12\x44\n\x0bposition_id\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12>\n\x06margin\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x12\n\x10ReduceMarginResp\"\xc5\x02\n\x10MsgClosePosition\x12@\n\x05owner\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x02 \x01(\t\x12\x44\n\x0bposition_id\x18\x03 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12=\n\x05price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rbase_quantity\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x12\n\nfull_close\x18\x06 \x01(\x08\"\x16\n\x14MsgClosePositionResp\"\xa5\x01\n\x16MsgLiquidationPosition\x12\x45\n\nliquidator\x18\x01 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x44\n\x0bposition_id\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"\x1c\n\x1aMsgLiquidationPositionResp\"\x96\x01\n\x14MsgCreatePairRequest\x12\x12\n\nbase_asset\x18\x01 \x01(\t\x12\x13\n\x0bquote_asset\x18\x02 \x01(\t\x12\x11\n\tvalidator\x18\x03 \x01(\t\x12\x42\n\ninit_price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x17\n\x15MsgCreatePairResponse2\x82\x04\n\x03Msg\x12\x45\n\x0b\x43reateOrder\x12\x16.fx.dex.MsgCreateOrder\x1a\x1e.fx.dex.MsgCreateOrderResponse\x12\x45\n\x0b\x43\x61ncelOrder\x12\x16.fx.dex.MsgCancelOrder\x1a\x1e.fx.dex.MsgCancelOrderResponse\x12;\n\tAddMargin\x12\x14.fx.dex.MsgAddMargin\x1a\x18.fx.dex.MsgAddMarginResp\x12\x41\n\x0cReduceMargin\x12\x17.fx.dex.MsgReduceMargin\x1a\x18.fx.dex.ReduceMarginResp\x12G\n\rClosePosition\x12\x18.fx.dex.MsgClosePosition\x1a\x1c.fx.dex.MsgClosePositionResp\x12Y\n\x13LiquidationPosition\x12\x1e.fx.dex.MsgLiquidationPosition\x1a\".fx.dex.MsgLiquidationPositionResp\x12I\n\nCreatePair\x12\x1c.fx.dex.MsgCreatePairRequest\x1a\x1d.fx.dex.MsgCreatePairResponseB3Z1git.wokoworks.com/blockchain/fx-chain/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,fx_dot_dex_dot_order__pb2.DESCRIPTOR,])




_MSGCREATEORDER = _descriptor.Descriptor(
  name='MsgCreateOrder',
  full_name='fx.dex.MsgCreateOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.MsgCreateOrder.owner', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.MsgCreateOrder.pair_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='fx.dex.MsgCreateOrder.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='fx.dex.MsgCreateOrder.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_quantity', full_name='fx.dex.MsgCreateOrder.base_quantity', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leverage', full_name='fx.dex.MsgCreateOrder.leverage', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=70,
  serialized_end=359,
)


_MSGCREATEORDERRESPONSE = _descriptor.Descriptor(
  name='MsgCreateOrderResponse',
  full_name='fx.dex.MsgCreateOrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='fx.dex.MsgCreateOrderResponse.order_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=361,
  serialized_end=403,
)


_MSGCANCELORDER = _descriptor.Descriptor(
  name='MsgCancelOrder',
  full_name='fx.dex.MsgCancelOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.MsgCancelOrder.owner', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='fx.dex.MsgCancelOrder.order_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=405,
  serialized_end=505,
)


_MSGCANCELORDERRESPONSE = _descriptor.Descriptor(
  name='MsgCancelOrderResponse',
  full_name='fx.dex.MsgCancelOrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=507,
  serialized_end=531,
)


_MSGADDMARGIN = _descriptor.Descriptor(
  name='MsgAddMargin',
  full_name='fx.dex.MsgAddMargin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.MsgAddMargin.owner', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.MsgAddMargin.pair_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position_id', full_name='fx.dex.MsgAddMargin.position_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin', full_name='fx.dex.MsgAddMargin.margin', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=534,
  serialized_end=765,
)


_MSGADDMARGINRESP = _descriptor.Descriptor(
  name='MsgAddMarginResp',
  full_name='fx.dex.MsgAddMarginResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=767,
  serialized_end=785,
)


_MSGREDUCEMARGIN = _descriptor.Descriptor(
  name='MsgReduceMargin',
  full_name='fx.dex.MsgReduceMargin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.MsgReduceMargin.owner', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.MsgReduceMargin.pair_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position_id', full_name='fx.dex.MsgReduceMargin.position_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin', full_name='fx.dex.MsgReduceMargin.margin', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=788,
  serialized_end=1022,
)


_REDUCEMARGINRESP = _descriptor.Descriptor(
  name='ReduceMarginResp',
  full_name='fx.dex.ReduceMarginResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1024,
  serialized_end=1042,
)


_MSGCLOSEPOSITION = _descriptor.Descriptor(
  name='MsgClosePosition',
  full_name='fx.dex.MsgClosePosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.MsgClosePosition.owner', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.MsgClosePosition.pair_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position_id', full_name='fx.dex.MsgClosePosition.position_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='fx.dex.MsgClosePosition.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_quantity', full_name='fx.dex.MsgClosePosition.base_quantity', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_close', full_name='fx.dex.MsgClosePosition.full_close', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1045,
  serialized_end=1370,
)


_MSGCLOSEPOSITIONRESP = _descriptor.Descriptor(
  name='MsgClosePositionResp',
  full_name='fx.dex.MsgClosePositionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1372,
  serialized_end=1394,
)


_MSGLIQUIDATIONPOSITION = _descriptor.Descriptor(
  name='MsgLiquidationPosition',
  full_name='fx.dex.MsgLiquidationPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='liquidator', full_name='fx.dex.MsgLiquidationPosition.liquidator', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position_id', full_name='fx.dex.MsgLiquidationPosition.position_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1397,
  serialized_end=1562,
)


_MSGLIQUIDATIONPOSITIONRESP = _descriptor.Descriptor(
  name='MsgLiquidationPositionResp',
  full_name='fx.dex.MsgLiquidationPositionResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1564,
  serialized_end=1592,
)


_MSGCREATEPAIRREQUEST = _descriptor.Descriptor(
  name='MsgCreatePairRequest',
  full_name='fx.dex.MsgCreatePairRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_asset', full_name='fx.dex.MsgCreatePairRequest.base_asset', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote_asset', full_name='fx.dex.MsgCreatePairRequest.quote_asset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validator', full_name='fx.dex.MsgCreatePairRequest.validator', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_price', full_name='fx.dex.MsgCreatePairRequest.init_price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1595,
  serialized_end=1745,
)


_MSGCREATEPAIRRESPONSE = _descriptor.Descriptor(
  name='MsgCreatePairResponse',
  full_name='fx.dex.MsgCreatePairResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1747,
  serialized_end=1770,
)

_MSGCREATEORDER.fields_by_name['direction'].enum_type = fx_dot_dex_dot_order__pb2._DIRECTION
DESCRIPTOR.message_types_by_name['MsgCreateOrder'] = _MSGCREATEORDER
DESCRIPTOR.message_types_by_name['MsgCreateOrderResponse'] = _MSGCREATEORDERRESPONSE
DESCRIPTOR.message_types_by_name['MsgCancelOrder'] = _MSGCANCELORDER
DESCRIPTOR.message_types_by_name['MsgCancelOrderResponse'] = _MSGCANCELORDERRESPONSE
DESCRIPTOR.message_types_by_name['MsgAddMargin'] = _MSGADDMARGIN
DESCRIPTOR.message_types_by_name['MsgAddMarginResp'] = _MSGADDMARGINRESP
DESCRIPTOR.message_types_by_name['MsgReduceMargin'] = _MSGREDUCEMARGIN
DESCRIPTOR.message_types_by_name['ReduceMarginResp'] = _REDUCEMARGINRESP
DESCRIPTOR.message_types_by_name['MsgClosePosition'] = _MSGCLOSEPOSITION
DESCRIPTOR.message_types_by_name['MsgClosePositionResp'] = _MSGCLOSEPOSITIONRESP
DESCRIPTOR.message_types_by_name['MsgLiquidationPosition'] = _MSGLIQUIDATIONPOSITION
DESCRIPTOR.message_types_by_name['MsgLiquidationPositionResp'] = _MSGLIQUIDATIONPOSITIONRESP
DESCRIPTOR.message_types_by_name['MsgCreatePairRequest'] = _MSGCREATEPAIRREQUEST
DESCRIPTOR.message_types_by_name['MsgCreatePairResponse'] = _MSGCREATEPAIRRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgCreateOrder = _reflection.GeneratedProtocolMessageType('MsgCreateOrder', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEORDER,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCreateOrder)
  })
_sym_db.RegisterMessage(MsgCreateOrder)

MsgCreateOrderResponse = _reflection.GeneratedProtocolMessageType('MsgCreateOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEORDERRESPONSE,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCreateOrderResponse)
  })
_sym_db.RegisterMessage(MsgCreateOrderResponse)

MsgCancelOrder = _reflection.GeneratedProtocolMessageType('MsgCancelOrder', (_message.Message,), {
  'DESCRIPTOR' : _MSGCANCELORDER,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCancelOrder)
  })
_sym_db.RegisterMessage(MsgCancelOrder)

MsgCancelOrderResponse = _reflection.GeneratedProtocolMessageType('MsgCancelOrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCANCELORDERRESPONSE,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCancelOrderResponse)
  })
_sym_db.RegisterMessage(MsgCancelOrderResponse)

MsgAddMargin = _reflection.GeneratedProtocolMessageType('MsgAddMargin', (_message.Message,), {
  'DESCRIPTOR' : _MSGADDMARGIN,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgAddMargin)
  })
_sym_db.RegisterMessage(MsgAddMargin)

MsgAddMarginResp = _reflection.GeneratedProtocolMessageType('MsgAddMarginResp', (_message.Message,), {
  'DESCRIPTOR' : _MSGADDMARGINRESP,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgAddMarginResp)
  })
_sym_db.RegisterMessage(MsgAddMarginResp)

MsgReduceMargin = _reflection.GeneratedProtocolMessageType('MsgReduceMargin', (_message.Message,), {
  'DESCRIPTOR' : _MSGREDUCEMARGIN,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgReduceMargin)
  })
_sym_db.RegisterMessage(MsgReduceMargin)

ReduceMarginResp = _reflection.GeneratedProtocolMessageType('ReduceMarginResp', (_message.Message,), {
  'DESCRIPTOR' : _REDUCEMARGINRESP,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.ReduceMarginResp)
  })
_sym_db.RegisterMessage(ReduceMarginResp)

MsgClosePosition = _reflection.GeneratedProtocolMessageType('MsgClosePosition', (_message.Message,), {
  'DESCRIPTOR' : _MSGCLOSEPOSITION,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgClosePosition)
  })
_sym_db.RegisterMessage(MsgClosePosition)

MsgClosePositionResp = _reflection.GeneratedProtocolMessageType('MsgClosePositionResp', (_message.Message,), {
  'DESCRIPTOR' : _MSGCLOSEPOSITIONRESP,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgClosePositionResp)
  })
_sym_db.RegisterMessage(MsgClosePositionResp)

MsgLiquidationPosition = _reflection.GeneratedProtocolMessageType('MsgLiquidationPosition', (_message.Message,), {
  'DESCRIPTOR' : _MSGLIQUIDATIONPOSITION,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgLiquidationPosition)
  })
_sym_db.RegisterMessage(MsgLiquidationPosition)

MsgLiquidationPositionResp = _reflection.GeneratedProtocolMessageType('MsgLiquidationPositionResp', (_message.Message,), {
  'DESCRIPTOR' : _MSGLIQUIDATIONPOSITIONRESP,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgLiquidationPositionResp)
  })
_sym_db.RegisterMessage(MsgLiquidationPositionResp)

MsgCreatePairRequest = _reflection.GeneratedProtocolMessageType('MsgCreatePairRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEPAIRREQUEST,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCreatePairRequest)
  })
_sym_db.RegisterMessage(MsgCreatePairRequest)

MsgCreatePairResponse = _reflection.GeneratedProtocolMessageType('MsgCreatePairResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCREATEPAIRRESPONSE,
  '__module__' : 'fx.dex.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.MsgCreatePairResponse)
  })
_sym_db.RegisterMessage(MsgCreatePairResponse)


DESCRIPTOR._options = None
_MSGCREATEORDER.fields_by_name['owner']._options = None
_MSGCREATEORDER.fields_by_name['price']._options = None
_MSGCREATEORDER.fields_by_name['base_quantity']._options = None
_MSGCANCELORDER.fields_by_name['owner']._options = None
_MSGADDMARGIN.fields_by_name['owner']._options = None
_MSGADDMARGIN.fields_by_name['position_id']._options = None
_MSGADDMARGIN.fields_by_name['margin']._options = None
_MSGREDUCEMARGIN.fields_by_name['owner']._options = None
_MSGREDUCEMARGIN.fields_by_name['position_id']._options = None
_MSGREDUCEMARGIN.fields_by_name['margin']._options = None
_MSGCLOSEPOSITION.fields_by_name['owner']._options = None
_MSGCLOSEPOSITION.fields_by_name['position_id']._options = None
_MSGCLOSEPOSITION.fields_by_name['price']._options = None
_MSGCLOSEPOSITION.fields_by_name['base_quantity']._options = None
_MSGLIQUIDATIONPOSITION.fields_by_name['liquidator']._options = None
_MSGLIQUIDATIONPOSITION.fields_by_name['position_id']._options = None
_MSGCREATEPAIRREQUEST.fields_by_name['init_price']._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='fx.dex.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1773,
  serialized_end=2287,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOrder',
    full_name='fx.dex.Msg.CreateOrder',
    index=0,
    containing_service=None,
    input_type=_MSGCREATEORDER,
    output_type=_MSGCREATEORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CancelOrder',
    full_name='fx.dex.Msg.CancelOrder',
    index=1,
    containing_service=None,
    input_type=_MSGCANCELORDER,
    output_type=_MSGCANCELORDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddMargin',
    full_name='fx.dex.Msg.AddMargin',
    index=2,
    containing_service=None,
    input_type=_MSGADDMARGIN,
    output_type=_MSGADDMARGINRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReduceMargin',
    full_name='fx.dex.Msg.ReduceMargin',
    index=3,
    containing_service=None,
    input_type=_MSGREDUCEMARGIN,
    output_type=_REDUCEMARGINRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClosePosition',
    full_name='fx.dex.Msg.ClosePosition',
    index=4,
    containing_service=None,
    input_type=_MSGCLOSEPOSITION,
    output_type=_MSGCLOSEPOSITIONRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LiquidationPosition',
    full_name='fx.dex.Msg.LiquidationPosition',
    index=5,
    containing_service=None,
    input_type=_MSGLIQUIDATIONPOSITION,
    output_type=_MSGLIQUIDATIONPOSITIONRESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreatePair',
    full_name='fx.dex.Msg.CreatePair',
    index=6,
    containing_service=None,
    input_type=_MSGCREATEPAIRREQUEST,
    output_type=_MSGCREATEPAIRRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
