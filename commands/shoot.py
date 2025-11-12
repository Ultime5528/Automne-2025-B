import commands2
from commands2 import Command

from subsystems.flywheel import Flywheel


class Shoot(Command):

    def __init__(self, flywheel: Flywheel) -> None:
        super().__init__()
        self.flywheel = flywheel
        self.addRequirements(flywheel)

    def execute(self) -> None:
        self.flywheel.startMotor()

    def end(self, interrupted: bool):
        self.flywheel.stop()
