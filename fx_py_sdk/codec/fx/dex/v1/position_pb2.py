# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/position.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/v1/position.proto',
  package='fx.dex.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/marginxio/marginx/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x66x/dex/v1/position.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\"Q\n\x11TotalPositionSize\x12<\n\x04size\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"I\n\nPositionID\x12;\n\x02id\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"@\n\x0bPositionIDs\x12\x31\n\x0cposition_ids\x18\x01 \x03(\x0b\x32\x15.fx.dex.v1.PositionIDB\x04\xc8\xde\x1f\x00\"\xd8\x06\n\x08Position\x12;\n\x02id\x18\x01 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\x12@\n\x05owner\x18\x02 \x01(\x0c\x42\x31\xfa\xde\x1f-github.com/cosmos/cosmos-sdk/types.AccAddress\x12\x0f\n\x07pair_id\x18\x03 \x01(\t\x12*\n\tdirection\x18\x04 \x01(\x0e\x32\x17.fx.dex.v1.PosDirection\x12\x43\n\x0b\x65ntry_price\x18\x05 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x42\n\nmark_price\x18\x06 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12I\n\x11liquidation_price\x18\x07 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x45\n\rbase_quantity\x18\x08 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12>\n\x06margin\x18\t \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x10\n\x08leverage\x18\n \x01(\x03\x12\x46\n\x0eunrealized_pnl\x18\x0b \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x43\n\x0bmargin_rate\x18\x0c \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x46\n\x0einitial_margin\x18\r \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12N\n\x16pending_order_quantity\x18\x0e \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"9\n\tPositions\x12,\n\tpositions\x18\x01 \x03(\x0b\x32\x13.fx.dex.v1.PositionB\x04\xc8\xde\x1f\x00*f\n\x0cPosDirection\x12\"\n\x0cPOSITIONBOTH\x10\x00\x1a\x10\x8a\x9d \x0cPOSITIONBOTH\x12\x12\n\x04LONG\x10\x01\x1a\x08\x8a\x9d \x04LONG\x12\x14\n\x05SHORT\x10\x02\x1a\t\x8a\x9d \x05SHORT\x1a\x08\xa8\xa4\x1e\x01\x88\xa3\x1e\x00\x42*Z(github.com/marginxio/marginx/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])

_POSDIRECTION = _descriptor.EnumDescriptor(
  name='PosDirection',
  full_name='fx.dex.v1.PosDirection',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POSITIONBOTH', index=0, number=0,
      serialized_options=b'\212\235 \014POSITIONBOTH',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LONG', index=1, number=1,
      serialized_options=b'\212\235 \004LONG',
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHORT', index=2, number=2,
      serialized_options=b'\212\235 \005SHORT',
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\250\244\036\001\210\243\036\000',
  serialized_start=1203,
  serialized_end=1305,
)
_sym_db.RegisterEnumDescriptor(_POSDIRECTION)

PosDirection = enum_type_wrapper.EnumTypeWrapper(_POSDIRECTION)
POSITIONBOTH = 0
LONG = 1
SHORT = 2



_TOTALPOSITIONSIZE = _descriptor.Descriptor(
  name='TotalPositionSize',
  full_name='fx.dex.v1.TotalPositionSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='fx.dex.v1.TotalPositionSize.size', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=61,
  serialized_end=142,
)


_POSITIONID = _descriptor.Descriptor(
  name='PositionID',
  full_name='fx.dex.v1.PositionID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fx.dex.v1.PositionID.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=144,
  serialized_end=217,
)


