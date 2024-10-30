from lib.actions.action import Action
from systems.chassis import Chassis

class MoveToCoordinate(Action):
    def __init__(self, desired_x, desired_y, chassis : Chassis):
        self.x = desired_x
        self.y = desired_y
        self.chassis = chassis

    def execute(self, agent):
        agent.move_to(self.x, self.y)

    def is_finished(self, agent):
        return agent.is_at(self.x, self.y)
    
    def end(self, agent):
        agent.stop()