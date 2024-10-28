import numpy as np
import math
from typing import List
#from .pose2d import Pose2d

class RobotConfig:
    def __init__(self, robot_radius: float, wheel_radius: float):
        self.robot_radius = robot_radius
        self.wheel_radius = wheel_radius

class RobotVelocity:
    def __init__(self, x: float, y: float, theta: float):
        self.x = x
        self.y = y
        self.theta = theta

class Kinematics:
    """ def __init__(self, config: RobotConfig):
        self.config = config """

    def move_motors(self, degree: int, speed: int) -> List[int]:
        """Calculate wheel speeds based on the robot's heading and speed."""
        m1 = math.cos(math.radians(45 + degree))
        m2 = math.cos(math.radians(135 + degree))
        m3 = math.cos(math.radians(225 + degree))
        m4 = math.cos(math.radians(315 + degree))

        speedA = abs(int(m1 * speed))
        speedB = abs(int(m2 * speed))
        speedC = abs(int(m3 * speed))
        speedD = abs(int(m4 * speed))

        # Simulating motor movements (forward or backward)
        motors_directions = [
            "forward" if m1 >= 0 else "backward",
            "forward" if m2 >= 0 else "backward",
            "forward" if m3 >= 0 else "backward",
            "forward" if m4 >= 0 else "backward",
        ]

        # Print motor speeds and directions (or implement actual motor control)
        motor_speeds = [speedA, speedB, speedC, speedD]
        for i in range(4):
            print(f"Motor {i+1}: Speed = {motor_speeds[i]}, Direction = {motors_directions[i]}")

        return motor_speeds

    def get_robot_velocity(self, wheel_velocities: List[float]) -> RobotVelocity:
        """Calculates robot velocity based on wheel velocities."""
        # Placeholder method: needs to be implemented based on the robot's kinematic model
        pass

"""     def get_wheels_angular_velocities(self, robot_velocity: RobotVelocity, robot_position: Pose2d) -> List[float]:
        x = np.array([
            [-math.sin(robot_position.theta + (math.pi / 4)), math.cos(robot_position.theta + (math.pi / 4)), self.config.robot_radius],
            [-math.sin(robot_position.theta + (3 * math.pi / 4)), math.cos(robot_position.theta + (3 * math.pi / 4)), self.config.robot_radius],
            [-math.sin(robot_position.theta + (5 * math.pi / 4)), math.cos(robot_position.theta + (5 * math.pi / 4)), self.config.robot_radius],
            [-math.sin(robot_position.theta + (7 * math.pi / 4)), math.cos(robot_position.theta + (7 * math.pi / 4)), self.config.robot_radius]
        ])
        
        vel = np.array([robot_velocity.x, robot_velocity.y, robot_velocity.theta])
        
        rad = 1 / self.config.wheel_radius
        
        result = np.dot(np.dot(x, vel), rad) 
        return result.tolist()
 """