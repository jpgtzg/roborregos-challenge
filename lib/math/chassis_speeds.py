from .pose2d import Pose2d
from .rotation2d import Rotation2d
from .translation2d import Translation2d

class ChassisSpeeds:
    """Represents the speed of a robot chassis."""

    def __init__(self, vx_meters_per_second=0.0, vy_meters_per_second=0.0, omega_radians_per_second=0.0):
        """Constructs a ChassisSpeeds object with the given velocities."""
        self.vx_meters_per_second = vx_meters_per_second
        self.vy_meters_per_second = vy_meters_per_second
        self.omega_radians_per_second = omega_radians_per_second

    @staticmethod
    def discretize(vx_meters_per_second, vy_meters_per_second, omega_radians_per_second, dt_seconds):
        """Discretizes a continuous-time chassis speed."""
        desired_delta_pose = Pose2d(
            vx_meters_per_second * dt_seconds,
            vy_meters_per_second * dt_seconds,
            Rotation2d(omega_radians_per_second * dt_seconds)
        )
        twist = Pose2d().log(desired_delta_pose)
        return ChassisSpeeds(
            twist.dx / dt_seconds,
            twist.dy / dt_seconds,
            twist.dtheta / dt_seconds
        )

    @staticmethod
    def from_field_relative_speeds(vx_meters_per_second, vy_meters_per_second, omega_radians_per_second, robot_angle):
        """Converts field-relative speeds into robot-relative speeds."""
        rotated = Translation2d(vx_meters_per_second, vy_meters_per_second).rotate_by(robot_angle.unary_minus())
        return ChassisSpeeds(rotated.x, rotated.y, omega_radians_per_second)

    @staticmethod
    def from_robot_relative_speeds(vx_robot, vy_robot, omega_robot, robot_angle):
        """Converts robot-relative speeds into field-relative speeds."""
        rotated = Translation2d(vx_robot, vy_robot).rotate_by(robot_angle)
        return ChassisSpeeds(rotated.x, rotated.y, omega_robot)

