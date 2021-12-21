import asyncio
from fx_py_sdk import ws

loop = None

async def main():
    ws.DexScan()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())