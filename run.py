from random import randint

# Function to create an empty grid
def create_grid(size):
    # take a grid size for n*n and append O in-place
    grid = []
    for _ in range(size):
        row = ["O"] * size
        grid.append(row)
    return grid

# Function to display the grid
def display_grid(grid):
    for row in grid:
        # with spaced row and column display grid
        print(" ".join(row))


def display_grids(player_grid, computer_grid):
    # display both user's grid parallely
    size = len(player_grid)

    print("Player's Grid\t\t\tComputer's Grid")
    for i in range(size):
        row_str = " ".join(player_grid[i])
        row_str += "\t\t\t"
        row_str += " ".join(computer_grid[i])
        print(row_str)

# Function to place the battleships randomly on the grid
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

# Function to check if a shot is on the grid
def is_valid_shot(grid, row, col):
    size = len(grid)
    return 0 <= row < size and 0 <= col < size

# Function for the computer to take a random shot
def computer_shot(grid):
    size = len(grid)
    row = randint(0, size - 1)
    col = randint(0, size - 1)
    return row, col

# Function to play against the computer
def play_against_computer(size, num_battleships):
    # create 2 grids of user and computer for given size
    player_grid = create_grid(size)
    computer_grid = create_grid(size)

    # place battleships on both grids
    place_battleships(player_grid, num_battleships)
    place_battleships(computer_grid, num_battleships)

    # print("Player Grid")
    # display_grid(player_grid)
    # print("Computer Grid")
    # display_grid(computer_grid)
    display_grids(player_grid, computer_grid)

    num_player_ships = num_battleships
    num_computer_ships = num_battleships

    while num_player_ships > 0 and num_computer_ships > 0:
        print("\n")
        player_row = int(input("Enter the row (0 to {}): ".format(size - 1)))
        player_col = int(input("Enter the column (0 to {}): ".format(size - 1)))

        if not is_valid_shot(computer_grid, player_row, player_col):
            print("Shot is off-grid!")
            continue

        if computer_grid[player_row][player_col] == "X":
            # replace battleship 'X' to '!' when you hit it
            print("Player hit!")
            computer_grid[player_row][player_col] = "!"
            num_computer_ships -= 1
        else:
            print("Player missed!")

        print("\nComputer's turn:")
        computer_row, computer_col = computer_shot(player_grid)

        if player_grid[computer_row][computer_col] == "X":
            # replace battleship 'X' to '!' when you hit it
            print("Computer hit!")
            player_grid[computer_row][computer_col] = "!"
            num_player_ships -= 1
        else:
            print("Computer missed!")
        # display for each occurance of shot
        display_grids(player_grid, computer_grid)
        player_score = num_battleships - num_computer_ships
        computer_score = num_battleships - num_player_ships
        print(f"Player's Score: {player_score}\nComputer's Score: {computer_score}")

    if num_player_ships == 0:
        print("\nComputer wins! Player's fleet destroyed.")
    else:
        print("\nCongratulations! Player destroys the computer's fleet.")


design = """
                                Battleship Game
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \___________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww 
"""
print(design)
# call functionality
grid_size = int(input("Enter the grid size: "))
num_battleships = int(input("Enter the number of battleships: "))
play_against_computer(grid_size, num_battleships)
