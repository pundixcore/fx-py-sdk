from typing import NamedTuple
from decimal import Decimal

class EnvVar:
    NETWORK = "NETWORK"
    DB_URI = "DB_URI"

class NetworkENV:
    LOCAL = "local"
    DEVNET = "devnet"
    TESTNET = "testnet"
    MAINNET = "mainnet"

class Network:
    LOCAL = "ws://127.0.0.1:26657/"
    DEVNET = "ws://44.196.199.119:26657/"
    TESTNET = ""
    MAINNET = ""

class DB:
    Database = "database"
    User = "user"
    Password = "password"
    Host = "host"
    Port = "port"

class Order(NamedTuple):
    TxHash: str
    Id: str
    Owner: str
    PairId: str
    Direction: str
    Price: Decimal
    BaseQuantity: Decimal
    QuoteQuantity: Decimal
    FilledQuantity: Decimal
    FilledAvgPrice: Decimal
    RemainLocked: Decimal
    Leverage: int
    Status: str
    OrderType: str
    CostFee: Decimal
    LockedFee: Decimal
    Created_at: str
    Ttl: int

class Position(NamedTuple):
    Id: int
    Owner: str
    PairId: str
    Direction: str
    EntryPrice: Decimal
    MarkPrice: Decimal
    LiquidationPrice: Decimal
    BaseQuantity: Decimal
    Margin: Decimal
    Leverage: int
    UnrealizedPnl: Decimal
    MarginRate: Decimal
    InitialMargin: Decimal
    PendingOrderQuantity: Decimal
