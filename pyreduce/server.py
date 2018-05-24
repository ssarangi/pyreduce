import grpc
import dill as pickle
from concurrent import futures
import time
import inspect

# import the generated classes
import protos.executor_pb2 as executor_pb2
import protos.executor_pb2_grpc as executor_pb2_grpc

def exec_code_and_return_x(code_object):
    code_globals = {}
    code_locals = {}
    exec(code_object, code_globals, code_locals)
    return code_locals.get('result')

# create a class to define the master functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class ExecutorServicer(executor_pb2_grpc.ExecutorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def Execute(self, request, context):
        response = executor_pb2.JobResponse()
        code_str = pickle.loads(request.code)
        code_str += "\n"
        code_str += "print('Hello World')\n"
        code_str += "result = " + request.func_name + "()\n"
        code_str += "print(result)"
        print(code_str)
        code_obj = compile(code_str, '<string>', 'exec')
        print(inspect.getmodulename(code_str))
        print(code_obj.co_name)
        result = exec_code_and_return_x(code_obj)
        response.ack = ("*" * 10) + str(result) + ("*" * 10)
        return response


# create a gRPC master
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the master
executor_pb2_grpc.add_ExecutorServicer_to_server(ExecutorServicer(), server)

# listen on port 50051
print('Starting master. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since master.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)