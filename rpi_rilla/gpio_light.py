#!/usr/bin/env python3

import yaml

light_actions = {"on":     lambda x: x.set_on(),
                 "off":    lambda x: x.set_off(),
                 "toggle": lambda x: x.toggle()}


def set_lights(lights):
    def f(idx, cmd):
        try:
            i = int(idx)
            light = lights[i-1]
            action = light_actions[cmd]
        except (ValueError, IndexError, KeyError):
            return None
        return lambda: action(light)
    return f


def get_light_state(id, config):
    try:
        with open(config["state file"]) as fh:
            res = yaml.load(fh)[id]
        assert type(res) is bool
        return res
    except (FileNotFoundError, KeyError, AssertionError):
        return config["default{0}".format(id)]


defaults = {"default1":    False,
            "default2":    False,
            "pin1":        None,
            "pin2":        None,
            "port":        10203,
            "host":        "127.0.0.1",
            "state file":  "/usr/local/etc/rpi_rilla/light_state.yaml",
            "config file": "/usr/local/etc/rpi_rilla/gpio_light.yaml"}
