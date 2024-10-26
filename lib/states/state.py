from ..actions import Action
from ..system.system import System
class State:

    def __init__(self, name : str, start_action : Action, execute_action :Action, exit_action: Action, parent : System):
        self.name = name 
        self.start_action = start_action
        self.execute_action = execute_action
        self.exit_action = exit_action
        self.parent = parent

    def enter_state(self):
        self.start_action.execute()

    def execute_state(self):
        self.execute_action.execute()

    def exit_state(self):
        self.exit_action.execute()

    