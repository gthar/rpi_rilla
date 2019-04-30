#!/usr/bin/env python3

import time
import threading

class Threadable:
    def __init__(self):
        self.stopper = threading.Event()

    def start(self):
        threading.Thread(target=self.target).start()

    def stop(self):
        self.stopper.set()

    def loop(selt):
        time.sleep(1)

    def target(self):
        while not self.stopper.is_set():
            self.loop()
