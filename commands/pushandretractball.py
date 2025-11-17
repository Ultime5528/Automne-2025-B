from commands2 import SequentialCommandGroup
from commands2.cmd import sequence

from commands.pushball import PushBall
from commands.retractball import RetractBall
from subsystems.ballpusher import BallPusher
from ultime.command import ignore_requirements


@ignore_requirements("ballpusher")
class PushAndRetractBall(SequentialCommandGroup):
    def __init__(self, ballpusher: BallPusher):
        super().__init__(sequence(PushBall(ballpusher),RetractBall(ballpusher)))
