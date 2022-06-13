# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fx_py_sdk.codec.cosmos.auth.v1beta1 import query_pb2 as cosmos_dot_auth_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Accounts = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Accounts',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString,
                )
        self.Account = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Account',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString,
                )
        self.Params = channel.unary_unary(
                '/cosmos.auth.v1beta1.Query/Params',
                request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Accounts(self, request, context):
        """Accounts returns all the existing accounts

        Since: cosmos-sdk 0.43
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account(self, request, context):
        """Account returns account details based on address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries all parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Accounts': grpc.unary_unary_rpc_method_handler(
                    servicer.Accounts,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.SerializeToString,
            ),
            'Account': grpc.unary_unary_rpc_method_handler(
                    servicer.Account,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.SerializeToString,
            ),
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.auth.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Accounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Accounts',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Account',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Params',
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
