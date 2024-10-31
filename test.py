from lib.actions.action_scheduler import ActionScheduler
from lib.actions.wait_action import WaitAction # Works
from lib.actions.instant_action import InstantAction # Works
from lib.actions.sequential_action_group import SequentialActionGroup # Works
from lib.actions.parallel_action_group import ParallelActionGroup # Works
from lib.actions.wait_until_action import WaitUntilAction  # Works
from lib.actions.parallel_deadline_group import ParallelDeadlineGroup # Works
from lib.actions.run_action import RunAction  # Works
from constants import Constants
import logging

from systems.chassis import Chassis
from hardware.motor import Motor

logger = logging.getLogger(__name__)
logging.basicConfig(filename="test.log", level=logging.INFO)
logger.info("Starting test")

scheduler = ActionScheduler()

chassis_system = Chassis(
    motor1=Motor(IN1=Constants.ChassisConstants.MOTOR1_IN1, IN2=Constants.ChassisConstants.MOTOR1_IN2, PWM=Constants.ChassisConstants.MOTOR1_PWM, inverted=Constants.ChassisConstants.MOTOR1_INVERTED),
    motor2=Motor(IN1=Constants.ChassisConstants.MOTOR2_IN1, IN2=Constants.ChassisConstants.MOTOR2_IN2, PWM=Constants.ChassisConstants.MOTOR2_PWM, inverted=Constants.ChassisConstants.MOTOR2_INVERTED),
    motor3=Motor(IN1=Constants.ChassisConstants.MOTOR3_IN1, IN2=Constants.ChassisConstants.MOTOR3_IN2, PWM=Constants.ChassisConstants.MOTOR3_PWM, inverted=Constants.ChassisConstants.MOTOR3_INVERTED),
    motor4=Motor(IN1=Constants.ChassisConstants.MOTOR4_IN1, IN2=Constants.ChassisConstants.MOTOR4_IN2, PWM=Constants.ChassisConstants.MOTOR4_PWM, inverted=Constants.ChassisConstants.MOTOR4_INVERTED)
)

moveAction = RunAction("MoveAction", chassis_system.move)

from lib.math.robot_kinematics import Kinematics

robot_kinematics = Kinematics()

move_action = RunAction("MoveAction", lambda: chassis_system.move(100, 0, 0))

scheduler.schedule_action(move_action)

while True:
    scheduler.run()

""" printAction = InstantAction("PrintAction", lambda: print("Hello World!"))

parallelAction = SequentialActionGroup(waitAction, printAction)

scheduler.schedule_action(parallelAction)

while True:
    scheduler.run() """