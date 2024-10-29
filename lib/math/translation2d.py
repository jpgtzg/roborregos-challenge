import math
from dataclasses import dataclass
from typing import List
import json
from .rotation2d import Rotation2d

@dataclass
class Translation2d:
    x: float
    y: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @classmethod
    def from_distance_and_angle(cls, distance: float, angle: Rotation2d):
        x = distance * angle.get_cos()
        y = distance * angle.get_sin()
        return cls(x, y)

    def get_distance(self, other: 'Translation2d') -> float:
        return math.hypot(other.x - self.x, other.y - self.y)

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def to_vector(self):
        return [self.x, self.y]

    def get_norm(self) -> float:
        return math.hypot(self.x, self.y)

    def get_angle(self) -> Rotation2d:
        return Rotation2d(self.x, self.y)

    def rotate_by(self, other: Rotation2d) -> 'Translation2d':
        return Translation2d(
            self.x * other.get_cos() - self.y * other.get_sin(),
            self.x * other.get_sin() + self.y * other.get_cos()
        )

    def plus(self, other: 'Translation2d') -> 'Translation2d':
        return Translation2d(self.x + other.x, self.y + other.y)

    def minus(self, other: 'Translation2d') -> 'Translation2d':
        return Translation2d(self.x - other.x, self.y - other.y)

    def unary_minus(self) -> 'Translation2d':
        return Translation2d(-self.x, -self.y)

    def times(self, scalar: float) -> 'Translation2d':
        return Translation2d(self.x * scalar, self.y * scalar)

    def div(self, scalar: float) -> 'Translation2d':
        return Translation2d(self.x / scalar, self.y / scalar)

    def nearest(self, translations: List['Translation2d']) -> 'Translation2d':
        return min(translations, key=self.get_distance)

    def __str__(self) -> str:
        return f"Translation2d(X: {self.x:.2f}, Y: {self.y:.2f})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Translation2d):
            return math.isclose(other.x, self.x, abs_tol=1E-9) and \
                   math.isclose(other.y, self.y, abs_tol=1E-9)
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def interpolate(self, end_value: 'Translation2d', t: float) -> 'Translation2d':
        x = self.x + (end_value.x - self.x) * t
        y = self.y + (end_value.y - self.y) * t
        return Translation2d(x, y)

    def to_json(self):
        return json.dumps({'x': self.x, 'y': self.y})

    @staticmethod
    def from_json(json_str: str) -> 'Translation2d':
        data = json.loads(json_str)
        return Translation2d(data['x'], data['y'])


# Example usage
if __name__ == "__main__":
    t1 = Translation2d(3.0, 4.0)
    t2 = Translation2d(1.0, 2.0)
    print(t1.get_distance(t2))
    print(t1.plus(t2))