_POSITIONIDS = _descriptor.Descriptor(
  name='PositionIDs',
  full_name='fx.dex.v1.PositionIDs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position_ids', full_name='fx.dex.v1.PositionIDs.position_ids', index=0,
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
  serialized_start=219,
  serialized_end=283,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='fx.dex.v1.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='fx.dex.v1.Position.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037\'github.com/cosmos/cosmos-sdk/types.Uint\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='fx.dex.v1.Position.owner', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\336\037-github.com/cosmos/cosmos-sdk/types.AccAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.v1.Position.pair_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='fx.dex.v1.Position.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entry_price', full_name='fx.dex.v1.Position.entry_price', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mark_price', full_name='fx.dex.v1.Position.mark_price', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='liquidation_price', full_name='fx.dex.v1.Position.liquidation_price', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_quantity', full_name='fx.dex.v1.Position.base_quantity', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin', full_name='fx.dex.v1.Position.margin', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leverage', full_name='fx.dex.v1.Position.leverage', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unrealized_pnl', full_name='fx.dex.v1.Position.unrealized_pnl', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin_rate', full_name='fx.dex.v1.Position.margin_rate', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_margin', full_name='fx.dex.v1.Position.initial_margin', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_order_quantity', full_name='fx.dex.v1.Position.pending_order_quantity', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=286,
  serialized_end=1142,
)


_POSITIONS = _descriptor.Descriptor(
  name='Positions',
  full_name='fx.dex.v1.Positions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='positions', full_name='fx.dex.v1.Positions.positions', index=0,
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
  serialized_start=1144,
  serialized_end=1201,
)

_POSITIONIDS.fields_by_name['position_ids'].message_type = _POSITIONID
_POSITION.fields_by_name['direction'].enum_type = _POSDIRECTION
_POSITIONS.fields_by_name['positions'].message_type = _POSITION
DESCRIPTOR.message_types_by_name['TotalPositionSize'] = _TOTALPOSITIONSIZE
DESCRIPTOR.message_types_by_name['PositionID'] = _POSITIONID
DESCRIPTOR.message_types_by_name['PositionIDs'] = _POSITIONIDS
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Positions'] = _POSITIONS
DESCRIPTOR.enum_types_by_name['PosDirection'] = _POSDIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TotalPositionSize = _reflection.GeneratedProtocolMessageType('TotalPositionSize', (_message.Message,), {
  'DESCRIPTOR' : _TOTALPOSITIONSIZE,
  '__module__' : 'fx.dex.v1.position_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.TotalPositionSize)
  })
_sym_db.RegisterMessage(TotalPositionSize)

PositionID = _reflection.GeneratedProtocolMessageType('PositionID', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONID,
  '__module__' : 'fx.dex.v1.position_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.PositionID)
  })
_sym_db.RegisterMessage(PositionID)

PositionIDs = _reflection.GeneratedProtocolMessageType('PositionIDs', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONIDS,
  '__module__' : 'fx.dex.v1.position_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.PositionIDs)
  })
_sym_db.RegisterMessage(PositionIDs)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'fx.dex.v1.position_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Position)
  })
_sym_db.RegisterMessage(Position)

Positions = _reflection.GeneratedProtocolMessageType('Positions', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONS,
  '__module__' : 'fx.dex.v1.position_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Positions)
  })
_sym_db.RegisterMessage(Positions)


DESCRIPTOR._options = None
_POSDIRECTION._options = None
_POSDIRECTION.values_by_name["POSITIONBOTH"]._options = None
_POSDIRECTION.values_by_name["LONG"]._options = None
_POSDIRECTION.values_by_name["SHORT"]._options = None
_TOTALPOSITIONSIZE.fields_by_name['size']._options = None
_POSITIONID.fields_by_name['id']._options = None
_POSITIONIDS.fields_by_name['position_ids']._options = None
_POSITION.fields_by_name['id']._options = None
_POSITION.fields_by_name['owner']._options = None
_POSITION.fields_by_name['entry_price']._options = None
_POSITION.fields_by_name['mark_price']._options = None
_POSITION.fields_by_name['liquidation_price']._options = None
_POSITION.fields_by_name['base_quantity']._options = None
_POSITION.fields_by_name['margin']._options = None
_POSITION.fields_by_name['unrealized_pnl']._options = None
_POSITION.fields_by_name['margin_rate']._options = None
_POSITION.fields_by_name['initial_margin']._options = None
_POSITION.fields_by_name['pending_order_quantity']._options = None
_POSITIONS.fields_by_name['positions']._options = None
# @@protoc_insertion_point(module_scope)
