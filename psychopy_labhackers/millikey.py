from psychopy import logging, core
from psychopy.hardware import serialdevice as sd
from psychopy.tools import systemtools as st
from psychopy.hardware.button import KeyboardButtonBox, BaseButtonGroup, ButtonResponse


class MillikeyHIDButtonGroup(KeyboardButtonBox):
    def __init__(self, buttons=(1, 2, 3, 4, 5, 6, 7, 8)):
        # initialise base class
        KeyboardButtonBox.__init__(self, buttons=buttons)


class MillikeySerialButtonGroup(BaseButtonGroup):
    def __init__(self, port=None, channels=8):
        BaseButtonGroup.__init__(self)
        # get port if not given
        if port is None:
            profiles = self.getAvailableDevices()
            if len(profiles):
                port = profiles[0]['port']
        # if port is still None by here, there's not a device connected
        if port is None:
            raise ConnectionError("Could not detect any Millikey device. Try ")
        # setup serial
        self.serial = sd.SerialDevice(port=port)
        # setup clock
        self.clock = core.Clock()

    def resetTimer(self, clock=logging.defaultClock):
        self.clock.reset(clock.getTime())

    @staticmethod
    def getAvailableDevices():
        devices = []
        for profile in st.systemProfilerWindowsOS(classname="Ports", connected=True):
            # identify by driver name
            if "usbser.inf" not in profile['Driver Name']:
                continue
            # find "COM" in profile description
            desc = profile['Device Description']
            start = desc.find("COM") + 3
            end = desc.find(")", start)
            # if there's no reference to a COM port, skip
            if -1 in (start, end):
                continue
            # get COM port number
            num = desc[start:end]
            devices.append({
                'deviceName': profile['Instance ID'],
                'port': f"COM{num}",
            })

        return devices

    def dispatchMessages(self):
        for message in self.serial.getResponse(length=2):
            resp = self.parseMessage(message)
            self.receiveMessage(resp)

    def parseMessage(self, message):
        keyNum = int(message)
        state = not self.getState(keyNum)
        return ButtonResponse(self.clock.getTime(), state, keyNum)
