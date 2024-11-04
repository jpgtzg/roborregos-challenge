# Written by Juan Pablo Gutiérez

from lib.actions.action_interface import ActionInterface
from lib.system.system import System

import logging

logger = logging.getLogger(__name__)
class Action(ActionInterface):
    
    def __init__(self, name):
        super().__init__(name)
        self.requirements = set()

    def add_requirements(self, requirement: System):
        self.requirements.add(requirement)

    def get_requirements(self):
        return self.requirements
        
    # Composition methods
    def andThen(self, next_action) -> 'Action':
        from lib.actions.sequential_action_group import SequentialActionGroup
        return SequentialActionGroup(self, next_action)

    def withTimeout(self, timeout) -> 'Action':
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        from lib.actions.wait_action import WaitAction
        return ParallelDeadlineGroup(WaitAction(timeout), self)

    def alongWith(self, *actions) -> 'Action':
        from lib.actions.parallel_action_group import ParallelActionGroup
        return ParallelActionGroup(self, *actions)

    def beforeStarting(self, *actions) -> 'Action':
        from lib.actions.sequential_action_group import SequentialActionGroup
        return SequentialActionGroup(*actions, self)

    def until(self, condition) -> 'Action': 
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        from lib.actions.wait_until_action import WaitUntilAction
        return ParallelDeadlineGroup(self, WaitUntilAction(condition))
    
    def deadlineWith(self, *deadline_action) -> 'Action':
        from lib.actions.parallel_deadline_group import ParallelDeadlineGroup
        return ParallelDeadlineGroup(*deadline_action, deadline_action=self)
    
 