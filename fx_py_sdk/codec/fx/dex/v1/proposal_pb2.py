# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fx_py_sdk.codec.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from fx_py_sdk.codec.fx.dex.v1 import funding_pb2 as fx_dot_dex_dot_v1_dot_funding__pb2
from fx_py_sdk.codec.fx.dex.v1 import margin_pb2 as fx_dot_dex_dot_v1_dot_margin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/v1/proposal.proto',
  package='fx.dex.v1',
  syntax='proto3',
  serialized_options=b'Z(github.com/marginxio/marginx/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x66x/dex/v1/proposal.proto\x12\tfx.dex.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x66x/dex/v1/funding.proto\x1a\x16\x66x/dex/v1/margin.proto\"z\n\x18ResetFundingTimeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12,\n\x0c\x66unding_time\x18\x03 \x01(\x0b\x32\x16.fx.dex.v1.FundingTime:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"z\n\x1aResetFundingParamsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x0e\x66unding_params\x18\x03 \x01(\x0b\x32\x12.fx.dex.v1.Funding:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\xaa\x01\n\x15ResetMMATableProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x0bmargin_rate\x18\x03 \x03(\x0b\x32\x15.fx.dex.v1.MarginRate\x12\x33\n\x10init_margin_rate\x18\x04 \x03(\x0b\x32\x19.fx.dex.v1.InitMarginRate:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"e\n\x12\x43reatePairProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1d\n\x04pair\x18\x03 \x01(\x0b\x32\x0f.fx.dex.v1.Pair:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\x99\x01\n\x04Pair\x12\x12\n\nbase_asset\x18\x01 \x01(\t\x12\x13\n\x0bquote_asset\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12\x15\n\rprice_decimal\x18\x04 \x01(\x03\x12\x18\n\x10position_decimal\x18\x05 \x01(\x03\x12\x12\n\ninit_price\x18\x06 \x01(\t\x12\x13\n\x0bmarket_type\x18\x07 \x01(\t\"\x8c\x01\n\x1fResetPremiumIndexConfigProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x37\n\x12premium_index_conf\x18\x03 \x01(\x0b\x32\x1b.fx.dex.v1.PremiumIndexConf:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"k\n\x12ShareSplitProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nmultiplier\x18\x03 \x01(\t\x12\x0f\n\x07pair_id\x18\x04 \x01(\t:\x0c\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x42*Z(github.com/marginxio/marginx/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,fx_dot_dex_dot_v1_dot_funding__pb2.DESCRIPTOR,fx_dot_dex_dot_v1_dot_margin__pb2.DESCRIPTOR,])




_RESETFUNDINGTIMEPROPOSAL = _descriptor.Descriptor(
  name='ResetFundingTimeProposal',
  full_name='fx.dex.v1.ResetFundingTimeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.ResetFundingTimeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.ResetFundingTimeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funding_time', full_name='fx.dex.v1.ResetFundingTimeProposal.funding_time', index=2,
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
  serialized_start=110,
  serialized_end=232,
)


_RESETFUNDINGPARAMSPROPOSAL = _descriptor.Descriptor(
  name='ResetFundingParamsProposal',
  full_name='fx.dex.v1.ResetFundingParamsProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.ResetFundingParamsProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.ResetFundingParamsProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funding_params', full_name='fx.dex.v1.ResetFundingParamsProposal.funding_params', index=2,
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
  serialized_end=356,
)


_RESETMMATABLEPROPOSAL = _descriptor.Descriptor(
  name='ResetMMATableProposal',
  full_name='fx.dex.v1.ResetMMATableProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.ResetMMATableProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.ResetMMATableProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin_rate', full_name='fx.dex.v1.ResetMMATableProposal.margin_rate', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_margin_rate', full_name='fx.dex.v1.ResetMMATableProposal.init_margin_rate', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_options=b'\350\240\037\000\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=359,
  serialized_end=529,
)


_CREATEPAIRPROPOSAL = _descriptor.Descriptor(
  name='CreatePairProposal',
  full_name='fx.dex.v1.CreatePairProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.CreatePairProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.CreatePairProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair', full_name='fx.dex.v1.CreatePairProposal.pair', index=2,
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
  serialized_start=531,
  serialized_end=632,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='fx.dex.v1.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_asset', full_name='fx.dex.v1.Pair.base_asset', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote_asset', full_name='fx.dex.v1.Pair.quote_asset', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='fx.dex.v1.Pair.active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price_decimal', full_name='fx.dex.v1.Pair.price_decimal', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position_decimal', full_name='fx.dex.v1.Pair.position_decimal', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_price', full_name='fx.dex.v1.Pair.init_price', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='market_type', full_name='fx.dex.v1.Pair.market_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=635,
  serialized_end=788,
)


