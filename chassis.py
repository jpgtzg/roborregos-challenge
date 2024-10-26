from lib.system import system
from hardware.motor import Motor

class Chassis(system.System):

    def __init__(self, motor1: Motor, motor2 : Motor, motor3 : Motor, motor4: Motor) -> None:
        super().__init__("Chassis System")

        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
        
        pass

    def start(self):
        pass

    def update(self):     
        pass