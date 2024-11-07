from lib.actions.action import Action
from systems.chassis import Chassis
from systems.ultrasonics import Ultrasonics

class FindEmptyWall(Action):

    def __init__(self, chassis_system: Chassis, ultrasonics: Ultrasonics):
        super().__init__("Find Empty Wall")

        self.chassis_system = chassis_system
        self.ultrasonics = ultrasonics

        self.add_requirements(chassis_system)
        self.add_requirements(ultrasonics)

    def execute(self):
        

        pass