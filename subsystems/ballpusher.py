from wpilib import VictorSP
from wpiutil import SendableBuilder

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class BallPusher(Subsystem):

    def __init__(self):

        super().__init__()

        self._motor = VictorSP(ports.SIM.ballpusher_motor)

    def push(self, speed : float):
        self._motor.set(speed)

    def retract(self, speed : float):
        self._motor.set(-float(speed))

    def stop(self):
        self._motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("ballpusher_motor", self._motor.get, noop)
