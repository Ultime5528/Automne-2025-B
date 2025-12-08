from commands.pushball import PushBall
from commands.pushballandretract import PushBallAndRetract
from commands.retractballpusher import RetractBallPusher
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
            Shoot.red(hardware.flywheel))
        hardware.controller.leftTrigger().whileTrue(
            Shoot.yellow(hardware.flywheel))
        hardware.controller.x().whileTrue(PushBall.red(hardware.ballpusher))
        hardware.controller.b().whileTrue(RetractBallPusher.red(hardware.ballpusher))
        hardware.controller.rightBumper().onTrue(PushBallAndRetract.red(hardware.ballpusher))
        hardware.controller.leftBumper().onTrue(PushBallAndRetract.yellow(hardware.ballpusher))