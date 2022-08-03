# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fx_py_sdk.codec.fx.dex.v1 import query_pb2 as fx_dot_dex_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryParams = channel.unary_unary(
                '/fx.dex.v1.Query/QueryParams',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsResp.FromString,
                )
        self.QueryOrders = channel.unary_unary(
                '/fx.dex.v1.Query/QueryOrders',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersResponse.FromString,
                )
        self.QueryPendingOrders = channel.unary_unary(
                '/fx.dex.v1.Query/QueryPendingOrders',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPendingOrdersResponse.FromString,
                )
        self.QueryOrder = channel.unary_unary(
                '/fx.dex.v1.Query/QueryOrder',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderRequest.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderResponse.FromString,
                )
        self.QueryOrderbook = channel.unary_unary(
                '/fx.dex.v1.Query/QueryOrderbook',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookResp.FromString,
                )
        self.QueryPositions = channel.unary_unary(
                '/fx.dex.v1.Query/QueryPositions',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsResp.FromString,
                )
        self.QueryPosition = channel.unary_unary(
                '/fx.dex.v1.Query/QueryPosition',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionResp.FromString,
                )
        self.QueryFunding = channel.unary_unary(
                '/fx.dex.v1.Query/QueryFunding',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingResp.FromString,
                )
        self.QueryPairFundingRates = channel.unary_unary(
                '/fx.dex.v1.Query/QueryPairFundingRates',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesResp.FromString,
                )
        self.QueryFundingTime = channel.unary_unary(
                '/fx.dex.v1.Query/QueryFundingTime',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeResp.FromString,
                )
        self.QueryDealPrice = channel.unary_unary(
                '/fx.dex.v1.Query/QueryDealPrice',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceResp.FromString,
                )
        self.QueryMatchResult = channel.unary_unary(
                '/fx.dex.v1.Query/QueryMatchResult',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultResp.FromString,
                )
        self.QueryMarkPrice = channel.unary_unary(
                '/fx.dex.v1.Query/QueryMarkPrice',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceResp.FromString,
                )
        self.QueryMarkAndOraclePrice = channel.unary_unary(
                '/fx.dex.v1.Query/QueryMarkAndOraclePrice',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceResp.FromString,
                )
        self.QueryLiquidationPrice = channel.unary_unary(
                '/fx.dex.v1.Query/QueryLiquidationPrice',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceResp.FromString,
                )
        self.QueryMovingAverage = channel.unary_unary(
                '/fx.dex.v1.Query/QueryMovingAverage',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMAReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMAResp.FromString,
                )
        self.QueryStoreStatistic = channel.unary_unary(
                '/fx.dex.v1.Query/QueryStoreStatistic',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticResp.FromString,
                )
        self.QueryIsFunding = channel.unary_unary(
                '/fx.dex.v1.Query/QueryIsFunding',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingResp.FromString,
                )
        self.QueryPremiumIndexConf = channel.unary_unary(
                '/fx.dex.v1.Query/QueryPremiumIndexConf',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfResp.FromString,
                )
        self.QueryNeedToLiquidationPosIds = channel.unary_unary(
                '/fx.dex.v1.Query/QueryNeedToLiquidationPosIds',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidationPosIdsReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidatorPosIdsResp.FromString,
                )
        self.QueryAccountNumber = channel.unary_unary(
                '/fx.dex.v1.Query/QueryAccountNumber',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberResp.FromString,
                )
        self.QueryReserve = channel.unary_unary(
                '/fx.dex.v1.Query/QueryReserve',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveResp.FromString,
                )
        self.QueryChainStatistics = channel.unary_unary(
                '/fx.dex.v1.Query/QueryChainStatistics',
                request_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsReq.SerializeToString,
                response_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsResp.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def QueryParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryOrders(self, request, context):
        """orders query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPendingOrders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryOrderbook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPositions(self, request, context):
        """positions query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryFunding(self, request, context):
        """fundings query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPairFundingRates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryFundingTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryDealPrice(self, request, context):
        """query latest deal price no matter what block
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryMatchResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryMarkPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryMarkAndOraclePrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryLiquidationPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryMovingAverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryStoreStatistic(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryIsFunding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPremiumIndexConf(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryNeedToLiquidationPosIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryAccountNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryReserve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryChainStatistics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'QueryParams': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryParams,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsResp.SerializeToString,
            ),
            'QueryOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryOrders,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersResponse.SerializeToString,
            ),
            'QueryPendingOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPendingOrders,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPendingOrdersResponse.SerializeToString,
            ),
            'QueryOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryOrder,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderRequest.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderResponse.SerializeToString,
            ),
            'QueryOrderbook': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryOrderbook,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookResp.SerializeToString,
            ),
            'QueryPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPositions,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsResp.SerializeToString,
            ),
            'QueryPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPosition,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionResp.SerializeToString,
            ),
            'QueryFunding': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryFunding,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingResp.SerializeToString,
            ),
            'QueryPairFundingRates': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPairFundingRates,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesResp.SerializeToString,
            ),
            'QueryFundingTime': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryFundingTime,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeResp.SerializeToString,
            ),
            'QueryDealPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryDealPrice,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceResp.SerializeToString,
            ),
            'QueryMatchResult': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryMatchResult,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultResp.SerializeToString,
            ),
            'QueryMarkPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryMarkPrice,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceResp.SerializeToString,
            ),
            'QueryMarkAndOraclePrice': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryMarkAndOraclePrice,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceResp.SerializeToString,
            ),
            'QueryLiquidationPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryLiquidationPrice,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceResp.SerializeToString,
            ),
            'QueryMovingAverage': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryMovingAverage,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMAReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryMAResp.SerializeToString,
            ),
            'QueryStoreStatistic': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryStoreStatistic,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticResp.SerializeToString,
            ),
            'QueryIsFunding': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryIsFunding,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingResp.SerializeToString,
            ),
            'QueryPremiumIndexConf': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPremiumIndexConf,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfResp.SerializeToString,
            ),
            'QueryNeedToLiquidationPosIds': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryNeedToLiquidationPosIds,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidationPosIdsReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidatorPosIdsResp.SerializeToString,
            ),
            'QueryAccountNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryAccountNumber,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberResp.SerializeToString,
            ),
            'QueryReserve': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryReserve,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveResp.SerializeToString,
            ),
            'QueryChainStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryChainStatistics,
                    request_deserializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsReq.FromString,
                    response_serializer=fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fx.dex.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def QueryParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryParams',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryParamsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryOrders',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryPendingOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryPendingOrders',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrdersRequest.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPendingOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryOrder',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderRequest.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryOrderbook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryOrderbook',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryOrderbookResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryPositions',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryPosition',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPositionResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryFunding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryFunding',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryPairFundingRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryPairFundingRates',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPairFundingRatesResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryFundingTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryFundingTime',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryFundingTimeResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryDealPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryDealPrice',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryDealPriceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryMatchResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryMatchResult',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMatchResultResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryMarkPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryMarkPrice',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkPriceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryMarkAndOraclePrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryMarkAndOraclePrice',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMarkAndOraclePriceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryLiquidationPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryLiquidationPrice',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryLiquidationPriceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryMovingAverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryMovingAverage',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMAReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryMAResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryStoreStatistic(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryStoreStatistic',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryStoreStatisticResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryIsFunding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryIsFunding',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryIsFundingResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryPremiumIndexConf(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryPremiumIndexConf',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryPremiumIndexConfResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryNeedToLiquidationPosIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryNeedToLiquidationPosIds',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidationPosIdsReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryNeedToLiquidatorPosIdsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryAccountNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryAccountNumber',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryAccountNumberResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryReserve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryReserve',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryReserveResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryChainStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fx.dex.v1.Query/QueryChainStatistics',
            fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsReq.SerializeToString,
            fx_dot_dex_dot_v1_dot_query__pb2.QueryChainStatisticsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
