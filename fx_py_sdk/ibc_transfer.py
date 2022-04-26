import yaml

class ConfigsKeys:
    IBC_CHANNELS = "IBC_CHANNELS"
    TSLA_FXCore = "TSLA_FXCore"
    FXCore_TSLA = "FXCore_TSLA"

    AAPL_FXCore = "AAPL_FXCore"
    FXCore_AAPL = "FXCore_AAPL"

    NFLX_FXCore = "NFLX_FXCore"
    FXCore_NFLX = "FXCore_NFLX"

    GOOG_FXCore = "GOOG_FXCore"
    FXCore_GOOG = "FXCore_GOOG"

    FB_FXCore = "FB_FXCore"
    FXCore_FB = "FXCore_FB"

    AMZ_FXCore = "AMZ_FXCore"
    FXCore_AMZ = "FXCore_AMZ"

    BTC_FXCore = "BTC_FXCore"
    FXCore_BTC = "FXCore_BTC"

    FX_FXCore = "FX_FXCore"
    FXCore_FX = "FXCore_FX"

    SPY_FXCore = "SPY_FXCore"
    FXCore_SPY = "FXCore_SPY"

    IWM_FXCore = "IWM_FXCore"
    FXCore_IWM = "FXCore_IWM"

    TQQQ_FXCore = "TQQQ_FXCore"
    FXCore_TQQQ = "FXCore_TQQQ"

    ###########rpc##############
    RPC = "RPC"
    TSLA_RPC = "TSLA_RPC"
    TSLA_GRPC = "TSLA_GRPC"

    AAPL_RPC = "AAPL_RPC"
    AAPL_GRPC = "AAPL_GRPC"

    NFLX_RPC = "NFLX_RPC"
    NFLX_GRPC = "NFLX_GRPC"

    GOOG_RPC = "GOOG_RPC"
    GOOG_GRPC = "GOOG_GRPC"

    FB_RPC = "FB_RPC"
    FB_GRPC = "FB_GRPC"

    AMZN_RPC = "AMZN_RPC"
    AMZN_GRPC = "AMZN_GRPC"

    BTC_RPC = "BTC_RPC"
    BTC_GRPC = "BTC_GRPC"

    FX_RPC = "FX_RPC"
    FX_GRPC = "FX_GRPC"

    SPY_RPC = "SPY_RPC"
    SPY_GRPC = "SPY_GRPC"

    IWM_RPC = "IWM_RPC"
    IWM_GRPC = "IWM_GRPC"

    TQQQ_RPC = "TQQQ_RPC"
    TQQQ_GRPC = "TQQQ_GRPC"


class Ibc_transfer:
    def __init__(self):
        with open("config.yaml", "r") as ymlfile:
            self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    def transfer_to_one(self):
        print("11")
