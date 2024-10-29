import math

class Twist2d:
    """A change in distance along a 2D arc since the last pose update."""
    
    def __init__(self, dx=0.0, dy=0.0, dtheta=0.0):
        """
        Constructs a Twist2d with the given values.
        
        :param dx: Change in x direction relative to robot.
        :param dy: Change in y direction relative to robot.
        :param dtheta: Change in angle relative to robot (in radians).
        """
        self.dx = dx
        self.dy = dy
        self.dtheta = dtheta

    def __str__(self):
        return f"Twist2d(dX: {self.dx:.2f}, dY: {self.dy:.2f}, dTheta: {self.dtheta:.2f})"

    def __eq__(self, other):
        if isinstance(other, Twist2d):
            return (math.isclose(self.dx, other.dx, abs_tol=1E-9) and
                    math.isclose(self.dy, other.dy, abs_tol=1E-9) and
                    math.isclose(self.dtheta, other.dtheta, abs_tol=1E-9))
        return False

    def __hash__(self):
        return hash((self.dx, self.dy, self.dtheta))
