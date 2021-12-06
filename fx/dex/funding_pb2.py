# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fx/dex/funding.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fx/dex/funding.proto',
  package='fx.dex',
  syntax='proto3',
  serialized_options=b'Z\'github.com/functionx/fx-dex/x/dex/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x66x/dex/funding.proto\x12\x06\x66x.dex\x1a\x14gogoproto/gogo.proto\"\x7f\n\x10PairFundingRates\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x44\n\x0c\x66unding_rate\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0c\x66unding_time\x18\x03 \x01(\x03\"\xa5\x01\n\x07\x46unding\x12\x16\n\x0e\x66unding_period\x18\x01 \x01(\x03\x12\x19\n\x11next_funding_time\x18\x02 \x01(\x03\x12\x15\n\rfunding_times\x18\x03 \x01(\x03\x12\x15\n\rnext_log_time\x18\x04 \x01(\x03\x12\x1a\n\x12log_funding_period\x18\x05 \x01(\x03\x12\x1d\n\x15max_funding_per_block\x18\x06 \x01(\x03\"w\n\x0b\x46undingTime\x12\x13\n\x0bsummer_time\x18\x01 \x01(\x03\x12\x13\n\x0bwinter_time\x18\x02 \x01(\x03\x12\x15\n\rsummer_clocks\x18\x03 \x03(\t\x12\x15\n\rwinter_clocks\x18\x04 \x03(\t\x12\x10\n\x08holidays\x18\x05 \x03(\t\"n\n\rSettleFunding\x12\x12\n\nis_funding\x18\x01 \x01(\x08\x12I\n\x10next_position_id\x18\x02 \x01(\tB/\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Uint\xc8\xde\x1f\x00\"\xa1\x01\n\x10PremiumIndexConf\x12\x15\n\rupdate_period\x18\x01 \x01(\x03\x12\x18\n\x10next_update_time\x18\x02 \x01(\x03\x12\x18\n\x10round_start_time\x18\x03 \x01(\x03\x12\x17\n\x0fnext_round_time\x18\x04 \x01(\x03\x12\x14\n\x0cround_period\x18\x05 \x01(\x03\x12\x13\n\x0bround_index\x18\x06 \x01(\x05\"\xb5\x01\n\x0cPremiumIndex\x12\x0f\n\x07pair_id\x18\x01 \x01(\t\x12\x17\n\x0fround_timestamp\x18\x02 \x01(\x03\x12(\n\x05ticks\x18\x03 \x03(\x0b\x32\x19.fx.dex.PremiumIndex.Tick\x1aQ\n\x04Tick\x12=\n\x05value\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\n\n\x02ts\x18\x02 \x01(\x03\x42)Z\'github.com/functionx/fx-dex/x/dex/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_PAIRFUNDINGRATES = _descriptor.Descriptor(
  name='PairFundingRates',
  full_name='fx.dex.PairFundingRates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.PairFundingRates.pair_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funding_rate', full_name='fx.dex.PairFundingRates.funding_rate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funding_time', full_name='fx.dex.PairFundingRates.funding_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_end=181,
)


_FUNDING = _descriptor.Descriptor(
  name='Funding',
  full_name='fx.dex.Funding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='funding_period', full_name='fx.dex.Funding.funding_period', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_funding_time', full_name='fx.dex.Funding.next_funding_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funding_times', full_name='fx.dex.Funding.funding_times', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_log_time', full_name='fx.dex.Funding.next_log_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log_funding_period', full_name='fx.dex.Funding.log_funding_period', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_funding_per_block', full_name='fx.dex.Funding.max_funding_per_block', index=5,
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
  serialized_start=184,
  serialized_end=349,
)


_FUNDINGTIME = _descriptor.Descriptor(
  name='FundingTime',
  full_name='fx.dex.FundingTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='summer_time', full_name='fx.dex.FundingTime.summer_time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='winter_time', full_name='fx.dex.FundingTime.winter_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summer_clocks', full_name='fx.dex.FundingTime.summer_clocks', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='winter_clocks', full_name='fx.dex.FundingTime.winter_clocks', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='holidays', full_name='fx.dex.FundingTime.holidays', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=351,
  serialized_end=470,
)


_SETTLEFUNDING = _descriptor.Descriptor(
  name='SettleFunding',
  full_name='fx.dex.SettleFunding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_funding', full_name='fx.dex.SettleFunding.is_funding', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_position_id', full_name='fx.dex.SettleFunding.next_position_id', index=1,
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
  serialized_start=472,
  serialized_end=582,
)


