from idlelib.undo import Command

import commands2
import wpilib

from subsystems.drivetrain import Drivetrain


class Drive(Command):

    def __init__(self, drivetrain : Drivetrain,
                 xbox_remote: commands2.button.CommandXboxController,) -> None:
        super().__init__()
        self.timer = wpilib.Timer()
        self.drivetrain = Drivetrain
        self.addRequirements(Drivetrain)
        self.xbox_remote = xbox_remote

    def execute(self) -> None:
        pass

    def end(self, interrupted: bool) -> None:
        self.drivetrain.stop()

