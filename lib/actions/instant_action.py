from lib.actions.action import Action

class InstantAction(Action):
    def __init__(self, function):
        super().__init__("Instant Command")
        self.function = function

    def initialize(self):
        self.function()

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def is_finished(self) -> bool:
        return True
    