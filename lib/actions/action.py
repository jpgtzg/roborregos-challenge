from ...lib.system.system import System

class Action:

    def __init__(self, name):
        self.name = name
        self.requirements = set()

    def start(self):
        pass
    
    def execute(self ):
        pass
    
    def is_finished(self ) -> bool:
        pass

    def finalize(self, interrupted : bool): 
        pass

    def add_requirements(self, requirement: System):
        self.requirements.add(requirement)