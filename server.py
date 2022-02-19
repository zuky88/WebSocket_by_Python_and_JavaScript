#!/usr/bin/env python3

import asyncio
import websockets
import datetime
import sys

ADDRESS = '127.0.0.1'
PORT = 60000

event = asyncio.get_event_loop()

async def serverMain(client, address):
    while True:
        msg = await client.recv()
        now = str(datetime.datetime.now())
        print("[server ]Recv :{0}[{1}]".format(str(msg), now))
        sendm = 'Server got data ' + str(msg)
        await client.send(sendm)
        now = str(datetime.datetime.now())
        print("[server ]Send :{0}[{1}]".format(str(sendm), now))

if __name__ == '__main__':
    try:
        startServer = websockets.serve(serverMain, ADDRESS, PORT)
        print('[server]Waiting access from client.')
        event.run_until_complete(startServer)
        event.run_forever()
    except KeyboardInterrupt:
        print('[clientA]Socket close.')
        sys.exit(1)





