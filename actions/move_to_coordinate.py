from lib.actions.action import Action
from systems.chassis import Chassis

class MoveToCoordinate(Action):
    def __init__(self, desired_x, desired_y, chassis : Chassis):
        self.x = desired_x
        self.y = desired_y
        self.chassis = chassis
        super().__init__("MoveToCoordinate")

    def execute(self):
        current_x, current_y = self.chassis.get_position()
        if current_x < self.x:
            self.chassis.move_offset(1, 0)
        elif current_x > self.x:
            self.chassis.move_offset(-1, 0)
        elif current_y < self.y:
            self.chassis.move_offset(0, 1)
        elif current_y > self.y:
            self.chassis.move_offset(0, -1)

    def is_finished(self):
        current_x, current_y = self.chassis.get_position()
        return current_x == self.x and current_y == self.y
    
    def end(self, interrupted: bool):
        self.chassis.stop()