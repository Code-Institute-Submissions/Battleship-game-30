# function to create an empty grid
def create_grid(size):
    # take a grid size for n*n and append O in-place
    grid = []
    for _ in range(size):
        row = ["O"] * size
        grid.append(row)
    return grid

# function to display the grid
def display_grid(grid):
    for row in grid:
        # with spaced row and column display grid
        print(" ".join(row))
