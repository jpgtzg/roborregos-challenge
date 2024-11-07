from lib.actions.action import Action
from systems.chassis import Chassis
from systems.infrareds import Infrareds
from simple_pid import PID

class LineFollower(Action):

    def __init__(self, chassis_system : Chassis, infrared : Infrareds):
        super().__init__("Line Follower")

        self.chassis_system = chassis_system
        self.infrared = infrared

        self.add_requirements(chassis_system)
        self.add_requirements(infrared)

    def init(self):
        self.pid = PID(1.4213, 0.1312, 0.00123, setpoint=0)  

    def execute(self):
        error = self.calculate_error()
        correction = self.pid(error)

        velocity = 10 # Note: NEeded for constant velocity
        omega = correction 

        self.chassis.move(velocity, omega, 0, 0)
        pass

    def is_finished(self) :
        return False

    def end(self, interrupted: bool):
        self.chassis_system.stop()

    def calculate_error(self):
        readings = [
            self.infrareds.infrared.get_distance(),
            self.infrareds.infrared2.get_distance(),
            self.infrareds.infrared3.get_distance(),
            self.infrareds.infrared4.get_distance()
        ]

        # Weights for each sensor reading
        weights = [-1.5, -0.5, 0.5, 1.5] 
        
         # Note to self: This allows for sensors farthest from the line to have the most weight (i.e. the most influence on the correction)
        error = sum(weight * reading for weight, reading in zip(weights, readings))
        
        return error