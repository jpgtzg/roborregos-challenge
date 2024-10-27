from ..actions.action_interface import ActionInterface
from ..actions.action_scheduler import ActionScheduler


class State:

    def __init__(self, name : str, start_action : ActionInterface, execute_action :ActionInterface, exit_action: ActionInterface):
        self.name = name 
        self.start_action = start_action
        self.execute_action = execute_action
        self.exit_action = exit_action

    def enter_state(self):
        ActionScheduler.schedule_action(self.start_action)

    def execute_state(self):
        ActionScheduler.schedule_action(self.execute_action)

    def exit_state(self):
        ActionScheduler.schedule_action(self.exit_action)

    