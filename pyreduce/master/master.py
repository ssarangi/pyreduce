# Main file for the Master server
import grpc
from concurrent import futures
from flask import Flask

from utils.logutils import get_logger
from protos import master_pb2 as master_pb2
from protos import master_pb2_grpc as master_pb2_grpc

from .config import WEB_APP_PORT


logger = get_logger(__name__)
grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
app = Flask(__name__)

class Master:
    def __init__(self):
        self._agents = [] # Empty list of agents

class MasterServicer(master_pb2_grpc.MasterServicer):
    def ExecutePipeline(self, request, context):
        return 'Hello World from Master'

@app.route('/')
def index():
    return 'Hello World'

def execute_master():
    master_pb2_grpc.add_MasterServicer_to_server(MasterServicer(), grpc_server)

    # Listen on port 50051
    logger.info('Starting Master. Listening on port 50051.')
    grpc_server.add_insecure_port('[::]:50051')
    grpc_server.start()
    logger.info('Monitor your job: %s:%s ', '127.0.0.1', WEB_APP_PORT)
    app.run(debug=True, host='0.0.0.0', port=WEB_APP_PORT)
