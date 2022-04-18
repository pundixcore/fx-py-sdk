# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/oracle/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/oracle/tx.proto',
  package='fx.oracle',
  syntax='proto3',
  serialized_options=b'Z4git.wokoworks.com/blockchain/fx-chain/x/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x66x/oracle/tx.proto\x12\tfx.oracle\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x9e\x01\n\x10MsgOracleRequest\x12\x11\n\tvalidator\x18\x01 \x01(\t\x12\x13\n\x0bprepare_gas\x18\x02 \x01(\x04\x12\x13\n\x0b\x65xecute_gas\x18\x03 \x01(\x04\x12\x32\n\tfee_limit\x18\x04 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x19\n\x0bmarket_type\x18\x05 \x01(\tB\x04\xc8\xde\x1f\x01\"\x13\n\x11MsgOracleResponse\"q\n\x0fMsgSubmitAnswer\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0e\n\x06oracle\x18\x02 \x01(\t\x12>\n\x06\x61nswer\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x13\n\x11MsgSubmitResponse2\x9b\x01\n\x03Msg\x12J\n\rOracleRequest\x12\x1b.fx.oracle.MsgOracleRequest\x1a\x1c.fx.oracle.MsgOracleResponse\x12H\n\x0cSubmitAnswer\x12\x1a.fx.oracle.MsgSubmitAnswer\x1a\x1c.fx.oracle.MsgSubmitResponseB6Z4git.wokoworks.com/blockchain/fx-chain/x/oracle/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_MSGORACLEREQUEST = _descriptor.Descriptor(
  name='MsgOracleRequest',
  full_name='fx.oracle.MsgOracleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='validator', full_name='fx.oracle.MsgOracleRequest.validator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prepare_gas', full_name='fx.oracle.MsgOracleRequest.prepare_gas', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execute_gas', full_name='fx.oracle.MsgOracleRequest.execute_gas', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fee_limit', full_name='fx.oracle.MsgOracleRequest.fee_limit', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='market_type', full_name='fx.oracle.MsgOracleRequest.market_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=88,
  serialized_end=246,
)


_MSGORACLERESPONSE = _descriptor.Descriptor(
  name='MsgOracleResponse',
  full_name='fx.oracle.MsgOracleResponse',
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
  serialized_start=248,
  serialized_end=267,
)


_MSGSUBMITANSWER = _descriptor.Descriptor(
  name='MsgSubmitAnswer',
  full_name='fx.oracle.MsgSubmitAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='fx.oracle.MsgSubmitAnswer.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oracle', full_name='fx.oracle.MsgSubmitAnswer.oracle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer', full_name='fx.oracle.MsgSubmitAnswer.answer', index=2,
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
  serialized_start=269,
  serialized_end=382,
)


_MSGSUBMITRESPONSE = _descriptor.Descriptor(
  name='MsgSubmitResponse',
  full_name='fx.oracle.MsgSubmitResponse',
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
  serialized_start=384,
  serialized_end=403,
)

_MSGORACLEREQUEST.fields_by_name['fee_limit'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name['MsgOracleRequest'] = _MSGORACLEREQUEST
DESCRIPTOR.message_types_by_name['MsgOracleResponse'] = _MSGORACLERESPONSE
DESCRIPTOR.message_types_by_name['MsgSubmitAnswer'] = _MSGSUBMITANSWER
DESCRIPTOR.message_types_by_name['MsgSubmitResponse'] = _MSGSUBMITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgOracleRequest = _reflection.GeneratedProtocolMessageType('MsgOracleRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLEREQUEST,
  '__module__' : 'fx.oracle.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.MsgOracleRequest)
  })
_sym_db.RegisterMessage(MsgOracleRequest)

MsgOracleResponse = _reflection.GeneratedProtocolMessageType('MsgOracleResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGORACLERESPONSE,
  '__module__' : 'fx.oracle.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.MsgOracleResponse)
  })
_sym_db.RegisterMessage(MsgOracleResponse)

MsgSubmitAnswer = _reflection.GeneratedProtocolMessageType('MsgSubmitAnswer', (_message.Message,), {
  'DESCRIPTOR' : _MSGSUBMITANSWER,
  '__module__' : 'fx.oracle.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.MsgSubmitAnswer)
  })
_sym_db.RegisterMessage(MsgSubmitAnswer)

MsgSubmitResponse = _reflection.GeneratedProtocolMessageType('MsgSubmitResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGSUBMITRESPONSE,
  '__module__' : 'fx.oracle.tx_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.MsgSubmitResponse)
  })
_sym_db.RegisterMessage(MsgSubmitResponse)


DESCRIPTOR._options = None
_MSGORACLEREQUEST.fields_by_name['fee_limit']._options = None
_MSGORACLEREQUEST.fields_by_name['market_type']._options = None
_MSGSUBMITANSWER.fields_by_name['answer']._options = None

_MSG = _descriptor.ServiceDescriptor(
  name='Msg',
  full_name='fx.oracle.Msg',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=406,
  serialized_end=561,
  methods=[
  _descriptor.MethodDescriptor(
    name='OracleRequest',
    full_name='fx.oracle.Msg.OracleRequest',
    index=0,
    containing_service=None,
    input_type=_MSGORACLEREQUEST,
    output_type=_MSGORACLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitAnswer',
    full_name='fx.oracle.Msg.SubmitAnswer',
    index=1,
    containing_service=None,
    input_type=_MSGSUBMITANSWER,
    output_type=_MSGSUBMITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MSG)

DESCRIPTOR.services_by_name['Msg'] = _MSG

# @@protoc_insertion_point(module_scope)
