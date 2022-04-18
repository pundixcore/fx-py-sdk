# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/params.proto',
  package='fx.dex',
  syntax='proto3',
  serialized_options=b'Z1git.wokoworks.com/blockchain/fx-chain/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x66x/dex/params.proto\x12\x06\x66x.dex\x1a\x14gogoproto/gogo.proto\"\xd5\x01\n\x06Params\x12@\n\x08\x66\x65\x65_rate\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12/\n\'force_liquidation_margin_rate_threshold\x18\x02 \x01(\x03\x12\x1b\n\x13order_expire_blocks\x18\x03 \x01(\x03\x12\x1b\n\x13max_deals_per_block\x18\x04 \x01(\x03\x12\x1e\n\x16max_orders_per_account\x18\x05 \x01(\x03\"\xdf\x01\n\x07Reserve\x12H\n\x10\x61\x63\x63umulative_fee\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0crisk_reserve\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x44\n\x0clocked_funds\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x33Z1git.wokoworks.com/blockchain/fx-chain/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='fx.dex.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fee_rate', full_name='fx.dex.Params.fee_rate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force_liquidation_margin_rate_threshold', full_name='fx.dex.Params.force_liquidation_margin_rate_threshold', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_expire_blocks', full_name='fx.dex.Params.order_expire_blocks', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_deals_per_block', full_name='fx.dex.Params.max_deals_per_block', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_orders_per_account', full_name='fx.dex.Params.max_orders_per_account', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=54,
  serialized_end=267,
)


_RESERVE = _descriptor.Descriptor(
  name='Reserve',
  full_name='fx.dex.Reserve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accumulative_fee', full_name='fx.dex.Reserve.accumulative_fee', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='risk_reserve', full_name='fx.dex.Reserve.risk_reserve', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locked_funds', full_name='fx.dex.Reserve.locked_funds', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=270,
  serialized_end=493,
)

DESCRIPTOR.message_types_by_name['Params'] = _PARAMS
DESCRIPTOR.message_types_by_name['Reserve'] = _RESERVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'fx.dex.params_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.Params)
  })
_sym_db.RegisterMessage(Params)

Reserve = _reflection.GeneratedProtocolMessageType('Reserve', (_message.Message,), {
  'DESCRIPTOR' : _RESERVE,
  '__module__' : 'fx.dex.params_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.Reserve)
  })
_sym_db.RegisterMessage(Reserve)


DESCRIPTOR._options = None
_PARAMS.fields_by_name['fee_rate']._options = None
_RESERVE.fields_by_name['accumulative_fee']._options = None
_RESERVE.fields_by_name['risk_reserve']._options = None
_RESERVE.fields_by_name['locked_funds']._options = None
# @@protoc_insertion_point(module_scope)
