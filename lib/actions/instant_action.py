from lib.actions.action import Action

class InstantAction(Action):
    def __init__(self, name, function):
        super().__init__(name)
        self.function = function

    def initialize(self):
        self.function()

    def is_finished(self) -> bool:
        return True
    