# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/anchor_generator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import flexible_grid_anchor_generator_pb2 as object__detection_dot_protos_dot_flexible__grid__anchor__generator__pb2
from object_detection.protos import grid_anchor_generator_pb2 as object__detection_dot_protos_dot_grid__anchor__generator__pb2
from object_detection.protos import multiscale_anchor_generator_pb2 as object__detection_dot_protos_dot_multiscale__anchor__generator__pb2
from object_detection.protos import ssd_anchor_generator_pb2 as object__detection_dot_protos_dot_ssd__anchor__generator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='object_detection/protos/anchor_generator.proto',
  package='object_detection.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.object_detection/protos/anchor_generator.proto\x12\x17object_detection.protos\x1a<object_detection/protos/flexible_grid_anchor_generator.proto\x1a\x33object_detection/protos/grid_anchor_generator.proto\x1a\x39object_detection/protos/multiscale_anchor_generator.proto\x1a\x32object_detection/protos/ssd_anchor_generator.proto\"\x82\x03\n\x0f\x41nchorGenerator\x12M\n\x15grid_anchor_generator\x18\x01 \x01(\x0b\x32,.object_detection.protos.GridAnchorGeneratorH\x00\x12K\n\x14ssd_anchor_generator\x18\x02 \x01(\x0b\x32+.object_detection.protos.SsdAnchorGeneratorH\x00\x12Y\n\x1bmultiscale_anchor_generator\x18\x03 \x01(\x0b\x32\x32.object_detection.protos.MultiscaleAnchorGeneratorH\x00\x12^\n\x1e\x66lexible_grid_anchor_generator\x18\x04 \x01(\x0b\x32\x34.object_detection.protos.FlexibleGridAnchorGeneratorH\x00\x42\x18\n\x16\x61nchor_generator_oneof'
  ,
  dependencies=[object__detection_dot_protos_dot_flexible__grid__anchor__generator__pb2.DESCRIPTOR,object__detection_dot_protos_dot_grid__anchor__generator__pb2.DESCRIPTOR,object__detection_dot_protos_dot_multiscale__anchor__generator__pb2.DESCRIPTOR,object__detection_dot_protos_dot_ssd__anchor__generator__pb2.DESCRIPTOR,])




_ANCHORGENERATOR = _descriptor.Descriptor(
  name='AnchorGenerator',
  full_name='object_detection.protos.AnchorGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='grid_anchor_generator', full_name='object_detection.protos.AnchorGenerator.grid_anchor_generator', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssd_anchor_generator', full_name='object_detection.protos.AnchorGenerator.ssd_anchor_generator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multiscale_anchor_generator', full_name='object_detection.protos.AnchorGenerator.multiscale_anchor_generator', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flexible_grid_anchor_generator', full_name='object_detection.protos.AnchorGenerator.flexible_grid_anchor_generator', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='anchor_generator_oneof', full_name='object_detection.protos.AnchorGenerator.anchor_generator_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=302,
  serialized_end=688,
)

_ANCHORGENERATOR.fields_by_name['grid_anchor_generator'].message_type = object__detection_dot_protos_dot_grid__anchor__generator__pb2._GRIDANCHORGENERATOR
_ANCHORGENERATOR.fields_by_name['ssd_anchor_generator'].message_type = object__detection_dot_protos_dot_ssd__anchor__generator__pb2._SSDANCHORGENERATOR
_ANCHORGENERATOR.fields_by_name['multiscale_anchor_generator'].message_type = object__detection_dot_protos_dot_multiscale__anchor__generator__pb2._MULTISCALEANCHORGENERATOR
_ANCHORGENERATOR.fields_by_name['flexible_grid_anchor_generator'].message_type = object__detection_dot_protos_dot_flexible__grid__anchor__generator__pb2._FLEXIBLEGRIDANCHORGENERATOR
_ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof'].fields.append(
  _ANCHORGENERATOR.fields_by_name['grid_anchor_generator'])
_ANCHORGENERATOR.fields_by_name['grid_anchor_generator'].containing_oneof = _ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof']
_ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof'].fields.append(
  _ANCHORGENERATOR.fields_by_name['ssd_anchor_generator'])
_ANCHORGENERATOR.fields_by_name['ssd_anchor_generator'].containing_oneof = _ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof']
_ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof'].fields.append(
  _ANCHORGENERATOR.fields_by_name['multiscale_anchor_generator'])
_ANCHORGENERATOR.fields_by_name['multiscale_anchor_generator'].containing_oneof = _ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof']
_ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof'].fields.append(
  _ANCHORGENERATOR.fields_by_name['flexible_grid_anchor_generator'])
_ANCHORGENERATOR.fields_by_name['flexible_grid_anchor_generator'].containing_oneof = _ANCHORGENERATOR.oneofs_by_name['anchor_generator_oneof']
DESCRIPTOR.message_types_by_name['AnchorGenerator'] = _ANCHORGENERATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnchorGenerator = _reflection.GeneratedProtocolMessageType('AnchorGenerator', (_message.Message,), {
  'DESCRIPTOR' : _ANCHORGENERATOR,
  '__module__' : 'object_detection.protos.anchor_generator_pb2'
  # @@protoc_insertion_point(class_scope:object_detection.protos.AnchorGenerator)
  })
_sym_db.RegisterMessage(AnchorGenerator)


# @@protoc_insertion_point(module_scope)
