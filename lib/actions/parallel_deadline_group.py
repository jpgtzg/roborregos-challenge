from lib.actions.action import Action

class ParallelDeadlineGroup(Action):
    def __init__(self, deadline_action, *actions):
        super().__init__("ParallelDeadlineGroup")
        self.deadline_action = deadline_action
        self.actions = actions

    def initialize(self):
        self.deadline_action.initialize()
        for action in self.actions:
            action.initialize()

    def execute(self):
        self.deadline_action.execute()
        for action in self.actions:
            action.execute()

    def is_finished(self) -> bool:
        return self.deadline_action.is_finished()

    def end(self, interrupted: bool):
        self.deadline_action.end(interrupted)
        for action in self.actions:
            action.end(interrupted)