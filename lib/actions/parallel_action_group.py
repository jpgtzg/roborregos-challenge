from lib.actions.action import Action

class ParallelActionGroup(Action):
    def __init__(self, *actions):
        super().__init__("ParallelGroup")
        self.actions = actions

    def initialize(self):
        for action in self.actions:
            action.initialize()

    def execute(self):
        for action in self.actions:
            action.execute()

    def is_finished(self) -> bool:
        return all(action.is_finished() for action in self.actions)
