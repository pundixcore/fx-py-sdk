import logging
from typing import Generic, TypeVar

from fxdex.client import QueryClient, TransactionClient
from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQueryStub
from cosmos.bank.v1beta1.tx_pb2_grpc import MsgStub as BankMsgStub
from fx.dex.query_pb2_grpc import QueryStub
from fx.dex.tx_pb2_grpc import MsgStub
from fxdex.cosmos import (
    PATH,
    BIP32DerivationError,
    generate_wallet,
    privkey_to_pubkey,
    pubkey_to_address,
    seed_to_privkey,
)

# fxdex.cosmos package contains a modified version of the original cosmospy library
# (https://github.com/hukkin/cosmospy) to handle customized fxdex transactions.
from fxdex.cosmos.typing import Wallet
from fxdex.tendermint import Tendermint34Client
from fxdex.utils import get_logger

Q = TypeVar("Q")
TX = TypeVar("TX")


class FxdexSDK(Generic[Q, TX]):
    q: Q
    tx: TX


class Fxdex:
    dex: FxdexSDK
    bank: FxdexSDK
    wallet: Wallet
    """Bluzelle is the main class for accessing Bluzelle SDKs."""

    def __init__(
        self,
        mnemonic: str,
        host: str,
        port: int,
        max_gas: int,
        gas_price: float,
        logging_level: int = logging.INFO,
    ):
        """Crating new Bluzelle instance.

        Args:
            mnemonic: Optional user provided mnemonic for deriving the wallet.
            host: Tendermint host for making rpc calls.
            port: Tendermint rpc port.
            max_gas: Maximum allowed gas limit for sending transaction.
            gas_price: Gas price in ubnt.

        Returns:
            New instance of the Bluzelle API.
        """
        self.wallet = Wallet()
        if mnemonic is None:
            # Generating a random wallet.
            w = generate_wallet()
            self.wallet.seed = w["seed"]
            self.wallet.private_key = w["private_key"]
            self.wallet.address = w["address"]
            self.wallet.public_key = w["public_key"]
            self.wallet.derivation_path = w["derivation_path"]
        else:
            try:
                privkey = seed_to_privkey(mnemonic)
                pubkey = privkey_to_pubkey(privkey)
                addr = pubkey_to_address(pubkey)
                self.wallet.derivation_path = PATH
                self.wallet.seed = mnemonic
                self.wallet.private_key = privkey
                self.wallet.address = addr
                self.wallet.public_key = pubkey
            except BIP32DerivationError:
                get_logger("fxdex").error("No valid private key in this derivation path!")

        # Creating a Tendermint RPC client.
        self.tendermint34Client = self.create_tendermint_client(
            host=host, port=port, logging_level=logging_level
        )

        # Creating grpc Query clients.
        self.query_client = QueryClient(self.tendermint34Client, logging_level)
        self.tx_client = TransactionClient(
            self.tendermint34Client,
            self.query_client,
            self.wallet,
            max_gas,
            gas_price,
            logging_level,
        )

        # Defining the db SDK.
        self.dex = FxdexSDK[QueryStub, MsgStub]()
        self.dex.q = QueryStub(self.query_client)
        self.dex.with_transactions = self.tx_client.with_transactions
        self.dex.tx = MsgStub(self.tx_client)

        # Defining the bank SDK
        self.bank = FxdexSDK[BankQueryStub, BankMsgStub]()
        self.bank.q = BankQueryStub(self.query_client)
        self.bank.with_transactions = self.tx_client.with_transactions
        self.bank.tx = BankMsgStub(self.tx_client)

    def create_tendermint_client(self, host, port, logging_level: int):
        """Tendermint is the transport for making grpc calls, sending new tx,
        ..."""
        return Tendermint34Client(host, port, logging_level)

