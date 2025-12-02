from commands2 import SequentialCommandGroup
from commands2.cmd import sequence

from commands.pushball import PushBall
from commands.retractballpusher import RetractBallPusher
from subsystems.ballpusher import BallPusher
from ultime.command import ignore_requirements


@ignore_requirements("ballpusher")
class PushBallAndRetract(SequentialCommandGroup):
    def __init__(self, ballpusher: BallPusher):
        super().__init__(sequence(PushBall(ballpusher),RetractBallPusher(ballpusher)))
