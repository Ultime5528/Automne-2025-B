import commands2
from wpilib import PowerDistribution

from commands.drivetrain.drive import DriveField
from commands.elevator.maintainelevator import MaintainElevator
from subsystems.arm import Arm
from subsystems.claw import Claw
from subsystems.climber import Climber
from subsystems.drivetrain import Drivetrain
from subsystems.elevator import Elevator
from subsystems.intake import Intake
from subsystems.led import LEDController
from subsystems.printer import Printer
from ultime.module import Module
from ultime.subsystem import Subsystem


class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.controller = commands2.button.CommandXboxController(0)
        self.panel_1 = commands2.button.CommandJoystick(1)
        self.panel_2 = commands2.button.CommandJoystick(2)

        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(DriveField(self.drivetrain, self.controller))

        self.elevator = Elevator()
        self.elevator.setDefaultCommand(MaintainElevator(self.elevator))

        self.intake = Intake()

        self.claw = Claw()

        self.arm = Arm()

        self.printer = Printer()

        self.climber = Climber()

        self.led = LEDController(self)

        self.pdp = PowerDistribution()

        self.subsystems: list[Subsystem] = [
            self.drivetrain,
            self.elevator,
            self.intake,
            self.claw,
            self.arm,
            self.printer,
            self.climber,
            self.led,
        ]
