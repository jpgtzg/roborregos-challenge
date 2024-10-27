from lib.actions.action import Action

class RunAction(Action):

    def __init__(self, name: str, function):
        super().__init__(name)
        self.function = function

    def initialize(self):
        pass

    def execute(self):
        self.function()

    def end(self, interrupted: bool):
        pass

    def is_finished(self) -> bool:
        return False