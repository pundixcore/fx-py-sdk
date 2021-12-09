#!/usr/bin/env bash
find codec -name '*.py' | xargs -I{} sed -i -r 's/^from (.*) import (.+_pb2.*)/from fx_py_sdk.codec.\1 import \2/g' {}
find codec -name '*.py' | xargs -I{} sed -i -r 's/^from .*(.*google\.protobuf.*) import (.+_pb2.*)/from \1 import \2/g' {}


