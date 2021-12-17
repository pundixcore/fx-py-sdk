# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fx_py_sdk.codec.fx.oracle import tx_pb2 as fx_dot_oracle_dot_tx__pb2


class MsgStub(object):
    """Msg defines the Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OracleRequest = channel.unary_unary(
                '/fx.oracle.Msg/OracleRequest',
                request_serializer=fx_dot_oracle_dot_tx__pb2.MsgOracleRequest.SerializeToString,
                response_deserializer=fx_dot_oracle_dot_tx__pb2.MsgOracleResponse.FromString,
                )
        self.SubmitAnswer = channel.unary_unary(
                '/fx.oracle.Msg/SubmitAnswer',
                request_serializer=fx_dot_oracle_dot_tx__pb2.MsgSubmitAnswer.SerializeToString,
                response_deserializer=fx_dot_oracle_dot_tx__pb2.MsgSubmitResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the Msg service.
    """

    def OracleRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitAnswer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OracleRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.OracleRequest,
                    request_deserializer=fx_dot_oracle_dot_tx__pb2.MsgOracleRequest.FromString,
                    response_serializer=fx_dot_oracle_dot_tx__pb2.MsgOracleResponse.SerializeToString,
            ),
            'SubmitAnswer': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitAnswer,
                    request_deserializer=fx_dot_oracle_dot_tx__pb2.MsgSubmitAnswer.FromString,
                    response_serializer=fx_dot_oracle_dot_tx__pb2.MsgSubmitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.oracle.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the Msg service.
    """

    @staticmethod
    def OracleRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.oracle.Msg/OracleRequest',
            fx_dot_oracle_dot_tx__pb2.MsgOracleRequest.SerializeToString,
            fx_dot_oracle_dot_tx__pb2.MsgOracleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitAnswer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.oracle.Msg/SubmitAnswer',
            fx_dot_oracle_dot_tx__pb2.MsgSubmitAnswer.SerializeToString,
            fx_dot_oracle_dot_tx__pb2.MsgSubmitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
