#!/usr/bin/env python3

import RPi.GPIO as GPIO
from rpi_rilla.helpers import update_yaml

GPIO.setmode(GPIO.BOARD)


class Light:
    def __init__(self, id, pin, default, state_file):
        GPIO.setup(pin, GPIO.OUT)
        self.id = id
        self.pin = pin
        self.state_file = state_file
        self.set(default)

    def update (self):
        update_yaml(self.state_file, self.id, self.state)
        GPIO.output(self.pin, not self.state)

    def set (self, x):
        self.state = x
        self.update()

    def set_on(self):
        print("turning light on")
        self.set(True)

    def set_off(self):
        print("turning light off")
        self.set(False)

    def toggle(self):
        self.set(not self.state)
