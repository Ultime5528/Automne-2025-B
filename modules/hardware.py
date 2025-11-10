import commands2
from wpilib import PowerDistribution

from subsystems.pulley import Pulley
from commands.drive import Drive
from subsystems.drivetrain import Drivetrain
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


        self.pdp = PowerDistribution()

        self.subsystems: list[Subsystem] = [self.drivetrain]
