#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
from rpi_rilla.threadable import Threadable

GPIO.setmode(GPIO.BOARD)

class Sensor(Threadable):
    def __init__(self, pin, action=lambda: None):
        GPIO.setup(pin, GPIO.IN)
        self.pin = pin
        self.action = action
        super().__init__()

    def sense(self):
        return bool(GPIO.input(self.pin))

    def loop(self):
        if self.sense():
            self.action()
        time.sleep(0.1)
