from random import randint


def create_grid(size):

    grid = []
    for _ in range(size):
        row = ["O"] * size
        grid.append(row)
    return grid


def display_grid(grid):
    for row in grid:

        print(" ".join(row))


def display_grids(player_grid, computer_grid):

    size = len(player_grid)

    print("Player's Grid\t\t\tComputer's Grid")
    for i in range(size):
        row_str = " ".join(player_grid[i])
        row_str += "\t\t\t"
        row_str += " ".join(computer_grid[i])
        print(row_str)


def place_battleships(grid, num_battleships):
    size = len(grid)
    for _ in range(num_battleships):
        row = randint(0, size - 1)
        col = randint(0, size - 1)
        if grid[row][col] == "X":
            continue
        grid[row][col] = "X"


def is_valid_shot(grid, row, col):
    size = len(grid)
    return 0 <= row < size and 0 <= col < size


def computer_shot(grid):
    size = len(grid)
    row = randint(0, size - 1)
    col = randint(0, size - 1)
    return row, col


def play_against_computer(size, num_battleships):

    player_grid = create_grid(size)
    computer_grid = create_grid(size)
    place_battleships(player_grid, num_battleships)
    place_battleships(computer_grid, num_battleships)

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

            print("Player hit!")
            computer_grid[player_row][player_col] = "!"
            num_computer_ships -= 1
        else:
            print("Player missed!")

        print("\nComputer's turn:")
        computer_row, computer_col = computer_shot(player_grid)

        if player_grid[computer_row][computer_col] == "X":

            print("Computer hit!")
            player_grid[computer_row][computer_col] = "!"
            num_player_ships -= 1
        else:
            print("Computer missed!")

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

grid_size = int(input("Enter the grid size: "))
num_battleships = int(input("Enter the number of battleships: "))
play_against_computer(grid_size, num_battleships)
