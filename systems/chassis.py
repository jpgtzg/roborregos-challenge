from lib.system import system
from hardware.motor import Motor
from lib.math.robot_kinematics import Kinematics
from math import sqrt

class Chassis(system.System):

    def __init__(self, motor1: Motor, motor2 : Motor, motor3 : Motor, motor4: Motor) -> None:
        super().__init__("Chassis System")

        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
        
        self.kinematics = Kinematics()

        pass

    def start(self):
        pass

    def update(self):     
        pass

    def move(self, vx: float, vy: float, omega: float):

        v = sqrt(vx**2 + vy**2)

        vel_target = self.kinematics.move_motors(v, omega)

        for vel, motor in zip(vel_target, [self.motor1, self.motor2, self.motor3, self.motor4]):
            motor.move_motor(vel)