from lib.actions.action import Action
from maze.maze import Maze
from systems.chassis import Chassis
from systems.ultrasonics import Ultrasonics

class MazeAction(Action):

    """ 
    This class is an action that will traverse a maze using a depth-first search algorithm.
    """    
    def __init__(self, maze: Maze,  chassis: Chassis, ultrasonics: Ultrasonics, color_map : map):
        super().__init__("Maze Action")
        self.maze = maze
        self.chassis = chassis
        self.ultrasonics = ultrasonics
        self.movements = []
        self.finished = False
        self.color_map = color_map

    def initialize(self):
        self.dfs(4, 1)

    def execute(self, agent):
        pass 

    def is_finished(self, agent):
        return self.finished

    def end(self, interrputed: bool):
        return self.color_map 
        
    def dfs(self, x, y):
        self.maze.set_visited(x, y, True)

        for neighbor in self.maze.get_neighbors(x, y):
            if neighbor.visited:
                continue

            pos = self.maze.get_cell(x, y).get_relative_position(neighbor)

            if pos == "left":
                if (self.ultrasonics.check_left()):
                    self.maze.add_wall_between(x, y, x, y-1)
                    continue
                self.chassis.move_offset(-1, 0)
                self.movements.append("Left")
                print("Left")

            elif pos == "backward":
                if(self.ultrasonics.check_back()):
                    self.maze.add_wall_between(x, y, x + 1, y)
                    continue
                self.chassis.move_offset(0, -1)
                self.movements.append("Backward")
                print("Backward")

            elif pos == "right":
                if(self.ultrasonics.check_right()):
                    self.maze.add_wall_between(x, y, x, y+1)
                    continue
                self.chassis.move_offset(1, 0)
                self.movements.append("Right")
                print("Right")

            elif pos == "forward":
                if(self.ultrasonics.check_forward()):
                    self.maze.add_wall_between(x, y, x - 1, y)
                    continue

                self.chassis.move_offset(0, 1) # checks for end of the maze
                self.movements.append("Forward")
                print("Forward")

            self.dfs(neighbor.x, neighbor.y)

        if self.movements:
            last_move = self.movements.pop()
            self.inverseMove(last_move) 
            print(f"Backtracking: {last_move}")
        else: 
            print("Maze traversal complete")
            self.finished = True
            return

    def inverseMove(self, last_move):
        if last_move == "Left":
            self.chassis.move_offset(1, 0)
        elif last_move == "Backward":
            self.chassis.move_offset(0, 1)
        elif last_move == "Right":
            self.chassis.move_offset(-1, 0)
        elif last_move == "Forward":
            self.chassis.move_offset(0, -1)