_PREMIUMINDEXCONF = _descriptor.Descriptor(
  name='PremiumIndexConf',
  full_name='fx.dex.PremiumIndexConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_period', full_name='fx.dex.PremiumIndexConf.update_period', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_update_time', full_name='fx.dex.PremiumIndexConf.next_update_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round_start_time', full_name='fx.dex.PremiumIndexConf.round_start_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_round_time', full_name='fx.dex.PremiumIndexConf.next_round_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round_period', full_name='fx.dex.PremiumIndexConf.round_period', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round_index', full_name='fx.dex.PremiumIndexConf.round_index', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=585,
  serialized_end=746,
)


_PREMIUMINDEX_TICK = _descriptor.Descriptor(
  name='Tick',
  full_name='fx.dex.PremiumIndex.Tick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='fx.dex.PremiumIndex.Tick.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='fx.dex.PremiumIndex.Tick.ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=849,
  serialized_end=930,
)

_PREMIUMINDEX = _descriptor.Descriptor(
  name='PremiumIndex',
  full_name='fx.dex.PremiumIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pair_id', full_name='fx.dex.PremiumIndex.pair_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round_timestamp', full_name='fx.dex.PremiumIndex.round_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ticks', full_name='fx.dex.PremiumIndex.ticks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREMIUMINDEX_TICK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=930,
)

_PREMIUMINDEX_TICK.containing_type = _PREMIUMINDEX
_PREMIUMINDEX.fields_by_name['ticks'].message_type = _PREMIUMINDEX_TICK
DESCRIPTOR.message_types_by_name['PairFundingRates'] = _PAIRFUNDINGRATES
DESCRIPTOR.message_types_by_name['Funding'] = _FUNDING
DESCRIPTOR.message_types_by_name['FundingTime'] = _FUNDINGTIME
DESCRIPTOR.message_types_by_name['SettleFunding'] = _SETTLEFUNDING
DESCRIPTOR.message_types_by_name['PremiumIndexConf'] = _PREMIUMINDEXCONF
DESCRIPTOR.message_types_by_name['PremiumIndex'] = _PREMIUMINDEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PairFundingRates = _reflection.GeneratedProtocolMessageType('PairFundingRates', (_message.Message,), {
  'DESCRIPTOR' : _PAIRFUNDINGRATES,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.PairFundingRates)
  })
_sym_db.RegisterMessage(PairFundingRates)

Funding = _reflection.GeneratedProtocolMessageType('Funding', (_message.Message,), {
  'DESCRIPTOR' : _FUNDING,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.Funding)
  })
_sym_db.RegisterMessage(Funding)

FundingTime = _reflection.GeneratedProtocolMessageType('FundingTime', (_message.Message,), {
  'DESCRIPTOR' : _FUNDINGTIME,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.FundingTime)
  })
_sym_db.RegisterMessage(FundingTime)

SettleFunding = _reflection.GeneratedProtocolMessageType('SettleFunding', (_message.Message,), {
  'DESCRIPTOR' : _SETTLEFUNDING,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.SettleFunding)
  })
_sym_db.RegisterMessage(SettleFunding)

PremiumIndexConf = _reflection.GeneratedProtocolMessageType('PremiumIndexConf', (_message.Message,), {
  'DESCRIPTOR' : _PREMIUMINDEXCONF,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.PremiumIndexConf)
  })
_sym_db.RegisterMessage(PremiumIndexConf)

PremiumIndex = _reflection.GeneratedProtocolMessageType('PremiumIndex', (_message.Message,), {

  'Tick' : _reflection.GeneratedProtocolMessageType('Tick', (_message.Message,), {
    'DESCRIPTOR' : _PREMIUMINDEX_TICK,
    '__module__' : 'fx.dex.funding_pb2'
    # @@protoc_insertion_point(class_scope:fx.dex.PremiumIndex.Tick)
    })
  ,
  'DESCRIPTOR' : _PREMIUMINDEX,
  '__module__' : 'fx.dex.funding_pb2'
  # @@protoc_insertion_point(class_scope:fx.dex.PremiumIndex)
  })
_sym_db.RegisterMessage(PremiumIndex)
_sym_db.RegisterMessage(PremiumIndex.Tick)


DESCRIPTOR._options = None
_PAIRFUNDINGRATES.fields_by_name['funding_rate']._options = None
_SETTLEFUNDING.fields_by_name['next_position_id']._options = None
_PREMIUMINDEX_TICK.fields_by_name['value']._options = None
# @@protoc_insertion_point(module_scope)
