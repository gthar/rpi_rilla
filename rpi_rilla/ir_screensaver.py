#!/usr/bin/env python3

import glob
import yaml


def activity(screen, clock):
    def f():
        clock.reset()
        screen.reset()
    return f


def iddle(screen):
    return lambda: screen.turn(False)


def set_on(screen, clock):
    def f():
        clock.reset()
        screen.turn_target(True)
    return f


def set_off(screen):
    return lambda: screen.turn_target(False)


def toggle(screen):
    return lambda: screen.toggle_target()


defaults = {"default state": True,
            "idle time":     10,
            "sensor pin":    None,
            "port":          10000,
            "host":          "127.0.0.1",
            "config file":   "/usr/local/etc/rpi_rilla/ir_screensaver.yaml"}
