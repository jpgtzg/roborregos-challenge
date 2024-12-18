# Written by Juan Pablo Gutiérrez
# Waits for a specified duration

from lib.actions.action import Action
import time

class WaitAction(Action):
    def __init__(self, duration):
        super().__init__("WaitCommand")
        self.duration = duration
        self.start_time = 0

    def initialize(self):
        self.start_time = time.time()

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def is_finished(self) -> bool:
        return time.time() - self.start_time >= self.duration
    

