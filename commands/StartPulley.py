
from subsystems.pulley import Pulley
from idlelib.undo import Command

class PulleyStartMotor(Command):

    def __init__(self, pulley: Pulley):
        super().__init__()

        self.pulley = pulley
        self.addRequirements(pulley)

    def initialize(self) -> None:
        self.pulley.startMotors()

    def isFinished(self) -> bool:
