from wpilib import VictorSP
from wpiutil import SendableBuilder

import ports
from ultime.subsystem import Subsystem


class Flywheel(Subsystem):

    def __init__(self):

        super().__init__()

        self._motor = VictorSP(ports.SIM.flywheel_motor)

    def start(self, speed : float):
        self._motor.set(speed)

    def stop(self):
            self._motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("flywheel_motor", self._motor.get, noop)
