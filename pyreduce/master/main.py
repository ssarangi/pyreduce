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

def run_discovery_service():
    # Run the Discovery Service
    t = threading.Thread(target=server_discover, args=(loop,))
    t.start()

def run_grpc_service(only_server=False):
    logger.info('Starting Master. Listening on port %s', GRPCConfig.PORT)
    master_pb2_grpc.add_MasterServicer_to_server(MasterServicer(), grpc_server)
    grpc_server.add_insecure_port('[::]:%s' % GRPCConfig.PORT)
    grpc_server.start()

    if only_server:
        while True:
            pass

def run_web_app():
    # Run the web app
    logger.info('Monitor your job: %s:%s ', get_ip_address() , WebAppConfig.WEB_APP_PORT)
    webapp.run(debug=True, host='0.0.0.0', port=WebAppConfig.WEB_APP_PORT)

def execute_master():
    run_discovery_service()
    run_grpc_service(only_server=True)
    run_web_app()


