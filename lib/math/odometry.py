# Written by Juan Pablo Gutiérrez

from dataclasses import dataclass
from lib.math.wheel_velocities import WheelVelocities
from lib.math.rotation2d import Rotation2d
from lib.math.pose2d import Pose2d
from lib.math.robot_kinematics import Kinematics
import math
import copy

@dataclass
class Odometry:

    kinematcis: Kinematics
    pose_meters: Pose2d
    gyro_offset: Rotation2d
    previous_angle: Rotation2d
    previous_wheel_positions: WheelVelocities

    def __init__(self, initial_pose : Pose2d, gyro_angle: Rotation2d, wheel_positions: WheelVelocities, kinematics : Kinematics):

        self.kinematcis = kinematics
        self.pose_meters = initial_pose
        self.gyro_offset = initial_pose.get_rotation().minus(gyro_angle)
        self.previous_angle = initial_pose.get_rotation()
        self.previous_wheel_positions = copy.copy(wheel_positions)
        
       
    def update(self, angle: Rotation2d, wheel_velocities: WheelVelocities):
        wheel_velocities = [wheel_velocities.front_right_vel, wheel_velocities.front_left_vel, wheel_velocities.back_left_vel, wheel_velocities.back_right_vel]

        x, y = self.pose_meters.get_x(), self.pose_meters.get_y()
        
        vx, vy, w = self.kinematcis.get_robot_velocity(wheel_velocities, angle)

        x += vx * 0.1
        y += vy * 0.1
        theta += w * 0.1

        # Normalize theta to keep it within -pi to pi
        theta = (theta + math.pi) % (2 * math.pi) - math.pi

        pose = Pose2d(x, y, theta)

        return pose
    
    