#!/usr/bin/env bash
python -m grpc_tools.protoc -Iprotos --python_out=protos --grpc_python_out=protos protos/master.proto