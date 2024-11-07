from lib.system import system
from hardware.motor import Motor
from lib.math.robot_kinematics import Kinematics, RobotConfig
from lib.math.odometry import Odometry
from lib.math.pose2d import Pose2d
from lib.math.rotation2d import Rotation2d
from simple_pid import PID
from hardware.navx import NavX
from math import sin, cos, radians

class Chassis(system.System):

    def __init__(self, motor1: Motor, motor2 : Motor, motor3 : Motor, motor4: Motor, gyro: NavX) -> None:
        super().__init__("Chassis System")

        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4

        self.navx = gyro

        config = RobotConfig(robot_radius=0.23, wheel_radius=0.051)
        
        self.kinematics = Kinematics(config)
        self.odometry = Odometry(Pose2d(), self.get_orientation(), self.kinematics)
        self.pid = PID(3.332, 0.0, 0.142, setpoint=0)
        pass

    def start(self):
        pass

    def update(self):     
        pass

    def move(self, v: float, omega: float, vel_angle : float, robot_theta: float) -> None:
        
        vx = v * cos(vel_angle)
        vy = v * sin(vel_angle)


        wheel_velocities = self.kinematics.get_wheel_velocities(vx, vy, omega, robot_theta)

        for vel, motor in zip(wheel_velocities, [self.motor1, self.motor2, self.motor3, self.motor4]):
            motor.move_motor(vel)

    def move_to(self, x: float, y: float, theta: float) -> None:
        error_x = x - self.get_position()[0]
        error_y = y - self.get_position()[1]

        error_theta = theta - self.get_orientation().get_degrees()

        self.pid.setpoint = theta
        correction_theta = self.pid(error_theta)

        self.pid.setpoint = x
        correction_x = self.pid(error_x)

        self.pid.setpoint = y
        correction_y = self.pid(error_y)

        self.move(correction_x, correction_y, correction_theta, self.get_orientation().get_degrees())

    def stop(self):
        for motor in [self.motor1, self.motor2, self.motor3, self.motor4]:
            motor.stop()

    def get_position(self) -> tuple:
        return self.odometry.get_pose().get_translation()[0], self.odometry.get_pose().get_translation()[1]
    
    def get_orientation(self) -> Rotation2d:
        rad = radians(self.navx.get_yaw())

        return Rotation2d.from_radians(rad)
    
    def get_pitch (self):
        return self.navx.get_pitch()

    def move_offset(self, x: float, y: float) -> None:
        current_x, current_y = self.get_position()
        self.move_to(current_x + x, current_y + y, self.get_orientation().get_degrees())