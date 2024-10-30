from dataclasses import dataclass, field

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
                return "left"
            elif self.y == other.y - 1:
                return "right"
        elif self.y == other.y:
            if self.x == other.x + 1:
                return "forward"
            elif self.x == other.x - 1:
                return "backward"
        return "not adjacent"

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
        if y > 0: neighbors.append(self.grid[y - 1][x])
        if x < self.width - 1: neighbors.append(self.grid[y][x + 1])
        if y < self.height - 1: neighbors.append(self.grid[y + 1][x])
        if x > 0: neighbors.append(self.grid[y][x - 1])
        return [cell for cell in neighbors if not cell.visited]
    
    def set_color(self, x: int, y: int, color: str):
        """Set the color of the cell at the given coordinates."""
        self.grid[y][x].color = color

    def set_visited(self, x: int, y: int, visited: bool):
        """Set the visited status of the cell at the given coordinates."""
        self.grid[y][x].visited = visited

    def display(self):
        """Print a simple visual representation of the maze."""
        for row in self.grid:
            for cell in row:
                walls = []
                if cell.top: walls.append("T")
                if cell.right: walls.append("R")
                if cell.bottom: walls.append("B")
                if cell.left: walls.append("L")
                print(f"Cell({','.join(walls)})", end=" ")
            print()

# Example usage
width, height = 5, 3
maze = Maze(width, height)

# Remove some walls to create paths // TODO ADD BASED OFF SENSOR DATA
maze.add_wall_between(1, 0, 1, 1)
""" maze.add_wall_between(1, 1, 2, 1)
maze.add_wall_between(2, 0, 2, 2)
maze.add_wall_between(4, 1, 4, 0)
"""
maze.set_color(1, 0, "black")

# Display the maze structure
maze.display()

# Create DFS Algorithm to traverse the entire maze 

movements = []

cell1 = maze.get_cell(3, 1)
cell2 = maze.get_cell(3, 2)


def dfs(x, y):
    maze.set_visited(x, y, True)
    for neighbor in maze.get_neighbors(x, y):
        if neighbor.visited:
            continue

        pos = maze.get_cell(x, y).get_relative_position(neighbor)

        if pos == "left":
            if (checkLeftWall()) :
                maze.add_wall_between(x, y, x, y-1)

            moveLeft()
            movements.append("Left")
            print("Left")
        elif pos == "backward":
            if(checkBackwardWall()):
                maze.add_wall_between(x, y, x + 1, y)

            moveBackward()
            movements.append("Backward")
            print("Backward")
        elif pos == "right":
            if(checkRightWall()):
                maze.add_wall_between(x, y, x, y+1)

            moveRight()
            movements.append("Right")
            print("Right")
        elif pos == "forward":
            if(checkForwardWall()):
                maze.add_wall_between(x, y, x - 1, y)

            moveForward()
            movements.append("Forward")
            print("Forward")

        dfs(neighbor.x, neighbor.y)

    # Backtrack: undo last movement if necessary
    if movements:
        last_move = movements.pop()
        inverseMove(last_move)  # Assume inverseMove reverses the last move
        print(f"Backtracking: {last_move}")
    else: 
        print("Maze traversal complete")
        return

#dfs(4, 1)
#print(visited)

""" cell = maze.get_cell(4, 1)
neighbors = maze.get_neighbors(4, 1)

for neighbor in neighbors:
    print(cell.get_relative_position(neighbor))

 """
# Display the maze structure after DFS