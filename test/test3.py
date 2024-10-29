import math
import numpy as np
from typing import List

class HolonomicRobot:
    def __init__(self, robot_radius):
        self.robot_radius = robot_radius
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def get_wheel_velocities(self, vx: float, vy: float, w: float, phi: float) -> List[float]:
        """Calculate the wheel velocities based on the robot's velocity and angular velocity."""
        t = np.array([
            [-math.sin(phi + math.pi/4), math.cos(phi + math.pi/4), self.robot_radius],
            [-math.sin(phi + 3 * math.pi/4), math.cos(phi + 3 * math.pi/4), self.robot_radius],
            [-math.sin(phi + 5 * math.pi/4), math.cos(phi + 5 * math.pi/4), self.robot_radius],
            [-math.sin(phi + 7 * math.pi/4), math.cos(phi + 7 * math.pi/4), self.robot_radius]
        ])
        v = np.array([vx, vy, w])
        w = np.dot(t, v)
        w1, w2, w3, w4 = w[0], w[1], w[2], w[3]
        return [w1, w2, w3, w4]

    def get_robot_velocity(self, wheel_velocities: List[float], phi: float) -> List[float]:
        """Calculate the robot's velocity and angular velocity based on the wheel velocities."""
        w1, w2, w3, w4 = wheel_velocities
        D =  np.array([
            [-math.sin(phi + math.pi/4), math.cos(phi + math.pi/4), 2/self.robot_radius],
            [-math.sin(phi + 3 * math.pi/4), math.cos(phi + 3 * math.pi/4), 2/self.robot_radius],
            [-math.sin(phi + 5 * math.pi/4), math.cos(phi + 5 * math.pi/4), 2/self.robot_radius],
            [-math.sin(phi + 7 * math.pi/4), math.cos(phi + 7 * math.pi/4), 2/self.robot_radius]
        ])

        D = 1/2 * np.transpose(D)

        w = np.array([w1, w2, w3, w4])
        v = np.dot(D, w)
        vx, vy, w = v[0], v[1], v[2]
        return [vx, vy, w]

    def update_odometry(self, current_position, wheel_velocities, dt=1.0):
        """Update the robot's position based on the wheel velocities."""
        x, y, theta = current_position
        vx, vy, w = self.get_robot_velocity(wheel_velocities, theta)

        # Update position based on velocities and time step
        x += vx * dt
        y += vy * dt
        theta += w * dt

        # Normalize theta to keep it within -pi to pi
        theta = (theta + math.pi) % (2 * math.pi) - math.pi

        self.x = x
        self.y = y
        self.theta = theta

        return self.x, self.y, self.theta

    def display_position(self):
        print(f"Position: x={self.x:.2f} m, y={self.y:.2f} m, theta={self.theta:.2f} radians")

# Example usage
robot_radius = 0.5  # Example radius in meters
holonomic_robot = HolonomicRobot(robot_radius)

# Example current position
current_position = (0.0, 0.0, 0.0)  # Starting position

# Example velocities
vx = 1.0  # Example x velocity
vy = 1.0  # Example y velocity
w = 0.1   # Example angular velocity (radians per second)
phi = math.radians(45) # Example robot heading

# Calculate wheel velocities
wheel_velocities = holonomic_robot.get_wheel_velocities(vx, vy, w, phi)

# Update odometry
new_position = holonomic_robot.update_odometry(current_position, wheel_velocities, dt=1.0)
holonomic_robot.display_position()
