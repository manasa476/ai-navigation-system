import numpy as np

def create_grid(size):
    grid = np.zeros((size, size))

    obstacles = [(3,3),(3,4),(3,5),(6,7),(7,7),(8,7)]

    for obs in obstacles:
        grid[obs] = 1

    return grid