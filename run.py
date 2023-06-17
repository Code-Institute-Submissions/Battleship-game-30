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

# function to place the battleships randomly on the grid
def place_battleships(grid, num_battleships):
    size = len(grid)
    for _ in range(num_battleships):
        # make a random position (row and column) to replace 'O' with 'X' which denotes the battleship
        row = randint(0, size - 1)
        col = randint(0, size - 1)
        if grid[row][col] == "X":
            # in this condition we check if already battleship or not
            continue
        grid[row][col] = "X"

# function to check if a shot is on the grid
def is_valid_shot(grid, row, col):
    size = len(grid)
    return 0 <= row < size and 0 <= col < size

# function to play the game
def play_battleships(size, num_battleships):
    # create a grid of user given size
    grid = create_grid(size)
    # place battleships on grid
    place_battleships(grid, num_battleships)
    # display the grid-battleships on terminal
    display_grid(grid)

    num_ships = num_battleships
    while num_ships > 0:
        print("\n")
        row = int(input("Enter the row (0 to {}): ".format(size - 1)))
        col = int(input("Enter the column (0 to {}): ".format(size - 1)))

        if not is_valid_shot(grid, row, col):
            print("Shot is off-grid!")
            continue

if grid[row][col] == "X":
            # replace battleship 'X' to '!' when you hit it
            print("Hit!")
            grid[row][col] = "!"
            num_ships -= 1
        else:
            print("Missed!")

        display_grid(grid)

    print("\nCongratulations! You destroyed all the battleships.")

# starting of user end interactions
grid_size = int(input("Enter the grid size: "))
num_battleships = int(input("Enter the number of battleships: "))
# calling functionality of battleship game
play_battleships(grid_size, num_battleships)
