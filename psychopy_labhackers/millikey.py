from psychopy import logging
from psychopy.hardware.button import KeyboardButtonBox, ButtonResponse


class MillikeyHIDButtonGroup(KeyboardButtonBox):
    def __init__(self, buttons=(1, 2, 3, 4, 5, 6, 7, 8)):
        # initialise base class
        KeyboardButtonBox.__init__(self, buttons=buttons)

    def resetTimer(self, clock=logging.defaultClock):
        pass

    @staticmethod
    def getAvailableDevices():
        devices = []

        return devices
