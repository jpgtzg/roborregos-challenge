from lib.actions.action_interface import ActionInterface
from lib.system.system import System

class Action(ActionInterface):
    
    def __init__(self, name):
        super().__init__(name)
        self.requirements = set()

    def add_requirements(self, requirement: System):
        self.requirements.add(requirement)

    def get_requirements(self):
        return self.requirements
        
    def schedule(self):
        from lib.actions.action_scheduler import ActionScheduler
        ActionScheduler().schedule_action(self)
    
    # Composition methods
    def andThen(self, next_action) -> ActionInterface:
        from lib.actions.sequential_action_group import SequentialActionGroup
        return SequentialActionGroup(self, next_action)

    def withTimeout(self, timeout) -> ActionInterface:
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        from lib.actions.wait_action import WaitAction
        return ParallelDeadlineGroup(self, deadline_action=WaitAction(timeout))

    def alongWith(self, *actions) -> ActionInterface:
        from lib.actions.parallel_action_group import ParallelActionGroup
        return ParallelActionGroup(self, *actions)

    def beforeStarting(self, *actions) -> ActionInterface:
        from lib.actions.sequential_action_group import SequentialActionGroup
        return SequentialActionGroup(*actions, self)

    def until(self, condition) -> ActionInterface: 
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        from lib.actions.wait_until_action import WaitUntilAction
        return ParallelDeadlineGroup(self, WaitUntilAction(condition))
    
    def deadlineWith(self, *deadline_action) -> ActionInterface:
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        return ParallelDeadlineGroup(*deadline_action, deadline_action=self)
    
 