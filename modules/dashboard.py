import commands2
import wpilib
from commands2 import CommandScheduler

from modules.hardware import HardwareModule
from ultime.module import Module, ModuleList


class DashboardModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,
        module_list: ModuleList,
    ):
        super().__init__()
        self._hardware = hardware
        self._module_list = module_list
        self.setupCommands(hardware)


    def setupCommands(self, hardware):
        """
        Flywheel
        """
        
        #putCommandOnDashboard("Elevator", ResetElevator(hardware.elevator))

        """
        Pulley
        """
        #putCommandOnDashboard("Printer", ResetPrinterRight(hardware.printer))

        """
        Drivetrain
        """
        #putCommandOnDashboard("Drivetrain", DriveRelative.forwards(hardware.drivetrain))
        #putCommandOnDashboard(
        #    "Drivetrain", DriveRelative.backwards(hardware.drivetrain)
        #)

        #putCommandOnDashboard(
        #    "Group",
        #    DropPrepareLoading.toLeft(
        #        hardware.printer,
        #        hardware.arm,
        #        hardware.elevator,
        #        hardware.drivetrain,
        #        hardware.claw,
        #        hardware.controller,
        #        False,
        #    ),
        #    "DropPrepareLoading.toLeft.NotAlways",
        #)
    def robotInit(self) -> None:
        for subsystem in self._hardware.subsystems:
            wpilib.SmartDashboard.putData(subsystem.getName(), subsystem)

        wpilib.SmartDashboard.putData(
            "CommandScheduler", CommandScheduler.getInstance()
        )
        wpilib.SmartDashboard.putData("PDP", self._hardware.pdp)

        for module in self._module_list.modules:
            if module.redefines_init_sendable:
                """
                If a module keeps a reference to a subsystem or the HardwareModule,
                it should be wrapped in a weakref.proxy(). For example,
                self.hardware = proxy(hardware)
                """
                print("Putting on dashboard:", module.getName())
                wpilib.SmartDashboard.putData(module.getName(), module)


def putCommandOnDashboard(
    sub_table: str, cmd: commands2.Command, name: str = None, suffix: str = " commands"
) -> commands2.Command:
    if not isinstance(sub_table, str):
        raise ValueError(
            f"sub_table should be a str: '{sub_table}' of type '{type(sub_table)}'"
        )

    if suffix:
        sub_table += suffix

    sub_table += "/"

    if name is None:
        name = cmd.getName()
    else:
        cmd.setName(name)

    wpilib.SmartDashboard.putData(sub_table + name, cmd)

    return cmd
