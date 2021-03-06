# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protos.executor_pb2 as executor__pb2


class ExecutorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Execute = channel.unary_unary(
        '/protos.Executor/Execute',
        request_serializer=executor__pb2.JobRequest.SerializeToString,
        response_deserializer=executor__pb2.JobResponse.FromString,
        )


class ExecutorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Execute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExecutorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Execute': grpc.unary_unary_rpc_method_handler(
          servicer.Execute,
          request_deserializer=executor__pb2.JobRequest.FromString,
          response_serializer=executor__pb2.JobResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Executor', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
