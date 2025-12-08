from rev import SparkMax
from wpiutil import SendableBuilder

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Pulley(Subsystem):

    pulley_speed = autoproperty(0.12)
    maintain_speed = autoproperty(-0.02)

    def __init__(self):

        super().__init__()

        self._motor = SparkMax(ports.CAN.pulley_motor, SparkMax.MotorType.kBrushless)

    def pulleyUp(self):
        self._motor.set(-self.pulley_speed)

    def pulleyDown(self):
        self._motor.set(self.pulley_speed)

    def stop(self):
        self._motor.stopMotor()

    def maintain(self):
        self._motor.set(self.maintain_speed)

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("pulley_motor", self._motor.get, noop)
