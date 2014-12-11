from weather_station import WeatherStation
from broadcaster import Broadcaster
import time
import os
import logging
logging.basicConfig(level=logging.DEBUG)

com = Broadcaster()


def speedUpdate(value):
    global sound
    #print "Wind speed: %s" % value
    com.emit("windSpeedUpdate", {'value': value})

def directionUpdate(value):
    global sound
    #print "Wind direction: %s" % value
    com.emit("windDirectionUpdate", {'value': value})


ws = WeatherStation(windSpeedCallback=speedUpdate, windDirectionCallback=directionUpdate)
print "starting weather station thread."
ws.start()

com.wait_forever()

while True:
    try:
        time.sleep(25)
    except KeyboardInterrupt:
        break


print "Done, killing threads"
ws.kill()
