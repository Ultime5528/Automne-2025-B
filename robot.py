#!/usr/bin/env python3
import wpilib

from modules.algaevision import AlgaeVisionModule
from modules.armcollision import ArmCollisionModule
from modules.autonomous import AutonomousModule
from modules.blockelevatoruntilcoral import BlockElevatorUntilCoralModule
from modules.control import ControlModule
from modules.coralretraction import CoralRetractionModule
from modules.dashboard import DashboardModule
from modules.diagnostics import DiagnosticsModule
from modules.hardware import HardwareModule
from modules.loadingdetection import LoadingDetectionModule
from modules.logging import LoggingModule
from modules.propertysavechecker import PropertySaveCheckerModule
from modules.tagvision import TagVisionModule
from ultime.modulerobot import ModuleRobot


class Robot(ModuleRobot):
    # robotInit fonctionne mieux avec les tests que __init__
    def __init__(self):
        super().__init__()

        wpilib.LiveWindow.disableAllTelemetry()
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)
        self.enableLiveWindowInTest(False)

        self.hardware = HardwareModule()

        self.tag_vision = TagVisionModule(self.hardware.drivetrain)
        self.algae_vision = AlgaeVisionModule()

        self.control = ControlModule(self.hardware, self.algae_vision)

        self.arm_collision = ArmCollisionModule(self.hardware)
        self.loading_detection = LoadingDetectionModule(self.hardware)
        self.block_elevator_until_coral = BlockElevatorUntilCoralModule(
            self.loading_detection, self.hardware.elevator
        )
        self.coral_retraction = CoralRetractionModule(
            self.hardware.elevator, self.hardware.claw
        )

        self.autonomous = AutonomousModule(self.hardware)

        self.dashboard = DashboardModule(self.hardware, self.modules)
        self.diagnostics = DiagnosticsModule(self.hardware, self.modules)
        self.logging = LoggingModule()
        self.property_save_checker = PropertySaveCheckerModule()
        # self.battery_sim = BatterySimModule(self.hardware)

        self.addModules(
            self.hardware,
            self.tag_vision,
            self.algae_vision,
            self.control,
            self.arm_collision,
            self.loading_detection,
            self.block_elevator_until_coral,
            self.coral_retraction,
            self.autonomous,
            self.dashboard,
            self.diagnostics,
            self.logging,
            self.property_save_checker,
            # self.battery_sim,  # Current becomes so low, robot stops working
        )
