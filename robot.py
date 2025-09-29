#!/usr/bin/env python3
import wpilib

from modules.control import ControlModule
from modules.dashboard import DashboardModule
from modules.hardware import HardwareModule
from modules.propertysavechecker import PropertySaveCheckerModule
from ultime.modulerobot import ModuleRobot


class Robot(ModuleRobot):
    # robotInit fonctionne mieux avec les tests que __init__
    def __init__(self):
        super().__init__()

        wpilib.LiveWindow.disableAllTelemetry()
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)
        self.enableLiveWindowInTest(False)

        self.hardware = HardwareModule()

        #self.tag_vision = TagVisionModule(self.hardware.drivetrain)

        self.control = ControlModule(self.hardware)

        self.dashboard = DashboardModule(self.hardware, self.modules)
        self.property_save_checker = PropertySaveCheckerModule()
        # self.battery_sim = BatterySimModule(self.hardware)

        self.addModules(
            self.control,
            self.dashboard,
            self.property_save_checker,
            # self.battery_sim,  # Current becomes so low, robot stops working
        )
