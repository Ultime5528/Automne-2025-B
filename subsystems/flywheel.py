from enum import Enum, auto

import ports
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem

class Flywheel(Subsystem):
    class State(Enum):
        Unknown = auto()
        Moving = auto()
        Loading = auto()

    speed = autoproperty(0.2)

    def __init__(self):
        super().__init__()
        self.flywheel = Flywheel
        self._motor = ports.flywheel_motor

    def stop(self):
        self._motor.stop()

    def move(self, speed:float):
        self._motor.setspeed(speed)