# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protos.master_pb2 as master__pb2


class MasterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecutePipeline = channel.unary_unary(
        '/protos.Master/ExecutePipeline',
        request_serializer=master__pb2.PipelineRequest.SerializeToString,
        response_deserializer=master__pb2.PipelineResponse.FromString,
        )


class MasterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ExecutePipeline(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExecutePipeline': grpc.unary_unary_rpc_method_handler(
          servicer.ExecutePipeline,
          request_deserializer=master__pb2.PipelineRequest.FromString,
          response_serializer=master__pb2.PipelineResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protos.Master', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))