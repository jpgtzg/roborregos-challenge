# Written by Juan Pablo Gutiérrez

from dataclasses import dataclass, field
from maze.cell import Cell

@dataclass
class Maze:
    width: int
    height: int
    grid: list = field(init=False)

    def __post_init__(self):
        self.grid = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    def add_wall_between(self, x1: int, y1: int, x2: int, y2: int):
        """Remove the wall between two adjacent cells."""
        cell1 = self.grid[y1][x1]
        cell2 = self.grid[y2][x2]
        
        # Determine which walls to remove based on the cells' relative positions
        if x1 == x2:
            if y1 < y2:  # cell1 is above cell2
                cell1.add_wall("bottom")
                cell2.add_wall("top")
            else:        # cell1 is below cell2
                cell1.add_wall("top")
                cell2.add_wall("bottom")
        elif y1 == y2:
            if x1 < x2:  # cell1 is to the left of cell2
                cell1.add_wall("right")
                cell2.add_wall("left")
            else:        # cell1 is to the right of cell2
                cell1.add_wall("left")
                cell2.add_wall("right")

    def get_cell(self, x: int, y: int) -> Cell:
        """Return the cell at the given coordinates."""
        return self.grid[y][x]
    
    def get_neighbors(self, x: int, y: int) -> list:
        """Return the unvisited neighbors of the cell at the given coordinates."""
        neighbors = []
        if y < self.height - 1: neighbors.append(self.grid[y + 1][x])
        if x < self.width - 1: neighbors.append(self.grid[y][x + 1])
        if y > 0: neighbors.append(self.grid[y - 1][x])
        if x > 0: neighbors.append(self.grid[y][x - 1])
        return [cell for cell in neighbors if not cell.visited]
    
    def set_color(self, x: int, y: int, color: str):
        """Set the color of the cell at the given coordinates."""
        self.grid[y][x].color = color

    def set_visited(self, x: int, y: int, visited: bool):
        """Set the visited status of the cell at the given coordinates."""
        self.grid[y][x].visited = visited

    def find_nearest_color(self, x: int, y: int, color: str, final_x: int, final_y: int) -> tuple:
        """Find the nearest cell of the given color to the cell at the given coordinates."""
        queue = [(x, y)]
        visited = set()

        while queue:
            x, y = queue.pop(0)
            cell = self.grid[y][x]

            if cell.color == color:
                final_x = x
                final_y = y
                return x, y

            visited.add((x, y))

            for neighbor in self.get_neighbors(x, y):
                nx, ny = neighbor.x, neighbor.y
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
        
        return None  # If no cell of the given color is found

    def display(self):
        """Print a simple visual representation of the maze."""
        for row in self.grid:
            for cell in row:
                pos = f"{cell.x} , {cell.y}"
                """ if cell.top: walls.append("T")
                if cell.right: walls.append("R")
                if cell.bottom: walls.append("B")
                if cell.left: walls.append("L") """
                print(f"Cell({pos})", end=" ")
            print()
