from maze.cell import Cell
from maze.maze import Maze

width, height = 5, 3
maze = Maze(width, height)

# Remove some walls to create paths
maze.add_wall_between(1, 0, 1, 1)
maze.add_wall_between(1, 1, 2, 1)
maze.add_wall_between(2, 0, 2, 2)
maze.add_wall_between(4, 1, 4, 0)

maze.set_color(1, 0, "black")

maze.display()

movements = []

# Psuedo code for DFS
def dfs(x, y):
    maze.set_visited(x, y, True)

    for neighbor in maze.get_neighbors(x, y):
        if neighbor.visited:
            continue

        pos = maze.get_cell(x, y).get_relative_position(neighbor)

        if pos == "left":
            if (checkLeftWall()):
                maze.add_wall_between(x, y, x, y-1)
                continue
            moveLeft()
            movements.append("Left")
            print("Left")

        elif pos == "backward":
            if(checkBackwardWall()):
                maze.add_wall_between(x, y, x + 1, y)
                continue
            moveBackward()
            movements.append("Backward")
            print("Backward")

        elif pos == "right":
            if(checkRightWall()):
                maze.add_wall_between(x, y, x, y+1)
                continue
            moveRight()
            movements.append("Right")
            print("Right")

        elif pos == "forward":
            if(checkForwardWall()):
                maze.add_wall_between(x, y, x - 1, y)
                continue

            moveForward() # add special casa for detexting the end of the maze
            movements.append("Forward")
            print("Forward")

        dfs(neighbor.x, neighbor.y)

    # Backtrack when all neighbors are visited or blocked
    if movements:
        last_move = movements.pop()
        inverseMove(last_move)  # Assume inverseMove reverses the last move
        print(f"Backtracking: {last_move}")
    else: 
        print("Maze traversal complete")
        return

#dfs(4, 1)
#print(visited)

cell = maze.get_cell(3, 1)
neighbors = maze.get_neighbors(3, 1)

for neighbor in neighbors:
    print(f"Cell: {cell.x}, {cell.y} | Neighbor: {neighbor.x}, {neighbor.y}")
    print(cell.get_relative_position(neighbor))

maze.display()
# Display the maze structure after DFS