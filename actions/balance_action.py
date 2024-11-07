from lib.actions.action import Action
from simple_pid import PID
from systems.chassis import Chassis
from systems.display import Display

class BalanceAction(Action):
        
        def __init__(self, chassis_system : Chassis, display: Display):
            super().__init__("Balance")
            self.add_requirements(chassis_system)
            self.add_requirements(display)
            self.chassis_system = chassis_system
            self.display = display
            self.pid = PID(1, 0.1, 0.05, setpoint=0)
            self.currentAngle = self.chassis_system.get_pitch()
    
        def execute(self):
            self.display.display_string("Balancing")

            self.currentAngle = self.chassis_system.get_pitch()

            output = -self.pid(self.currentAngle)

            self.chassis_system.move(v=output, omega=0, vel_angle=0, robot_theta=0)

            return True
        
        def is_finished(self):
            return abs(self.currentAngle) < 0.5
        
        def end(self, interrupted):
             self.display.display_string("Balancing ended")