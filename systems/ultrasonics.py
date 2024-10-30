
from lib.actions.action import Action
from hardware.ultrasonic import Ultrasonic

class Ultrasonics(Action):

    def __init__(self, ultrasonic1_port, ultrasonic2_port, ultrasonic3_port):
        super().__init__("Ultrasonic System")

        self.ultrasonic1 = Ultrasonic(ultrasonic1_port)
        self.ultrasonic2 = Ultrasonic(ultrasonic2_port)
        self.ultrasonic3 = Ultrasonic(ultrasonic3_port)
        
    def start(self):
        pass

    def update(self):
        pass

    def get_distance(self, ultrasonic: int) -> float:
        if ultrasonic == 1:
            return self.ultrasonic1.get_distance()
        elif ultrasonic == 2:
            return self.ultrasonic2.get_distance()
        elif ultrasonic == 3:
            return self.ultrasonic3.get_distance()
        else:
            return -1
        pass

    def get_all_distances(self) -> list:
        return [self.ultrasonic1.get_distance(), self.ultrasonic2.get_distance(), self.ultrasonic3.get_distance()]

    def get_closest_distance(self) -> float:
        return min(self.get_all_distances())

    def get_farthest_distance(self) -> float:
        return max(self.get_all_distances())

    def is_within_range(self, range: float, ultrasonic: int) -> bool:
        return self.get_distance(ultrasonic) < range
        