import wpilib
from commands2 import Command

from subsystems.ballpusher import BallPusher
from ultime.autoproperty import autoproperty


class PushBall(Command):

    delay = autoproperty(1.5)

    def __init__(self, ballpusher: BallPusher) -> None:
        super().__init__()
        self.ballpusher = ballpusher
        self.addRequirements(ballpusher)
        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.reset()
        self.timer.start()

    def execute(self) -> None:
        self.ballpusher.push()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.delay)

    def end(self, interrupted: bool):
        self.timer.stop()
        self.ballpusher.stop()

