import commands2.button

from subsystems.pulley import Pulley
from idlelib.undo import Command

class MoveGrooveMotor(Command):

    def __init__(self, pulley : Pulley,
            xbox_remote: commands2.button.CommandXboxController) -> None:

        super().__init__()

        self.pulley = pulley
        self.addRequirements(pulley)
        self.xbox_remote = xbox_remote

    def initialize(self) -> None:
        self.pulley.startMotors()

    def execute(self):
        self.pulley.pulleyUp()


    def isFinished(self) -> bool:
        pass


    def end(self, interrupted: bool) -> None:
        self.pulley.stopPulley()