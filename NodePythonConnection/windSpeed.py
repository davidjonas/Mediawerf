import RPi.GPIO as GPIO
import time

GPIO.cleanup()

STEP = 1000
revs = 0
current = int(time.time()*1000)
nextStep = current + STEP
val = 1
prevVal = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def countRevs(channel):
	global revs
	revs=revs+1
	#print "Rev!!!"

def calcSpeed():
	global revs
	base = 24011
	speed = base * revs
	revs = 0
	return speed / 1000

def interrupt():
	global prevVal
	global val	
	val = GPIO.input(23)
	#print val
	#import pdb; pdb.set_trace()
	if prevVal == 1 and val == 0:
		countRevs(1)
	prevVal = val
	

#GPIO.add_event_detect(23, GPIO.FALLING, callback=countRevs, bouncetime=100)
#GPIO.add_event_detect(23, GPIO.BOTH)
#GPIO.add_event_callback(23, countRevs, 100)

while True:
	current = int(time.time()*1000)
	interrupt()
	if current > nextStep:	
		print calcSpeed()
		nextStep = current + STEP

