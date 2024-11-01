from lib.system import system
from hardware.motor import Motor
from lib.math.robot_kinematics import Kinematics, RobotConfig
from math import sin, cos

class Chassis(system.System):

    def __init__(self, motor1: Motor, motor2 : Motor, motor3 : Motor, motor4: Motor) -> None:
        super().__init__("Chassis System")

        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4

        config = RobotConfig(robot_radius=0.23, wheel_radius=0.051)
        
        self.kinematics = Kinematics(config)

        pass

    def start(self):
        pass

    def update(self):     
        pass

    def move(self, v: float, omega: float, vel_angle : float, robot_theta: float) -> None:
        
        vx = v * cos(vel_angle)
        vy = v * sin(vel_angle)


        wheel_velocities = self.kinematics.get_wheel_velocities(vx, vy, omega, robot_theta)

        #print(wheel_velocities)

        for vel, motor in zip(wheel_velocities, [self.motor1, self.motor2, self.motor3, self.motor4]):
            motor.move_motor(vel)

    def stop(self):
        for motor in [self.motor1, self.motor2, self.motor3, self.motor4]:
            motor.stop()