import commands2
from commands2 import Command

from subsystems.pulley import Pulley

class MoveGroove(Command):

    def __init__(self, pulley: Pulley,
                 xbox_remote: commands2.button.CommandXboxController):
        super().__init__()
        self.pulley = pulley
        self.addRequirements(pulley)
        self.xbox_remote = xbox_remote

    def execute(self):
        if self.xbox_remote.rightTrigger():
            self.pulley.pulleyUp()
        elif self.xbox_remote.leftTrigger():
            self.pulley.pulleyDown()
        else:
            self.pulley.stop()

    def isFinished(self) -> bool:
        return False