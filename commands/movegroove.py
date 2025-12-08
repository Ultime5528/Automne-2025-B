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

    def initialize(self):
        self.pulley.maintain()

    def execute(self):
        if self.xbox_remote.povUp().getAsBoolean():
            self.pulley.pulleyUp()
        elif self.xbox_remote.povDown().getAsBoolean():
            self.pulley.pulleyDown()
        else:
            self.pulley.maintain()

    def isFinished(self) -> bool:
        return False