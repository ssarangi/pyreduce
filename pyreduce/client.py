import grpc
import pickle
import inspect

# import the generated classes
import protos.executor_pb2 as executor_pb2
import protos.executor_pb2_grpc as executor_pb2_grpc

def foo(a=5, b=7):
    return a + b

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = executor_pb2_grpc.ExecutorStub(channel)

code_str = pickle.dumps(inspect.getsource(foo))

# create a valid request message
job_request = executor_pb2.JobRequest(code=code_str, func_name='foo')

# make the call
response = stub.Execute(job_request)

# et voilà
print(response.ack)