from commands2 import Command

from subsystems.flywheel import Flywheel
from ultime.autoproperty import autoproperty, asCallable, FloatProperty


class Shoot(Command):
    @classmethod
    def red(cls, flywheel: Flywheel):
        cmd = cls(
            flywheel,
            lambda: shoot_properties.speed_red
        )
        cmd.setName(cmd.getName() + ".red")
        return cmd

    @classmethod
    def yellow(cls, flywheel: Flywheel):
        cmd = cls(
            flywheel,
            lambda: shoot_properties.speed_yellow
        )
        cmd.setName(cmd.getName() + ".yellow")
        return cmd


    def __init__(self, flywheel: Flywheel, speed : FloatProperty) -> None:
        super().__init__()
        self.flywheel = flywheel
        self.speed_getter = asCallable(speed)
        self.addRequirements(flywheel)

    def execute(self) -> None:
        self.flywheel.start(self.speed_getter())

    def end(self, interrupted: bool):
        self.flywheel.stop()

class _ClassProperties:
    speed_red = autoproperty(-1.0, subtable=Shoot.__name__)
    speed_yellow = autoproperty(-0.85, subtable=Shoot.__name__)

shoot_properties = _ClassProperties()