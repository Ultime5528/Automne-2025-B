
from wpilib import VictorSP

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Flywheel(Subsystem):

    FWspeed = autoproperty(0.2)

    def  __init__(self):

        super().__init__()

        self.motor = VictorSP(ports.SIM.flywheel_motor)


    def startFw(self):
        self._motor.setspeed(self.FWspeed)

    def stopFw(self):
        self._motor.stopMotor()
