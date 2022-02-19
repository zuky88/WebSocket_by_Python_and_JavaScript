#!/usr/bin/env python3

import asyncio
import websockets
import sys
import time
import datetime

ADDRESS = '127.0.0.1'
PORT = 60000
BUFSIZE = 4096

event = asyncio.get_event_loop()
uri = 'ws://' + ADDRESS + ':' + str(PORT)
server = event.run_until_complete(websockets.connect(uri))

async def clientMain():
    data = 0
    while True:
        time.sleep(1)
        data += 1
        await server.send(str(data).encode("UTF-8"))
        now = datetime.datetime.now()
        print('[client]Send:{0} [{1}]'.format(data, now))
        msg = await server.recv()
        print('[client]Recv:{0} [{1}]'.format(msg, now))

if __name__ == '__main__':
    try:
        event.run_until_complete(clientMain())
        event.run_forever()
    except KeyboardInterrupt:
        event.run_until_complete(server.close())
        event.close()
        print('[clientA]Socket close.')
        sys.exit(1)
