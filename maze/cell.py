# Written by Juan Pablo Gutiérrez

from dataclasses import dataclass

@dataclass
class Cell:

    x: int
    y: int

    top: bool = False
    right: bool = False
    bottom: bool = False
    left: bool = False

    color: str = "white"
    visited: bool = False

    def add_wall(self, direction: str):
        setattr(self, direction, True)

    def get_relative_position(self, other) -> str:
        """
        Get the relative position of an adjacent cell.
        
        Inversions of the x and y coordinates are intentional to match the orientation of the maze.
        """
        if self.x == other.x:
            if self.y == other.y + 1:
                return "right"
            elif self.y == other.y - 1:
                return "left"
        elif self.y == other.y:
            if self.x == other.x + 1:
                return "forward"
            elif self.x == other.x - 1:
                return "backward"
        return "not adjacent"
