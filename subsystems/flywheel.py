from wpilib import VictorSP
from wpiutil import SendableBuilder

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Flywheel(Subsystem):

    motor_speed = autoproperty(0.2)

    def __init__(self):

        super().__init__()

        self._motor = VictorSP(ports.SIM.flywheel_motor)

    def startMotor(self):
        self._motor.set(self.motor_speed)

    def stop(self):
            self._motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("flywheel_motor", self._motor.get, noop)
