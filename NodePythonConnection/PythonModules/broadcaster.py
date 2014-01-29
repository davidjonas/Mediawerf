__author__ = 'David Jonas'

from socketIO_client import SocketIO
import sys


class Broadcaster(object):
    port = 8080
    host = "localhost"

    def __init__(self, port=8080, host="localhost"):
        self.port = port
        self.host = host
        self.socketIO = SocketIO(host, port)

        self.socketIO.on("ack", self.logACK)

    def logAck(self, data):
        print("Acknowledgement received for %s" % data['original'])

    def emit(self, event, data):
        self.socketIO.emit(event, data)

    def on(self, event, callback):
        self.socketIO.on(event, callback)