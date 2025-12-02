from wpilib import VictorSP
from wpiutil import SendableBuilder

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Pulley(Subsystem):

    PulleySpeed = autoproperty(0.1)

    def __init__(self):

        super().__init__()

        self._motor = VictorSP(ports.SIM.pulley_motor)

    def pulleyUp(self):
        self._motor.set(self.PulleySpeed)

    def pulleyDown(self):
        self._motor.set(-self.PulleySpeed)

    def stop(self):
        self._motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("pulley_motor", self._motor.get, noop)
