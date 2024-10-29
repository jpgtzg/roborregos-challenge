from dataclasses import dataclass

@dataclass
class WheelVelocities:
    """
    Class to store the velocities of the wheels of the robot
    """
    
    front_right_vel: float
    front_left_vel: float
    back_right_vel: float
    back_left_vel: float

    def __init__(self, front_right: float, front_left: float, back_right: float, back_left: float) -> None:
        self.front_right_vel = front_right
        self.front_left_vel = front_left
        self.back_right_vel = back_right
        self.back_left_vel = back_left