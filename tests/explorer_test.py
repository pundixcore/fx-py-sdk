import asyncio
from fx_py_sdk.explorer import DexExploer

loop = None

async def main():
    global loop
    e = DexExploer()
    await e.explorer()

    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(10)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())