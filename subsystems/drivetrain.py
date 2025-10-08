from wpilib import VictorSP

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem


class Drivetrain(Subsystem):

    motor_speed = autoproperty(0.2)

    def __init__(self):

        super().__init__()

        self._motor = VictorSP(ports.SIM.drivetrain_motor)

    def goForward(self):
        self._motor.set(self.motor_speed)

    def goBackward(self):
        self._motor.set(-self.motor_speed)

    def StopMotors(self):
        self._motor.stopMotor()
