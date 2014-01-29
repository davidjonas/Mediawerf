__author__ = 'David Jonas'

import sys
import time
from broadcaster import Broadcaster
from audio_control import AudioController

port = 8080
host = "localhost"
last_dir = "N"

#read port from commandline python remote_sound.py host 8080
if len(sys.argv) >= 3:
    try:
        port = int(sys.argv[2])
        host = sys.argv[1]
    except:
        print("Argument error, Usage: python wind_managment.py host port")


def updateSpeed(data):
    val = data["value"]
    #print "windSpeed: %s" % val
    ac.set_volume("bg02.wav", val/50, fade=2.0)
    ac.set_volume("bg01.wav", val/50 + 0.3, fade=2.0)



def updateDirection(data):
    global last_dir
    global ac
    val = data["value"]
    #print "windDirection: %s" % val
    if val != last_dir:
        if val == "N":
            ac.go_to_seconds("sample2.wav", 0)
            ac.play_sound("sample2.wav")
        elif val == "S":
            ac.go_to_seconds("sample3.wav", 0)
            ac.play_sound("sample3.wav")
        elif val == "E":
            ac.go_to_seconds("sample4.wav", 0)
            ac.play_sound("sample4.wav")
        elif val == "W":
            ac.go_to_seconds("sample5.wav", 0)
            ac.play_sound("sample5.wav")
    last_dir = val

ac = AudioController()

print "Loading sounds..."
ac.add_sound("bg01.wav")
ac.add_sound("bg02.wav")
ac.add_sound("sample2.wav")
ac.add_sound("sample3.wav")
ac.add_sound("sample4.wav")
ac.add_sound("sample5.wav")
ac.play_sound("bg01.wav", loops=-1)
ac.play_sound("bg02.wav", loops=-1)
ac.set_volume("bg02.wav",0.0)
print("finished loading sounds.")

print "Starting communications..."
com = Broadcaster(port=port, host=host)
com.on("windSpeedUpdate", updateSpeed)
com.on("windDirectionUpdate", updateDirection)
print "communications established."
print "Enjoy..."

com.wait_forever()

print "Finished"