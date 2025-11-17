from commands.pushball import PushBall
from commands.shoot import Shoot
from modules.hardware import HardwareModule
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
        hardware.controller.rightTrigger().whileTrue(
            Shoot(hardware.flywheel))
        hardware.controller.rightBumper(PushBall(hardware.ballpusher))