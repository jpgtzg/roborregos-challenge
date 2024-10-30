from lib.actions.action import Action
from hardware.motor import Motor

class Intake(Action):
    def __init__(self, name, description, intake, left_motor_port, right_motor_port):
        super().__init__(name, description)
        self.intake = intake
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)


    def start(self):
        pass

    def update(self):
        pass

    def set(self, speed: float) -> None:
        self.left_motor.simple_move(speed)
        self.right_motor.simple_move(-speed)
        pass