from rev import SparkMax
from wpiutil import SendableBuilder

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Drivetrain(Subsystem):

    motor_speed = autoproperty(0.5)

    def __init__(self):

        super().__init__()

        self._motor = SparkMax(ports.CAN.drivetrain_motor, SparkMax.MotorType.kBrushless)

    def goForward(self):
        self._motor.set(self.motor_speed)

    def goBackward(self):
        self._motor.set(-self.motor_speed)

    def stop(self):
        self._motor.stopMotor()

    def initSendable(self, builder: SendableBuilder) -> None:
        def noop(_): pass
        builder.addFloatProperty("drive_motor", self._motor.get, noop)
