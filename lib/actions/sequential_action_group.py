from lib.actions.action import Action

class SequentialActionGroup(Action):
    def __init__(self, *actions):
        super().__init__("SequentialGroup")
        self.actions = actions
        self.current_action_index = 0

    def initialize(self):
        if self.actions:  
            self.actions[0].initialize()

    def execute(self):
        if self.current_action_index >= len(self.actions): 
            return
        
        current_action = self.actions[self.current_action_index]
        current_action.execute()
        if current_action.is_finished():
            current_action.end(False)
            self.current_action_index += 1
            if self.current_action_index < len(self.actions):
                self.actions[self.current_action_index].initialize()

    def is_finished(self) -> bool:
        return self.current_action_index >= len(self.actions)
