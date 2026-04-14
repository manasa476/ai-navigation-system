import matplotlib.pyplot as plt
from src.grid import create_grid
from src.astar import astar

def run_simulation():
    size = 10
    grid = create_grid(size)

    start = (0, 0)
    goal = (9, 9)

    path = astar(grid, start, goal)

    plt.imshow(grid, cmap='gray')

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, color='blue', linewidth=2)

    plt.scatter(start[1], start[0], color='green', s=100)
    plt.scatter(goal[1], goal[0], color='red', s=100)

    plt.title("Autonomous Navigation System")
    plt.show()