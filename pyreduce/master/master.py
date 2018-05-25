# Main file for the Master server
import asyncio
import grpc
from concurrent import futures
from flask import Flask
import threading

from config.webapp_cfg import WebAppConfig
from .discovery_service import server_discover
from protos import master_pb2_grpc as master_pb2_grpc
from utils.logutils import get_logger
from utils.network import get_ip_address
from config.discovery_cfg import DiscoveryConfig

MODULE_NAME = "master"
logger = get_logger(MODULE_NAME)
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
webapp = Flask(__name__)


class MasterServer:
    def __init__(self):
        self._agents = [] # Empty list of agents

class MasterServicer(master_pb2_grpc.MasterServicer):
    def ExecutePipeline(self, request, context):
        return 'Hello World from Master'


@webapp.route('/')
def index():
    return 'Hello World'

loop = asyncio.get_event_loop()
def execute_master():
    master_pb2_grpc.add_MasterServicer_to_server(MasterServicer(), grpc_server)
    # Run the Discovery Service
    # Call server
    t = threading.Thread(target=server_discover, args=(loop,))
    t.start()

    # Listen on port 50051
    logger.info('Starting Master. Listening on port 50051.')
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    logger.info('Monitor your job: %s:%s ', get_ip_address() , WebAppConfig.WEB_APP_PORT)
    webapp.run(debug=True, host='0.0.0.0', port=WebAppConfig.WEB_APP_PORT)
