from commands2 import Command

from subsystems.flywheel import Flywheel

class FlywheelStartMotor(Command):

    def __init__(self, flywheel: Flywheel):
        super().__init__()

        self.flywheel = flywheel
        self.addRequirements(flywheel)

    def initialize(self) -> None:
        self.flywheel.startMotors()

    def isFinished(self) -> bool:
        pass