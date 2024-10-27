from lib.actions.action import Action
import time

class WaitAction(Action):
    def __init__(self, duration):
        super().__init__("WaitCommand")
        self.duration = duration
        self.start_time = 0

    def initialize(self):
        self.start_time = time.time()

    def is_finished(self) -> bool:
        return time.time() - self.start_time >= self.duration
    