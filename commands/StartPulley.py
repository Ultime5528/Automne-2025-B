def initialize(self) -> None:
    self.timer.reset()
    self.timer.start()


def execute(self) -> None:
    self.ballPusher.open()


def isFinished(self) -> bool:
    return self.timer.get() >= self.open_time


def end(self, interrupted: bool) -> None:
    self.timer.stop()
    self.ballPusher.close()