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
chassis_system = Chassis(
    motor1=Motor(IN1=Constants.ChassisConstants.MOTOR1_IN1, IN2=Constants.ChassisConstants.MOTOR1_IN2, PWM=Constants.ChassisConstants.MOTOR1_PWM, inverted=Constants.ChassisConstants.MOTOR1_INVERTED),
    motor2=Motor(IN1=Constants.ChassisConstants.MOTOR2_IN1, IN2=Constants.ChassisConstants.MOTOR2_IN2, PWM=Constants.ChassisConstants.MOTOR2_PWM, inverted=Constants.ChassisConstants.MOTOR2_INVERTED),
    motor3=Motor(IN1=Constants.ChassisConstants.MOTOR3_IN1, IN2=Constants.ChassisConstants.MOTOR3_IN2, PWM=  Constants.ChassisConstants.MOTOR3_PWM, inverted=Constants.ChassisConstants.MOTOR3_INVERTED),
    motor4=Motor(IN1=Constants.ChassisConstants.MOTOR4_IN1, IN2=Constants.ChassisConstants.MOTOR4_IN2, PWM=Constants.ChassisConstants.MOTOR4_PWM, inverted=Constants.ChassisConstants.MOTOR4_INVERTED)
)


move_action1 = RunAction("MoveAction", lambda: chassis_system.move(v=-100, omega=1, vel_angle=math.radians(270), robot_theta=0))
move_action2 = RunAction("MoveAction", lambda: chassis_system.move(v=-100, omega=1, vel_angle=math.radians(180), robot_theta=0))
move_action3 = RunAction("MoveAction", lambda: chassis_system.move(v=-100, omega=1, vel_angle=math.radians(90), robot_theta=0))
move_action4 = RunAction("MoveAction", lambda: chassis_system.move(v=-100, omega=1, vel_angle=math.radians(0), robot_theta=0))

final_action = InstantAction(lambda: chassis_system.stop())

complete_action= move_action1.withTimeout(5).andThen(move_action2.withTimeout(5)).andThen(move_action3.withTimeout(5)).andThen(move_action4.withTimeout(5)).andThen(final_action)

scheduler.schedule_action(complete_action)
    motor4=Motor(IN1=Constants.ChassisConstants.MOTOR4_IN1, IN2=Constants.ChassisConstants.MOTOR4_IN2, PWM=Constants.ChassisConstants.MOTOR4_PWM, inverted=Constants.ChassisConstants.MOTOR4_INVERTED)
)


#from lib.math.robot_kinematics import Kinematics

move_action = RunAction("MoveAction", lambda: chassis_system.move(100, 0, 0))

printAction = RunAction("Prin Action", lambda: print("HII"))

#scheduler.schedule_action()

import math
while True:
    #chassis_system.move(v=-25, omega=1, vel_angle=math.radians(270), robot_theta=0)
    scheduler.run()

    if complete_action.is_finished():
        break
""" printAction = InstantAction("PrintAction", lambda: print("Hello World!"))
""" while True:
    #scheduler.run() """

waitAction = WaitAction(1) # Finishes after 1 second

printAction = InstantAction("PrintAction", lambda: print("Hello World!")) # Prints Hello World! Once

parallelAction = waitAction.alongWith(printAction) # Waits for 1 second and prints Hello World! at the same time
sequentialAction = waitAction.andThen(printAction) # Waits for 1 second and then prints Hello World!

scheduler.schedule_action(parallelAction)

while True:
    scheduler.run()


