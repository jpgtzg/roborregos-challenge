from lib.math.twist2d import Twist2d
from lib.math.wheel_positions import WheelPositions
import numpy as np
import math
from typing import List
#from .pose2d import Pose2d

class RobotConfig:
    def __init__(self, robot_radius: float, wheel_radius: float):
        self.robot_radius = robot_radius
        self.wheel_radius = wheel_radius

class Kinematics:
    def __init__(self, config: RobotConfig):
        self.config = config

    def get_wheel_velocities(self, vx: float, vy: float, w: float, phi: float) -> List[float]:
        """Calculate the wheel velocities based on the robot's current velocity and angular velocity."""
        t = np.array([
            [-math.sin(phi + math.pi/4), math.cos(phi + math.pi/4), self.config.robot_radius],
            [-math.sin(phi + 3 * math.pi/4), math.cos(phi + 3 * math.pi/4), self.config.robot_radius],
            [-math.sin(phi + 5 * math.pi/4), math.cos(phi + 5 * math.pi/4), self.config.robot_radius],
            [-math.sin(phi + 7 * math.pi/4), math.cos(phi + 7 * math.pi/4), self.config.robot_radius]
        ])

        # Debug print statements to check matrix values and transformations
        
        v = np.array([vx, vy, w])
        w = np.dot(t, v)
        w1, w2, w3, w4 = w[0], w[1], w[2], w[3]

        # Debug print to check wheel velocities
        print(f"Wheel velocities: {w1}, {w2}, {w3}, {w4}")

        return [w1, w2, w3, w4]

    
    def get_robot_velocity(self, wheel_velocities: List[float], phi: float) -> List[float]:
        """
        Calculate the robot's velocity and angular velocity based on the wheel velocities.

        :param wheel_velocities: The wheel velocities.
        :param phi: The robot's heading.
        :return: The robot's velocity and angular velocity.
        """

        w1, w2, w3, w4 = wheel_velocities

        D = 1/2 * np.array([-math.sin(phi + math.pi/4), math.cos(phi + math.pi/4), 2/self.config.robot_radius],
                           [-math.sin(phi + 3 * math.pi/4), math.cos(phi + 3 * math.pi/4), 2/self.config.robot_radius],
                           [-math.sin(phi + 5 * math.pi/4), math.cos(phi + 5 * math.pi/4), 2/self.config.robot_radius],
                           [-math.sin(phi + 7 * math.pi/4), math.cos(phi + 7 * math.pi/4), 2/self.config.robot_radius])

        D = 1/2 * np.transpose(D)

        w = np.array([w1, w2, w3, w4])
        v = np.dot(D, w)
        vx, vy, w = v[0], v[1], v[2]
        return [vx, vy, w]