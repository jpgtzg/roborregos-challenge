from lib.actions.action import Action

class RunAction(Action):

    def __init__(self, name: str, function):
        super().__init__(name)
        self.function = function

    def execute(self):
        self.function()

    def is_finished(self) -> bool:
        return False