import grpc
from concurrent import futures
from protos import master_pb2_grpc as master_pb2_grpc

grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))

class MasterServicer(master_pb2_grpc.MasterServicer):
    def ExecutePipeline(self, request, context):
        return 'Hello World from Master'

    def RegisterAgent(self, request, context):
        return "I got this"