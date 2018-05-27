import grpc

from config.discovery_cfg import DiscoveryConfig
from protos import models_pb2, master_pb2, master_pb2_grpc
from utils import get_logger
from utils import get_machine_name, get_ip_address
from .discover import discover
from .system_info_gatherer import system_info_gatherer

logger = get_logger(__name__)

def execute_agent():
    _, _, grpc_server_ip, grpc_server_port = discover(
        magic=DiscoveryConfig.MAGIC,
        port=DiscoveryConfig.PORT,
        password=DiscoveryConfig.PASSWORD,
        timeout=5)

    # cpu_infos, python_info = system_info_gatherer()
    # logger.info(cpu_infos)
    # logger.info(python_info)

    # channel = grpc.insecure_channel('localhost:%s' % (grpc_server_port)) # (grpc_server_ip, grpc_server_port))
    grpc_server = '%s:%s' % (grpc_server_ip, grpc_server_port)
    logger.info('Connecting to GRPC server at %s', grpc_server)
    channel = grpc.insecure_channel(grpc_server)
    # create a stub (client)
    stub = master_pb2_grpc.MasterStub(channel)

    # create a valid request message
    network_info = models_pb2.NetworkInfo(ip_address=get_ip_address())
    system_info = models_pb2.SystemInfo(hostname=get_machine_name(),
                                        network_info=network_info)
    register_agent_request = master_pb2.RegisterAgentRequest(system_info=system_info)

    # make the call
    response = stub.RegisterAgent(register_agent_request)

    logger.warning(response)
