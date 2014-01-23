__author__ = 'David Jonas'

import time
import RPi.GPIO as GPIO
import threading

class WeatherStation(threading.Thread):

    STEP = 1000
    revs = 0
    current = int(time.time()*1000)
    nextStep = current + STEP
    val = 1
    prevVal = 1
    speedPin = 27
    directionPin = 17
    _windSpeedCallbacks = []
    _windDirectionCallbacks = []
    exitFlag = False


    def __init__(self, speedPin = 27, directionPin = 17, windSpeedCallback = None, windDirectionCallback = None):
        threading.Thread.__init__(self)
        self.speedPin = speedPin
        self.directionPin = directionPin

        if windSpeedCallback is not None:
            self._windSpeedCallbacks.append(windSpeedCallback)
        else:
            self._windSpeedCallbacks = []

        if windDirectionCallback is not None:
            self._windDirectionCallbacks.append(windDirectionCallback)
        else:
            self._windDirectionCallbacks = []

    def run(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        #Wind speed reading
        GPIO.setup(self.speedPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        while True:
            if self.exitFlag:
                break
            self.current = int(time.time()*1000)
            self._speed_interrupt()
            if self.current > self.nextStep:
                self._on_wind_speed_update(self._calcSpeed())
                self.nextStep = self.current + self.STEP
            time.sleep(0.1)

    def _speed_interrupt(self):
        self.val = GPIO.input(self.speedPin)
        if self.prevVal == 1 and self.val == 0:
            self.revs = self.revs + 1
        self.prevVal = self.val

    def _calcSpeed(self):
        base = 24011
        speed = base * self.revs
        self.revs = 0
        return speed / 1000

    def add_wind_speed_callback(self, callback):
        self._windSpeedCallbacks.append(callback)

    def add_wind_direction_callback(self, callback):
        self._windDirectionCallbacks.append(callback)

    def _on_wind_speed_update(self, value):
        for cb in self._windSpeedCallbacks:
            cb(value)

    def _on_wind_direction_update(self, value):
        for cb in self._windDirectionCallbacks:
            cb(value)

    def kill(self):
        self.exitFlag = True



