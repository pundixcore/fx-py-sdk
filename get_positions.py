import grpc
import grpc_client
import wallet


channel = grpc.insecure_channel('44.196.199.119:9090')
address = "dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy"
#address = "dex1nasudt9lptq77t9yjzsfvzm8vppjtqqv63eg62"
#address = "dex1ggz598a4506llaglzsmhp3r23hfke6nw29wans"
seed = "crime indicate code innocent brush loud among labor girl print solar flower visit ridge garage scan visual finger gaze rack toy road mimic divorce"

balances = grpc_client.query_all_balances(channel=channel, address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
print(balances)

account = grpc_client.query_account_info(channel=channel, address="dex1v0zwwfe3gw2fqdhdnx0hcurh2gzz98z8dagewy")
print(account)

priv_key = wallet.seed_to_privkey(seed)
accAddress = priv_key.to_address()
print(accAddress)
print(address)

#position = grpc_client.QueryPositionsReq(channel=channel, owner=address)
position = grpc_client.QueryPositionsReq(channel=channel, owner=accAddress)