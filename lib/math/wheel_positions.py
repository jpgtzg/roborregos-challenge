from dataclasses import dataclass

@dataclass
class WheelPositions:
    """
    Class to store the positions of the wheels of the robot
    """
    
    front_right_pos: float
    front_left_pos: float
    back_right_pos: float
    back_left_pos: float

    def __init__(self, front_right: float, front_left: float, back_right: float, back_left: float) -> None:
        self.front_right_pos = front_right
        self.front_left_pos = front_left
        self.back_right_pos = back_right
        self.back_left_pos = back_left