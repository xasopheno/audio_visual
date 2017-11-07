import asyncio
import websockets

async def sendFreq(websocket, path):
    freq = await websocket.recv()
    print(freq)

    # greeting = "Hello {}!".format(name)
    # await websocket.send(greeting)
    # print("> {}".format(greeting))

start_server = websockets.serve(sendFreq, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
