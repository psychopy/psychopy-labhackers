from psychopy.experiment.components.buttonBox import ButtonBoxBackend, ButtonBoxComponent
from psychopy.experiment import getInitVals, Param
from psychopy.localization import _translate


class MillikeySerialButtonBoxBackend(
    ButtonBoxBackend, key="millikeySerial", label="Labhackers Millikey (Serial)"
):
    """
    """

    def getParams(self: ButtonBoxComponent):
        # define order
        order = [
            "millikeySerialPort",
        ]
        # define params
        params = {}
        def getPorts():
            from psychopy_labhackers.millikey import MillikeySerialButtonGroup
            profiles = MillikeySerialButtonGroup.getAvailableDevices()
            return [prof['port'] for prof in profiles]
        params['millikeySerialPort'] = Param(
            "", valType="str", inputType="choice", categ="Device",
            allowedVals=getPorts,
            label=_translate("COM port"),
            hint=_translate(
                "Serial port to connect to"
            )
        )
        # define depends
        depends = []

        return params, order, depends

    def addRequirements(self: ButtonBoxComponent):
        self.exp.requireImport(
            importName="millikey", importFrom="psychopy_labhackers"
        )

    def writeDeviceCode(self, buff):
        # get inits
        inits = getInitVals(self.params)
        # make ButtonGroup object
        code = (
            "deviceManager.addDevice(\n"
            "    deviceClass='psychopy_labhackers.millikey.MillikeySerialButtonGroup',\n"
            "    deviceName=%(deviceName)s,\n"
            "    port=%(millikeySerialPort)s,\n"
            "    channels=%(nButtons)s\n"
            ")\n"
        )
        buff.writeOnceIndentedLines(code % inits)