_RESETPREMIUMINDEXCONFIGPROPOSAL = _descriptor.Descriptor(
  name='ResetPremiumIndexConfigProposal',
  full_name='fx.dex.v1.ResetPremiumIndexConfigProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.ResetPremiumIndexConfigProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.ResetPremiumIndexConfigProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='premium_index_conf', full_name='fx.dex.v1.ResetPremiumIndexConfigProposal.premium_index_conf', index=2,
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
  serialized_start=791,
  serialized_end=931,
)


_SHARESPLITPROPOSAL = _descriptor.Descriptor(
  name='ShareSplitProposal',
  full_name='fx.dex.v1.ShareSplitProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='fx.dex.v1.ShareSplitProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='fx.dex.v1.ShareSplitProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='fx.dex.v1.ShareSplitProposal.multiplier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.v1.ShareSplitProposal.pair_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_options=b'\350\240\037\000\210\240\037\000\230\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=933,
  serialized_end=1040,
)

_RESETFUNDINGTIMEPROPOSAL.fields_by_name['funding_time'].message_type = fx_dot_dex_dot_v1_dot_funding__pb2._FUNDINGTIME
_RESETFUNDINGPARAMSPROPOSAL.fields_by_name['funding_params'].message_type = fx_dot_dex_dot_v1_dot_funding__pb2._FUNDING
_RESETMMATABLEPROPOSAL.fields_by_name['margin_rate'].message_type = fx_dot_dex_dot_v1_dot_margin__pb2._MARGINRATE
_RESETMMATABLEPROPOSAL.fields_by_name['init_margin_rate'].message_type = fx_dot_dex_dot_v1_dot_margin__pb2._INITMARGINRATE
_CREATEPAIRPROPOSAL.fields_by_name['pair'].message_type = _PAIR
_RESETPREMIUMINDEXCONFIGPROPOSAL.fields_by_name['premium_index_conf'].message_type = fx_dot_dex_dot_v1_dot_funding__pb2._PREMIUMINDEXCONF
DESCRIPTOR.message_types_by_name['ResetFundingTimeProposal'] = _RESETFUNDINGTIMEPROPOSAL
DESCRIPTOR.message_types_by_name['ResetFundingParamsProposal'] = _RESETFUNDINGPARAMSPROPOSAL
DESCRIPTOR.message_types_by_name['ResetMMATableProposal'] = _RESETMMATABLEPROPOSAL
DESCRIPTOR.message_types_by_name['CreatePairProposal'] = _CREATEPAIRPROPOSAL
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['ResetPremiumIndexConfigProposal'] = _RESETPREMIUMINDEXCONFIGPROPOSAL
DESCRIPTOR.message_types_by_name['ShareSplitProposal'] = _SHARESPLITPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResetFundingTimeProposal = _reflection.GeneratedProtocolMessageType('ResetFundingTimeProposal', (_message.Message,), {
  'DESCRIPTOR' : _RESETFUNDINGTIMEPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.ResetFundingTimeProposal)
  })
_sym_db.RegisterMessage(ResetFundingTimeProposal)

ResetFundingParamsProposal = _reflection.GeneratedProtocolMessageType('ResetFundingParamsProposal', (_message.Message,), {
  'DESCRIPTOR' : _RESETFUNDINGPARAMSPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.ResetFundingParamsProposal)
  })
_sym_db.RegisterMessage(ResetFundingParamsProposal)

ResetMMATableProposal = _reflection.GeneratedProtocolMessageType('ResetMMATableProposal', (_message.Message,), {
  'DESCRIPTOR' : _RESETMMATABLEPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.ResetMMATableProposal)
  })
_sym_db.RegisterMessage(ResetMMATableProposal)

CreatePairProposal = _reflection.GeneratedProtocolMessageType('CreatePairProposal', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPAIRPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.CreatePairProposal)
  })
_sym_db.RegisterMessage(CreatePairProposal)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.Pair)
  })
_sym_db.RegisterMessage(Pair)

ResetPremiumIndexConfigProposal = _reflection.GeneratedProtocolMessageType('ResetPremiumIndexConfigProposal', (_message.Message,), {
  'DESCRIPTOR' : _RESETPREMIUMINDEXCONFIGPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.ResetPremiumIndexConfigProposal)
  })
_sym_db.RegisterMessage(ResetPremiumIndexConfigProposal)

ShareSplitProposal = _reflection.GeneratedProtocolMessageType('ShareSplitProposal', (_message.Message,), {
  'DESCRIPTOR' : _SHARESPLITPROPOSAL,
  '__module__' : 'fx.dex.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.v1.ShareSplitProposal)
  })
_sym_db.RegisterMessage(ShareSplitProposal)


DESCRIPTOR._options = None
_RESETFUNDINGTIMEPROPOSAL._options = None
_RESETFUNDINGPARAMSPROPOSAL._options = None
_RESETMMATABLEPROPOSAL._options = None
_CREATEPAIRPROPOSAL._options = None
_RESETPREMIUMINDEXCONFIGPROPOSAL._options = None
_SHARESPLITPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)
