# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/oracle/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.fx.oracle import genesis_pb2 as fx_dot_oracle_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/oracle/proposal.proto',
  package='fx.oracle',
  syntax='proto3',
  serialized_options=b'Z4git.wokoworks.com/blockchain/fx-chain/x/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x66x/oracle/proposal.proto\x12\tfx.oracle\x1a\x1cgoogle/api/annotations.proto\x1a\x14gogoproto/gogo.proto\x1a\x17\x66x/oracle/genesis.proto\"t\n\x14UpdateOracleProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x0b\x62\x61nd_oracle\x18\x03 \x01(\x0b\x32\x15.fx.oracle.BandOracle:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"w\n\x18UpdateAggregatorProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12)\n\naggregator\x18\x03 \x01(\x0b\x32\x15.fx.oracle.Aggregator:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x42\x36Z4git.wokoworks.com/blockchain/fx-chain/x/oracle/typesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,fx_dot_oracle_dot_genesis__pb2.DESCRIPTOR,])




_UPDATEORACLEPROPOSAL = _descriptor.Descriptor(
  name='UpdateOracleProposal',
  full_name='fx.oracle.UpdateOracleProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.oracle.UpdateOracleProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.oracle.UpdateOracleProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='band_oracle', full_name='fx.oracle.UpdateOracleProposal.band_oracle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=232,
)


_UPDATEAGGREGATORPROPOSAL = _descriptor.Descriptor(
  name='UpdateAggregatorProposal',
  full_name='fx.oracle.UpdateAggregatorProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.oracle.UpdateAggregatorProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.oracle.UpdateAggregatorProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregator', full_name='fx.oracle.UpdateAggregatorProposal.aggregator', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=353,
)

_UPDATEORACLEPROPOSAL.fields_by_name['band_oracle'].message_type = fx_dot_oracle_dot_genesis__pb2._BANDORACLE
_UPDATEAGGREGATORPROPOSAL.fields_by_name['aggregator'].message_type = fx_dot_oracle_dot_genesis__pb2._AGGREGATOR
DESCRIPTOR.message_types_by_name['UpdateOracleProposal'] = _UPDATEORACLEPROPOSAL
DESCRIPTOR.message_types_by_name['UpdateAggregatorProposal'] = _UPDATEAGGREGATORPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateOracleProposal = _reflection.GeneratedProtocolMessageType('UpdateOracleProposal', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORACLEPROPOSAL,
  '__module__' : 'fx.oracle.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.UpdateOracleProposal)
  })
_sym_db.RegisterMessage(UpdateOracleProposal)

UpdateAggregatorProposal = _reflection.GeneratedProtocolMessageType('UpdateAggregatorProposal', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEAGGREGATORPROPOSAL,
  '__module__' : 'fx.oracle.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.oracle.UpdateAggregatorProposal)
  })
_sym_db.RegisterMessage(UpdateAggregatorProposal)


DESCRIPTOR._options = None
_UPDATEORACLEPROPOSAL._options = None
_UPDATEAGGREGATORPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)
