# Main file for the Master server
import asyncio
import threading

from config import WebAppConfig, GRPCConfig
from protos import master_pb2_grpc as master_pb2_grpc
from utils import get_logger
from utils import get_ip_address

from .discovery_service import server_discover
from .rpc_api import MasterServicer, grpc_server
from .web_api import webapp

MODULE_NAME = "master"
logger = get_logger(MODULE_NAME)

loop = asyncio.get_event_loop()
def execute_master():
    master_pb2_grpc.add_MasterServicer_to_server(MasterServicer(), grpc_server)
    # Run the Discovery Service
    # Call server
    t = threading.Thread(target=server_discover, args=(loop,))
    t.start()

    # Listen on port 50051
    logger.info('Starting Master. Listening on port %s', GRPCConfig.PORT)
    grpc_server.add_insecure_port('[::]:%s' % GRPCConfig.PORT)
    grpc_server.start()
    logger.info('Monitor your job: %s:%s ', get_ip_address() , WebAppConfig.WEB_APP_PORT)
    webapp.run(debug=True, host='0.0.0.0', port=WebAppConfig.WEB_APP_PORT)
