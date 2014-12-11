__author__ = 'David Jonas'

from socketIO_client import SocketIO
import sys


class Broadcaster(object):
    port = 8080
    host = "localhost"

    def __init__(self, port=8080, host="localhost"):
        self.port = port
        self.host = host
        self.socketIO = SocketIO(host, int(port), transports=['websocket', 'polling'])

        self.socketIO.on("ack", self.logACK)

    def logACK(self, data):
        print("Acknowledgement received for %s" % data['original'])

    def emit(self, event, data):
        self.socketIO.emit(event, data)

    def on(self, event, callback):
        self.socketIO.on(event, callback)

    def wait(self, millis):
        self.socketIO.wait(millis)

    def wait_forever(self):
        self.socketIO.wait()
