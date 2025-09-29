from ultime.immutable import Immutable

"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    shooter_motor = 0
    drivetrain_motor_fr = 1
    drivetrain_motor_rr = 2
"""


class CAN(Immutable):
    pass

class PWM(Immutable):
    pass

class DIO(Immutable):
    pass

class PDP(Immutable):
    pass

class SIM(Immutable):
    flywheel_motor = 1