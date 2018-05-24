# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executor.proto

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
  name='executor.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x65xecutor.proto\x12\x06protos\"-\n\nJobRequest\x12\x11\n\tfunc_name\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\"\x1a\n\x0bJobResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t2@\n\x08\x45xecutor\x12\x34\n\x07\x45xecute\x12\x12.protos.JobRequest\x1a\x13.protos.JobResponse\"\x00\x62\x06proto3')
)




_JOBREQUEST = _descriptor.Descriptor(
  name='JobRequest',
  full_name='protos.JobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='func_name', full_name='protos.JobRequest.func_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='protos.JobRequest.code', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=71,
)


_JOBRESPONSE = _descriptor.Descriptor(
  name='JobResponse',
  full_name='protos.JobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='protos.JobResponse.ack', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['JobRequest'] = _JOBREQUEST
DESCRIPTOR.message_types_by_name['JobResponse'] = _JOBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobRequest = _reflection.GeneratedProtocolMessageType('JobRequest', (_message.Message,), dict(
  DESCRIPTOR = _JOBREQUEST,
  __module__ = 'executor_pb2'
  # @@protoc_insertion_point(class_scope:protos.JobRequest)
  ))
_sym_db.RegisterMessage(JobRequest)

JobResponse = _reflection.GeneratedProtocolMessageType('JobResponse', (_message.Message,), dict(
  DESCRIPTOR = _JOBRESPONSE,
  __module__ = 'executor_pb2'
  # @@protoc_insertion_point(class_scope:protos.JobResponse)
  ))
_sym_db.RegisterMessage(JobResponse)



_EXECUTOR = _descriptor.ServiceDescriptor(
  name='Executor',
  full_name='protos.Executor',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=101,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='Execute',
    full_name='protos.Executor.Execute',
    index=0,
    containing_service=None,
    input_type=_JOBREQUEST,
    output_type=_JOBRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTOR)

DESCRIPTOR.services_by_name['Executor'] = _EXECUTOR

# @@protoc_insertion_point(module_scope)