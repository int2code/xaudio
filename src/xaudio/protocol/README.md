# Generating the Python protocol files

Install the Protocol Buffers compiler (`protoc`) by following the
[official installation guide](https://protobuf.dev/installation/), then verify
that it is available:

```console
protoc --version
```

`interface.proto` imports `nanopb.proto`. Make that file available in this
directory before generating the Python files.

From the repository root, run:

```console
cd src/xaudio/protocol
protoc --proto_path=. --python_out=. --pyi_out=. --experimental_allow_proto3_optional interface.proto
```

This regenerates both files in this directory:

- `interface_pb2.py`, containing the Python protocol implementation
- `interface_pb2.pyi`, containing its type information

Commit both generated files whenever `interface.proto` changes. Do not edit the
generated files manually.
