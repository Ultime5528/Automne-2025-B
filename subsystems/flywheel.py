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
