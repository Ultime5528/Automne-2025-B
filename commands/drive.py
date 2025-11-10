
import commands2

from subsystems.drivetrain import Drivetrain
from ultime.command import Command


class Drive(Command):

    def __init__(self, drivetrain : Drivetrain,
                 xbox_remote: commands2.button.CommandXboxController) -> None:
        super().__init__()
        self.drivetrain = drivetrain
        self.addRequirements(drivetrain)
        self.xbox_remote = xbox_remote

    def execute(self) -> None:
        if self.xbox_remote.povUp():
            self.drivetrain.goForward()
        elif self.xbox_remote.povDown():
            self.drivetrain.goBackward()
        else:
            self.drivetrain.stop()

    def end(self, interrupted: bool) -> None:
        self.drivetrain.StopMotors()

