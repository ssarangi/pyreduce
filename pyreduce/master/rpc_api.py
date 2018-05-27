import grpc
import pendulum
from concurrent import futures
from protos import master_pb2_grpc as master_pb2_grpc
from protos import master_pb2
from .master_server_info import MasterServerInfo
from utils import get_logger
from .master_server_info import master_server_info

grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))


class MasterServicer(master_pb2_grpc.MasterServicer):
    def __init__(self):
        self.master_server_info = MasterServerInfo()
        self.logger = get_logger(__name__)

    def ExecutePipeline(self, request, context):
        return master_pb2.PipelineResponse()

    def RegisterAgent(self, request, context):
        hostname = request.system_info.hostname
        s = '\nRegistering Agent:\n'
        s += ('Hostname: %s\n' % hostname)
        s += ('IP Address: %s\n' % request.system_info.network_info.ip_address)
        self.logger.info(s)
        unique_id = master_server_info.register_agent(request.system_info, pendulum.now())
        register_agent_response = master_pb2.RegisterAgentResponse(client_id=unique_id)
        return register_agent_response

    def ClientHeartBeat(self, request, context):
        self.logger.info('Received heart beat from agent: %s', request.unique_id)
        heartbeat_response = master_pb2.AgentHeartBeatResponse()
        return heartbeat_response