import wpilib
from commands2 import Command

from subsystems.ballpusher import BallPusher
from ultime.autoproperty import autoproperty, FloatProperty, asCallable


class RetractBallPusher(Command):

    @classmethod
    def red(cls, ballpusher: BallPusher):
        cmd = cls(
            ballpusher,
            lambda: retract_ball_pusher_properties.delay_red,
            lambda: retract_ball_pusher_properties.speed_red
        )
        cmd.setName(cmd.getName() + ".red")
        return cmd

    @classmethod
    def yellow(cls, ballpusher: BallPusher):
        cmd = cls(
            ballpusher,
            lambda: retract_ball_pusher_properties.delay_yellow,
            lambda: retract_ball_pusher_properties.speed_yellow
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
        self.ballpusher.retract(self.speed_getter())

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.delay_getter())

    def end(self, interrupted: bool):
        self.timer.stop()
        self.ballpusher.stop()

class _ClassProperties:
    delay_red = autoproperty(1.15, subtable=RetractBallPusher.__name__)
    speed_red = autoproperty(0.15, subtable=RetractBallPusher.__name__)
    delay_yellow = autoproperty(1.3, subtable=RetractBallPusher.__name__)
    speed_yellow = autoproperty(0.15, subtable=RetractBallPusher.__name__)

retract_ball_pusher_properties = _ClassProperties()