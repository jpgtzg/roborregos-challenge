from lib.math.odometry import Odometry
from lib.math.pose2d import Pose2d
from lib.math.rotation2d import Rotation2d
from lib.math.wheel_positions import WheelPositions
from lib.math.robot_kinematics import Kinematics
from lib.math.robot_kinematics import RobotConfig

config = RobotConfig(robot_radius=0.28, wheel_radius=0.1)

kine = Kinematics(config) 

odo = Odometry(Pose2d(0, 0, Rotation2d(0)), Rotation2d(0), WheelPositions(0, 0, 0, 0), kine)

x = odo.update(Rotation2d(0), WheelPositions(1, 1, 1, 1))
print(x)

