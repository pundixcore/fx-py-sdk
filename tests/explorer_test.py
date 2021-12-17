import asyncio
from fx_py_sdk.explorer import DexExploer
from fx_py_sdk.rpc.websockets import WebsocketRpcClient

loop = None

async def main():
    global loop
    e = DexExploer()
    await e.explorer()

    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(20, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())