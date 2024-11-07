from actions.maze_action import MazeAction
from lib.actions.instant_action import InstantAction
from actions.move_to_coordinate import MoveToCoordinate
from systems.chassis import Chassis
from systems.ultrasonics import Ultrasonics
from maze.maze import Maze
from lib.actions.action_scheduler import ActionScheduler
from systems.display import Display
from actions.balance_action import BalanceAction
from systems.intake import Intake
import time

# TODO: FINISH TESTING
def init_maze(chassis_system: Chassis, ultrasonics: Ultrasonics, display : Display, intake: Intake):

    # TODO: Move over to action system

    chassis_system.move(10, 0, 0, 0)

    if not ultrasonics.check_forward():
        intake.set(100)
        chassis_system.move(10, 0, 0, 0)
        time.sleep(10)
        intake.set(0)
        chassis_system.move(-10, 0, 0, 0)

    if not ultrasonics.check_right():
        chassis_system.move(0, 10, 0, 0)
        intake.set(100)
        chassis_system.move(10, 0, 0, 0)
        time.sleep(10)
        intake.set(0)
        chassis_system.move(-10, 0, 0, 0)

    if not ultrasonics.check_left():
        chassis_system.move(0, -10, 0, 0)
        intake.set(100)
        chassis_system.move(10, 0, 0, 0)
        time.sleep(10)
        intake.set(0)
        chassis_system.move(-10, 0, 0, 0)

    if not ultrasonics.check_back():
        chassis_system.move(0, 20, 0, 0)
        intake.set(100)
        chassis_system.move(10, 0, 0, 0)
        time.sleep(10)
        intake.set(0)
        chassis_system.move(-10, 0, 0, 0)

    move_to_coordinate = MoveToCoordinate(-1, 1, chassis_system)

    ActionScheduler().schedule_action(move_to_coordinate)