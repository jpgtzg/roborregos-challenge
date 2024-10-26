from ..system.system import System
import time

class Action:
    def __init__(self, name):
        self.name = name
        self.requirements = set()

    def initialize(self):
        pass

    def execute(self):
        pass

    def is_finished(self) -> bool:
        return False

    def end(self, interrupted: bool):
        pass

    def add_requirements(self, requirement: System):
        self.requirements.add(requirement)

    def andThen(self, next_action):
        return SequentialCommandGroup(self, next_action)

    def withTimeout(self, timeout):
        return ParallelDeadlineGroup(self, deadline_action= WaitCommand(timeout))

    def alongWith(self, *actions):
        return ParallelCommandGroup(self, *actions)

    def beforeStarting(self, *actions):
        return SequentialCommandGroup(*actions, self)

    def until(self, condition):
        return ParallelDeadlineGroup(self, WaitUntilCommand(condition))
    

# Composition classes
class SequentialCommandGroup(Action):
    def __init__(self, *actions):
        super().__init__("SequentialGroup")
        self.actions = actions
        self.current_action_index = 0

    def initialize(self):
        self.actions[0].initialize()

    def execute(self):
        current_action = self.actions[self.current_action_index]
        current_action.execute()
        if current_action.is_finished():
            current_action.end(False)
            self.current_action_index += 1
            if self.current_action_index < len(self.actions):
                self.actions[self.current_action_index].initialize()

    def is_finished(self) -> bool:
        return self.current_action_index >= len(self.actions)

class ParallelCommandGroup(Action):
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

class InstantCommand(Action):
    def __init__(self, name, function):
        super().__init__(name)
        self.function = function

    def execute(self):
        self.function()

    def is_finished(self) -> bool:
        return True
    

class WaitCommand(Action):
    def __init__(self, duration):
        super().__init__("WaitCommand")
        self.duration = duration
        self.start_time = 0

    def initialize(self):
        self.start_time = time.time()

    def is_finished(self) -> bool:
        return time.time() - self.start_time >= self.duration
    
class WaitUntilCommand(Action):
    def __init__(self, condition):
        super().__init__("WaitUntilCommand")
        self.condition = condition

    def is_finished(self) -> bool:
        return self.condition()