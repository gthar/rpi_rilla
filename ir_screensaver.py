#!/usr/bin/env python3

###############################################################################

import sys
import time

from rpi_rilla.ir_screensaver import defaults, iddle, activity, set_on, set_off, toggle
from rpi_rilla.helpers import get_config, assoc
from rpi_rilla.screen import Screen
from rpi_rilla.sensor import Sensor
from rpi_rilla.socket_handler import SocketHandler
from rpi_rilla.count_down import CountDown

###############################################################################

def main ():
    config = get_config(defaults)

    screen = Screen(state=True, target_state=config["default state"])
    iddle_seconds = config["idle time"] * 60
    clock = CountDown(iddle_seconds, 1, iddle(screen))
    sensor = Sensor(config["sensor pin"], activity(screen, clock))

    socket_handler = SocketHandler(assoc(wake   = activity(screen, clock),
                                         on     = set_on(screen, clock),
                                         off    = set_off(screen),
                                         toggle = toggle(screen)),
                                   port = config["port"],
                                   host = config["host"])

    clock.start()
    sensor.start()
    socket_handler.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clock.stop()
        sensor.stop()
        socket_handler.stop()
        return 0


if __name__ == "__main__":
    sys.exit(main())

###############################################################################
