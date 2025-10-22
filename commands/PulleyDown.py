
from subsystems.pulley import Pulley
from idlelib.undo import Command

class MoveGrooveMotor(Command):

    def __init__(self, pulley: Pulley):
        super().__init__()

        self.pulley = pulley
        self.addRequirements(pulley)

    def initialize(self) -> None:
        self.pulley.startMotors()

    def execute(self):
        self.pulley.pulleyDown()


    def isFinished(self) -> bool:
        pass

    def end(self, interrupted: bool) -> None:
        self.pulley.stopPulley()
