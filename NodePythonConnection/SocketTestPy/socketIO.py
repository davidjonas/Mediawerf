import websocket
import thread
import time
import sys
from urllib import *


class SocketIO:
    def __init__(self, host, port):
        self.PORT = port
        self.HOSTNAME = host
        self.connect()

    def __del__(self):
        self.close()

    def handshake(self,host,port):
        u = urlopen("http://%s:%d/socket.io/1/" % (host, port))
        if u.getcode() == 200:
            response = u.readline()
            (sid, hbtimeout, ctimeout, supported) = response.split(":")
            supportedlist = supported.split(",")
            if "websocket" in supportedlist:
                return (sid, hbtimeout, ctimeout)
            else:
                raise TransportException()
        else:
            raise InvalidResponseException()

    def connect(self):
        try:
            (sid, hbtimeout, ctimeout) = self.handshake(self.HOSTNAME, self.PORT) #handshaking according to socket.io spec.
            self.ws = websocket.create_connection("ws://%s:%d/socket.io/1/websocket/%s" % (self.HOSTNAME, self.PORT, sid))
        except Exception as e:
            print e
            sys.exit(1)

    def heartbeat(self):
        self.ws.send("2::")

    def send(self,event,message):
        self.heartbeat()
        self.ws.send('5:1::{"name":"%s","args":"%s"}' % (event, message))

    def close(self):
        if hasattr(self, 'ws'):
            self.ws.close()