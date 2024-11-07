from lib.system.system import System
from hardware.motor import Motor

class Intake(System):
    def __init__(self, intake, left_motor : Motor, right_motor: Motor):
        super().__init__("Intake System")
        self.intake = intake
        self.left_motor = left_motor
        self.right_motor = right_motor


    def start(self):
        pass

    def update(self):
        pass

    def set(self, speed: float) -> None:
        self.left_motor.simple_move(speed)
        self.right_motor.simple_move(speed)
        pass