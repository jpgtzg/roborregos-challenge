from lib.actions.action import Action

class ActionScheduler():
    
    def __init__(self):
        self.action = None
        self.scheduledCommands = set()

    def schedule_action(self, action: Action):
        self.action = action
        self.action.initialize()

    def execute_action(self):
        self.action.execute()
        if self.action.is_finished():
            self.action.end(False)
            self.action = None

    def is_finished(self) -> bool:
        return self.action is None
    
    def init_action(self, action):
        self.scheduledCommands.add(action)
        action.initialize()

    def run(self):
        actions_to_remove = []
        
        for action in self.scheduledCommands:
            action.execute()
            if action.is_finished():
                action.end(False)
                actions_to_remove.append(action)
        
        for action in actions_to_remove:
            self.scheduledCommands.remove(action)
