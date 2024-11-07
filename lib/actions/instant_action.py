# Written by Juan Pablo Gutiérrez
# Action that starts and ends immediately

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
        #Check if function has a return value
        if self.function.__code__.co_argcount > 0:
            return self.function()
        else:
            pass

    def is_finished(self) -> bool:
        return True
    
