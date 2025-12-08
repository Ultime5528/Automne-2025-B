import wpilib
from commands2 import Command

from subsystems.ballpusher import BallPusher
from ultime.autoproperty import autoproperty, FloatProperty, asCallable


class PushBall(Command):

    @classmethod
    def red(cls, ballpusher: BallPusher):
        cmd = cls(
            ballpusher,
            lambda: push_ball_properties.delay_red,
            lambda: push_ball_properties.speed_red
        )
        cmd.setName(cmd.getName() + ".red")
        return cmd

    @classmethod
    def yellow(cls, ballpusher: BallPusher):
        cmd = cls(
            ballpusher,
            lambda: push_ball_properties.delay_yellow,
            lambda: push_ball_properties.speed_yellow
        )
        cmd.setName(cmd.getName() + ".yellow")
        return cmd

    def __init__(self, ballpusher: BallPusher, delay : FloatProperty, speed : FloatProperty) -> None:
        super().__init__()
        self.delay_getter = asCallable(delay)
        self.speed_getter = asCallable(speed)
        self.ballpusher = ballpusher
        self.addRequirements(ballpusher)
        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.reset()
        self.timer.start()

    def execute(self) -> None:
        self.ballpusher.push(self.speed_getter())

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.delay_getter())

    def end(self, interrupted: bool):
        self.timer.stop()
        self.ballpusher.stop()

class _ClassProperties:
    delay_red = autoproperty(3, subtable=PushBall.__name__)
    speed_red = autoproperty(0.15, subtable=PushBall.__name__)
    delay_yellow = autoproperty(3, subtable=PushBall.__name__)
    speed_yellow = autoproperty(0.15, subtable=PushBall.__name__)

push_ball_properties = _ClassProperties()