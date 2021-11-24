proto_dirs=$(find ./protos -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
for dir in $proto_dirs; do
  python -m grpc_tools.protoc \
  -I=./protos \
  -I=./third_party_protos \
  --python_out=. \
  --grpc_python_out=. \
  $(find "${dir}" -maxdepth 1 -name '*.proto')
done

proto_dirs=$(find ./third_party_protos -path -prune -o -name '*.proto' -print0 | xargs -0 -n1 dirname | sort | uniq)
for dir in $proto_dirs; do
  python -m grpc_tools.protoc \
  -I=./third_party_protos \
  --python_out=. \
  --grpc_python_out=. \
  $(find "${dir}" -maxdepth 1 -name '*.proto')
done