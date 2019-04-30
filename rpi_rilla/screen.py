#!/usr/bin/env python3

import os

class Screen:
    """
    We can turn off the screen with tvservice
    """
    def __init__(self, state=True, target_state=True):
        self.state = state
        self.target_state = target_state

    def turn_on(self):
        self.state = True
        print("turning screen on")
        os.system('/usr/bin/tvservice -e "DMT 47"')
        os.system("/bin/chvt 2")
        os.system("/bin/chvt 1")

    def turn_off(self):
        self.state = False
        print("turning screen off")
        os.system("/usr/bin/tvservice -o")

    def turn(self, new_state):
        """
        Method used to control the 'state' of the screen
        """
        if new_state and not self.state:
            self.turn_on()

        elif not new_state and self.state:
            self.turn_off()

    def reset(self):
        """
        Set the current screen state to its target state
        """
        self.turn(self.target_state)

    def turn_target(self, new_state):
        """
        Method used to control the 'target_state' of the screen
        """
        self.target_state = new_state
        self.reset()

    def toggle(self):
        self.turn(not self.state)

    def toggle_target(self):
        self.turn_target(not self.target_state)
