#!/usr/bin/env python3

import datetime
import os
from PyQt4 import QtGui, QtCore
from threading import Timer

from rpi_rilla.socket_sender import send_msg


def get_sleep_time(wakeup_str):
    h, m = map(int, wakeup_str.split(":"))
    now = datetime.datetime.today()
    wakeup_time = datetime.datetime(now.year, now.month, now.day, h, m)
    if now.hour > h or (now.hour == h and now.minute >= m):
        wakeup_time += datetime.timedelta(days=1)
    res = (wakeup_time - now).total_seconds()
    #res = 5
    return res


class State:
    def __init__(self):
        # sleeping | waking | snoozing | awake | standby
        self.val = None
        self.wait_time = 0
        self.action = lambda: None

    def set_val(self, x):
        self.val = x
    def get_wait(self):
        return self.wait_time
    def get_action(self):
        return self.action

    def get_val(self):
        return self.val
    def set_wait(self, x):
        self.wait_time = x
    def set_action(self, x):
        self.action = x


def light_on(config):
    print("light on")
    send_msg("1_on", config["host"], config["port"])


def light_off(config):
    print("light off")
    send_msg("1_off", config["host"], config["port"])
    send_msg("2_off", config["host"], config["port"])


def screen_on(config):
    print("screen on")
    send_msg("on", config["host"], config["port"])


def screen_off(config):
    print("screen off")
    send_msg("off", config["host"], config["port"])


def make_worker(f, config, player, state, status, wait_time=0, post_action=lambda: None):
    def inner():
        f(config, player)
        state.set_wait(wait_time)
        state.set_action(post_action)
        state.set_val(status)
        print(state.get_val())
    return inner


def good_night(config, player):
    screen_off(config["screen"])
    light_off(config["light"])
    print("sleep tight tupper")


def wake_up(config, player):
    screen_on(config["screen"])
    print("music on")
    player.play()
    light_on(config["light"])
    print("good morning!")


def snooze(config, player):
    screen_off(config["screen"])
    light_off(config["light"])
    print("music muted")
    player.pause()
   

def im_awake(config, player):
    print("music off")
    player.quit()
    light_off(config["light"])
    screen_on(config["screen"])
    print("so you are awake...")


def dummy_timer():
    return Timer(0, lambda: _)


def alarm_controller(snoozer, cleanup, default_snooze_time):
    def f(cmd, *args):
        if cmd == "snooze":
            try:
                snooze_time = int(args[0])
            except (ValueError, IndexError):
                snooze_time = default_snooze_time
            return snoozer(snooze_time)
        elif cmd == "awake":
            return cleanup
        else:
            return None
    return f


def read_from_popup(default="", txt="", width=100, height=50):
    text = ""
    app = QtGui.QApplication([])
    w = QtGui.QMainWindow()
    w.resize(width, height)
    w.setWindowTitle(txt)
    input = QtGui.QLineEdit(w)
    input.resize(width, heigth)
    input.setAlignment(QtCore.Qt.AlignCenter)
    input.setText(default)

    @QtCore.pyqtSlot()
    def enter():
        nonlocal text
        text = input.text()
        w.close()

    input.returnPressed.connect(enter)
    w.show()
    app.exec_()
    return text


def read_wakeup_time(default, txt):
    if "DISPLAY" in os.environ.keys():
        return read_from_popup(default, txt)
    else:
        print(txt)
        return(input('>'))


defaults = {"config file": "/usr/local/etc/rpi_rilla/alarm.yaml",
            "host":        "127.0.0.1",
            "port":        None,
            "snooze time": 600,
            "sleep time":  5,
            "wakeup time": "8:00",
            "waking time": 600,
            "song":        None}
