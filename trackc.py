from actions.maze_action import MazeAction
from lib.actions.instant_action import InstantAction
from actions.move_to_coordinate import MoveToCoordinate
from systems.chassis import Chassis
from systems.ultrasonics import Ultrasonics
from maze.maze import Maze
from lib.actions.action_scheduler import ActionScheduler
from systems.display import Display
from actions.balance_action import BalanceAction

# FINALLY WORKED :))))
def init_maze_action(maze: Maze, chassis_system: Chassis, ultrasonics: Ultrasonics, display : Display):
    color_map = {}
    color = "white"
    final_x = -1
    final_y = -1

    maze_action = MazeAction(maze, chassis_system, ultrasonics, color_map)

    find_color_action = InstantAction("Find Color", lambda: find_color_occurences(color_map, color=color))

    find_coordinates = InstantAction("Find Coordinates", lambda: maze.find_nearest_color(chassis_system.get_position()[0], chassis_system.get_position()[1], color, final_x, final_y))

    move_to_coordinate = MoveToCoordinate(final_x, final_y, chassis_system)

    display_color = InstantAction("Display Color", lambda: display.display_string(color)) 

    move_to_pre_end = MoveToCoordinate(-1, 0, chassis_system)

    balance_action = BalanceAction(chassis_system, display)

    move_to_post_end = MoveToCoordinate(-3, 0, chassis_system)

    final_action = maze_action.andThen(find_color_action).andThen(find_coordinates).andThen(move_to_coordinate).andThen(display_color).andThen(move_to_pre_end).andThen(balance_action).andThen(move_to_post_end)

    ActionScheduler().schedule_action(final_action)

def find_color_occurences(color_map : map, color : str):
    # Find the color that happens 5 times
    for color in color_map:
        if color_map[color] == 5:
            color = color
            break