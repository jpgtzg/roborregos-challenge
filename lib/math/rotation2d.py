import math
from dataclasses import dataclass

@dataclass
class Rotation2d:
    """A rotation in a 2D coordinate frame represented by a point on the unit circle (cosine and sine).
    
    The angle is continuous, meaning an angle of 361 degrees will return 361 degrees.
    This avoids discontinuities in rotations across 360 degrees.
    """
    m_value: float = 0.0  # Angle in radians
    m_cos: float = math.cos(0.0)
    m_sin: float = math.sin(0.0)

    def __init__(self, value=None, x=None, y=None):
        if value is not None:
            self.m_value = value
            self.m_cos = math.cos(value)
            self.m_sin = math.sin(value)
        elif x is not None and y is not None:
            magnitude = math.hypot(x, y)
            if magnitude > 1e-6:
                self.m_sin = y / magnitude
                self.m_cos = x / magnitude
            else:
                self.m_sin = 0.0
                self.m_cos = 1.0
            self.m_value = math.atan2(self.m_sin, self.m_cos)

    @staticmethod
    def from_radians(radians):
        return Rotation2d(value=radians)

    @staticmethod
    def from_degrees(degrees):
        return Rotation2d(value=math.radians(degrees))

    @staticmethod
    def from_rotations(rotations):
        return Rotation2d(value=rotations * 2 * math.pi)

    def plus(self, other):
        return self.rotate_by(other)

    def minus(self, other):
        return self.rotate_by(other.unary_minus())

    def unary_minus(self):
        return Rotation2d(value=-self.m_value)

    def times(self, scalar):
        return Rotation2d(value=self.m_value * scalar)

    def div(self, scalar):
        return self.times(1.0 / scalar)

    def rotate_by(self, other):
        return Rotation2d(
            x=self.m_cos * other.m_cos - self.m_sin * other.m_sin,
            y=self.m_cos * other.m_sin + self.m_sin * other.m_cos
        )

    def get_radians(self):
        return self.m_value

    def get_degrees(self):
        return math.degrees(self.m_value)

    def get_rotations(self):
        return self.m_value / (2 * math.pi)

    def get_cos(self):
        return self.m_cos

    def get_sin(self):
        return self.m_sin

    def get_tan(self):
        return self.m_sin / self.m_cos

    def __str__(self):
        return f"Rotation2d(Rads: {self.m_value:.2f}, Deg: {math.degrees(self.m_value):.2f})"

    def __eq__(self, other):
        if isinstance(other, Rotation2d):
            return math.isclose(self.m_cos, other.m_cos, abs_tol=1e-9) and \
                   math.isclose(self.m_sin, other.m_sin, abs_tol=1e-9)
        return False

    def __hash__(self):
        return hash(self.m_value)

    def interpolate(self, end_value, t):
        t = max(0, min(t, 1))  # Clamp t to [0, 1]
        return self.plus(end_value.minus(self).times(t))
