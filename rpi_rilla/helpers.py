#!/usr/bin/env python3

import yaml


def read_config(f, **defaults):
    with open(f) as fh:
        config = yaml.load(fh)
    for k, v in config.items():
        defaults[k] = v
    for k, v in defaults.items():
        if v is None:
            raise Exception("unspeciefied value for {0}".format(k))
    return defaults


def get_config(defaults):
    return read_config(defaults["config file"], **defaults)


def assoc (**d):
    def f(x):
        try:
            return d[x]
        except KeyError:
            return None
    return f


def update_yaml(f, k, v):
    try:
        with open(f, 'r') as fh:
            d = yaml.load(fh)
    except FileNotFoundError:
        d = {}
    if d is None:
        d = {}
    d[k] = v
    with open(f, 'w') as fh:
        fh.write(yaml.dump(d, default_flow_style=False))
