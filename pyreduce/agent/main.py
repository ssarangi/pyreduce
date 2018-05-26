import grpc

from config.discovery_cfg import DiscoveryConfig
from protos import master_pb2, master_pb2_grpc
from utils.logutils import get_logger
from .discover import discover
from .system_info_gatherer import system_info_gatherer

logger = get_logger(__name__)

def execute_agent():
    _, _, grpc_server_port, grpc_server_ip = discover(
        magic=DiscoveryConfig.MAGIC,
        port=DiscoveryConfig.PORT,
        password=DiscoveryConfig.PASSWORD,
        timeout=5)

    logger.info('GRPC port found from server: %s', grpc_server_port)
    # cpu_infos, python_info = system_info_gatherer()
    # logger.info(cpu_infos)
    # logger.info(python_info)

    channel = grpc.insecure_channel('localhost:%s' % (grpc_server_port)) # (grpc_server_ip, grpc_server_port))
    # create a stub (client)
    stub = master_pb2_grpc.MasterStub(channel)

    # create a valid request message
    register_agent_request = master_pb2.RegisterAgentRequest()

    # make the call
    response = stub.RegisterAgent(register_agent_request)

    logger.warning(response)
