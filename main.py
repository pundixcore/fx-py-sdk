import grpc
from cosmos.auth.v1beta1.auth_pb2 import BaseAccount

from cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest
from cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest

from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub as BankQuery

from cosmos.auth.v1beta1.query_pb2_grpc import QueryStub as AuthQuery

def query_all_balances(channel, address):
    """查询用户所有的余额"""
    stub = BankQuery(channel)
    response = stub.AllBalances(QueryAllBalancesRequest(address=address))
    print("Address All Balances:", response.balances)


def query_account_info(channel, address):
    """查询用户信息"""
    client = AuthQuery(channel)
    response = client.Account(QueryAccountRequest(address=address))
    # Any 类型转换 - BaseAccount
    baseAccount = BaseAccount()
    response.account.Unpack(baseAccount)
    print("Account Data")
    print("Address", baseAccount.address)
    print("accountNumber", baseAccount.account_number)
    print("Sequence", baseAccount.sequence)

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:9090')

    query_all_balances(channel=channel, address="fx1gkfjjmnlfnur2xwynhj80m7kctalmsyxkrthpg")

    query_account_info(channel=channel, address="fx1gkfjjmnlfnur2xwynhj80m7kctalmsyxkrthpg")

