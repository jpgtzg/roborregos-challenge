from lib.system.system import System

class StateMachine:

    def __init__(self, *systems : System) -> None:
        self.systems = [*systems]

    def start(self):
        for system in self.systems:
            system.start()

    def periodic(self):
        for system in self.systems:
            system.update()