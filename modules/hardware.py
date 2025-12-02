import commands2
from wpilib import PowerDistribution

from commands.drive import Drive
from commands.movegroove import MoveGroove
from subsystems.ballpusher import BallPusher
from subsystems.drivetrain import Drivetrain
from subsystems.flywheel import Flywheel
from subsystems.pulley import Pulley
from ultime.module import Module
from ultime.subsystem import Subsystem


class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.controller = commands2.button.CommandXboxController(0)
        self.panel_1 = commands2.button.CommandJoystick(1)
        self.panel_2 = commands2.button.CommandJoystick(2)

        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.controller))
        self.pulley = Pulley()
        self.pulley.setDefaultCommand(MoveGroove(self.pulley, self.controller))
        self.flywheel = Flywheel()
        self.ballpusher = BallPusher()

        self.pdp = PowerDistribution()

        self.subsystems: list[Subsystem] = [self.drivetrain, self.pulley, self.flywheel, self.ballpusher]
