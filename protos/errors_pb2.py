# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/errors.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/errors.proto',
  package='disposable',
  syntax='proto3',
  serialized_pb=_b('\n\x13protos/errors.proto\x12\ndisposable\"~\n\x05\x45rror\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12)\n\x04info\x18\x03 \x03(\x0b\x32\x1b.disposable.Error.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x35\n\x1a\x30x19.github.com.disposableZ\ndisposable\xa2\x02\nDisposableb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ERROR_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='disposable.Error.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='disposable.Error.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='disposable.Error.InfoEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=161,
)

_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='disposable.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='disposable.Error.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='disposable.Error.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='disposable.Error.info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ERROR_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=161,
)

_ERROR_INFOENTRY.containing_type = _ERROR
_ERROR.fields_by_name['info'].message_type = _ERROR_INFOENTRY
DESCRIPTOR.message_types_by_name['Error'] = _ERROR

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _ERROR_INFOENTRY,
    __module__ = 'protos.errors_pb2'
    # @@protoc_insertion_point(class_scope:disposable.Error.InfoEntry)
    ))
  ,
  DESCRIPTOR = _ERROR,
  __module__ = 'protos.errors_pb2'
  # @@protoc_insertion_point(class_scope:disposable.Error)
  ))
_sym_db.RegisterMessage(Error)
_sym_db.RegisterMessage(Error.InfoEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\0320x19.github.com.disposableZ\ndisposable\242\002\nDisposable'))
_ERROR_INFOENTRY.has_options = True
_ERROR_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)