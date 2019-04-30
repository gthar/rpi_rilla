#!/usr/bin/env python3

import time
from rpi_rilla.threadable import Threadable

class CountDown(Threadable):
    def __init__(self, count, step=1, action=lambda: None):
        self.count = count
        self.step = step
        self.state = count
        self.action = action
        self.running = True
        super().__init__()

    def advance(self):
        """
        Advance time and report whether the time is finished
        """
        still_running = self.running
        time_over = self.state <= 0

        if time_over:
            self.running = False

        if still_running:
            print(self.state)
            self.state -= self.step

        time.sleep(self.step)
        return still_running and time_over

    def reset(self):
        self.running = True
        self.state = self.count

    def pause(self):
        self.running = False

    def loop(self):
        if self.advance():
            self.action()
