from typing import Literal
from commands2 import SequentialCommandGroup

from commands.pushball import PushBall
from commands.retractballpusher import RetractBallPusher
from subsystems.ballpusher import BallPusher
from ultime.command import ignore_requirements


@ignore_requirements("ballpusher")
class PushBallAndRetract(SequentialCommandGroup):
    @staticmethod
    def red(ballpusher: BallPusher):
        cmd = PushBallAndRetract(ballpusher, "red")
        cmd.setName(PushBallAndRetract.__name__ + ".red")
        return cmd

    @staticmethod
    def yellow(ballpusher: BallPusher):
        cmd = PushBallAndRetract(ballpusher, "yellow")
        cmd.setName(PushBallAndRetract.__name__ + ".yellow")
        return cmd

    def __init__(
        self,
        ballpusher: BallPusher,
        color: Literal["red", "yellow"]
    ):
        super().__init__(
            {
                "red": PushBall.red(ballpusher),
                "yellow": PushBall.yellow(ballpusher),
            }[color]
            ,
            {
                "red": RetractBallPusher.red(ballpusher),
                "yellow": RetractBallPusher.yellow(ballpusher),
            }[color]
        )