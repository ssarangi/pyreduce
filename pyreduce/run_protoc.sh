#!/usr/bin/env bash
/usr/local/bin/python3 -m grpc_tools.protoc -Iprotos --python_out=protos --grpc_python_out=protos protos/master.proto
/usr/local/bin/python3 -m grpc_tools.protoc -Iprotos --python_out=protos --grpc_python_out=protos protos/models.proto