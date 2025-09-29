from modules.hardware import HardwareModule
from ultime.axistrigger import AxisTrigger
from ultime.module import Module


class ControlModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,
    ):
        super().__init__()

        """
        Pilot's buttons
        """
        #hardware.controller.rightTrigger().whileTrue(
        #    AlignWithAlgae(hardware.drivetrain, algae_vision, hardware.controller)
        #)