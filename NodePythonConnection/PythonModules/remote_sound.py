__author__ = 'David Jonas'

import sys
import time
from broadcaster import Broadcaster
import termios, fcntl, os

port = 8080
host = "localhost"
#read port from commandline python remote_sound.py host 8080
if len(sys.argv) >= 3:
    try:
        port = int(sys.argv[2])
        host = sys.argv[1]
    except:
        print("Argument error, Usage: python wind_managment.py host port")


com = Broadcaster(port=port, host=host)


def updateSpeed(data):
    val = data["value"]
    print "windSpeed: %s" % val


def updateDirection(data):
    val = data["value"]
    print "windDirection: %s" % val

def handle(key):
    print "Key pressed: " % key

com.on("windSpeedUpdate", updateSpeed)
com.on("windDirectionUpdate", updateDirection)
com.wait_forever()

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            handle(c)
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

