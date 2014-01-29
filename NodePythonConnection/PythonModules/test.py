from weather_station import WeatherStation
import time
import os

sound=1

def speedUpdate(value):
	global sound
	print "Wind speed: %s" % value
	if value > 60:
		os.system('mpg321 mxline%d.mp3'%sound)
		
def directionUpdate(value):
	global sound
	print "Wind direction: %s" % value
	if value in range(1020, 1023):
		sound=1
	elif value in range(880, 890):
		sound=2
	elif value in range(340, 350):
		sound=3
	else:
		sound=4	
	print 'sound %d'%sound	

ws = WeatherStation(windSpeedCallback=speedUpdate, windDirectionCallback=directionUpdate)

print "starting weather station thread."
ws.start()


while True:
	try:
		time.sleep(25)
	except KeyboardInterrupt:
		break
print "Done, killing threads"
ws.kill()
