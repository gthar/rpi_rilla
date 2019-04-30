#!/usr/bin/env python3

import socket
import sys

from rpi_rilla.helpers import get_config

sep = "_"


def send_msg(msg, host, port):
    s = socket.socket()

    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        print("server not running")
        s.close()
        return 1

    s.send(msg.encode())
    s.close
    return 0


def main(defaults):
    config = get_config(defaults)

    cmds = sys.argv[1:]
    if len(cmds) == 0:
        print("no message given")
        return 2
    msg = sep.join(cmds)

    return send_msg(msg, config["host"], config["port"])
