from wpilib import VictorSP

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Pulley(Subsystem):

    PulleySpeed = autoproperty(0.1)

    def __init__(self):

        super().__init__(self)

        self.motor = VictorSP(ports.SIM.pulley_motor)

    def startPulley(self):
        self._motor.setspeed(self.PulleySpeed)



    def stopPulley(self):
        self._motor.stopMotor()
