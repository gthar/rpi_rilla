#!/usr/bin/env python3

import time
import sys

from rpi_rilla.socket_handler import SocketHandler
from rpi_rilla.light import Light
from rpi_rilla.gpio_light import defaults, set_lights, get_light_state
from rpi_rilla.helpers import get_config


def main ():
    config = get_config(defaults)

    lights = [Light(id,
                    config["pin{0}".format(id)],
                    get_light_state(id, config),
                    config["state file"])
              for id in [1, 2]]

    socket_handler = SocketHandler(set_lights(lights),
                                   port = config["port"],
                                   host = config["host"])
    socket_handler.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        socket_handler.stop()
        return 0

if __name__ == "__main__":
    sys.exit(main())

