import math
from dataclasses import dataclass
from typing import List, TypeVar
from .translation2d import Translation2d
from .rotation2d import Rotation2d
from .transform2d import Transform2d
from .twist2d import Twist2d

# Define TypeVar for interpolation
T = TypeVar('T', bound='Pose2d')

@dataclass
class Pose2d:
    translation: Translation2d
    rotation: Rotation2d

    def __init__(self, x: float = 0.0, y: float = 0.0, rotation: Rotation2d = None):
        if rotation is None:
            rotation = Rotation2d(0.0)
        self.translation = Translation2d(x, y)
        self.rotation = rotation

    def plus(self, other: Transform2d) -> 'Pose2d':
        new_translation = self.translation.plus(other.translation.rotate_by(self.rotation))
        new_rotation = other.rotation.plus(self.rotation)
        return Pose2d(new_translation.x, new_translation.y, new_rotation)

    def minus(self, other: 'Pose2d') -> Transform2d:
        relative_pose = self.relative_to(other)
        return Transform2d(relative_pose.translation, relative_pose.rotation)

    def relative_to(self, other: 'Pose2d') -> 'Pose2d':
        transform = Transform2d(other.translation, other.rotation)  # Assuming a constructor
        return Pose2d(transform.translation.x, transform.translation.y, transform.rotation)

    def get_translation(self) -> Translation2d:
        return self.translation

    def get_x(self) -> float:
        return self.translation.x

    def get_y(self) -> float:
        return self.translation.y

    def get_rotation(self) -> Rotation2d:
        return self.rotation

    def rotate_by(self, rotation: Rotation2d) -> 'Pose2d':
        return Pose2d(self.translation.rotate_by(rotation), self.rotation.rotate_by(rotation))

    def exp(self, twist: Twist2d) -> 'Pose2d':
        dx = twist.dx
        dy = twist.dy
        dtheta = twist.dtheta

        sin_theta = math.sin(dtheta)
        cos_theta = math.cos(dtheta)

        if abs(dtheta) < 1E-9:
            s = 1.0 - 1.0 / 6.0 * dtheta * dtheta
            c = 0.5 * dtheta
        else:
            s = sin_theta / dtheta
            c = (1 - cos_theta) / dtheta

        transform = Transform2d(
            Translation2d(dx * s - dy * c, dx * c + dy * s),
            Rotation2d(math.atan2(sin_theta, cos_theta))
        )

        return self.plus(transform)

    def log(self, end: 'Pose2d') -> Twist2d:
        transform = end.relative_to(self)
        dtheta = transform.rotation.get_radians()
        half_dtheta = dtheta / 2.0

        cos_minus_one = transform.rotation
