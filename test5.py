import math
import numpy as np
from typing import List

class HolonomicRobot:
    def __init__(self, robot_radius):
        self.robot_radius = robot_radius

    def get_wheel_velocities(self, vx: float, vy: float, w: float, phi: float) -> List[float]:
        """Calculate the wheel velocities based on the robot's current velocity and angular velocity."""
        t = np.array([
            [-math.sin(phi + math.pi/4), math.cos(phi + math.pi/4), self.robot_radius],
            [-math.sin(phi + 3 * math.pi/4), math.cos(phi + 3 * math.pi/4), self.robot_radius],
            [-math.sin(phi + 5 * math.pi/4), math.cos(phi + 5 * math.pi/4), self.robot_radius],
            [-math.sin(phi + 7 * math.pi/4), math.cos(phi + 7 * math.pi/4), self.robot_radius]
        ])

        # Debug print statements to check matrix values and transformations
        for i, (sin_val, cos_val) in enumerate(t[:, :2]):
            print(f"Wheel {i + 1} -> sin(phi + {i * 90 + 45}°): {sin_val}, cos(phi + {i * 90 + 45}°): {cos_val}")
        
        v = np.array([vx, vy, w])
        w = np.dot(t, v)
        w1, w2, w3, w4 = w[0], w[1], w[2], w[3]

        # Debug print to check wheel velocities
        print(f"Wheel velocities: {w1}, {w2}, {w3}, {w4}")

        return [w1, w2, w3, w4]

# Example usage
robot_radius = 0.5  # Example radius in meters
holonomic_robot = HolonomicRobot(robot_radius)

# Example velocities and angle
vx = 70.71067812  # Example x velocity
vy = 70.71067812  # Example y velocity
w = 0.1   # Example angular velocity

# Test for different angles
for phi in [0, math.pi/4, math.pi/2, math.pi, 3*math.pi/2]:
    print(f"\nTesting for phi: {phi} radians ({math.degrees(phi)} degrees)")
    wheel_velocities = holonomic_robot.get_wheel_velocities(vx, vy, w, phi)
    print(f"Calculated wheel velocities: {wheel_velocities}")
