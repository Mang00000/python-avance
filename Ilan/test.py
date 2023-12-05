import random
import os

# Function to initialize the game grid
def initialize_grid(size):
    grid = [[0] * size for _ in range(size)]
    return grid

# Function to generate a new tile with value 2 or 4
def generate_tile(grid):
    size = len(grid)
    empty_cells = [(i, j) for i in range(size) for j in range(size) if grid[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        value = random.choices([2, 4], weights=[9, 1])[0]
        grid[row][col] = value

# Function to print the game grid
def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    size = len(grid)
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end='\t')
        print()

# Function to move the tiles to the left
def move_left(grid):
    size = len(grid)
    for i in range(size):
        merged = [False] * size
        for j in range(1, size):
            if grid[i][j] != 0:
                k = j
                while k > 0 and grid[i][k-1] == 0:
                    grid[i][k-1] = grid[i][k]
                    grid[i][k] = 0
                    k -= 1
                if k > 0 and grid[i][k-1] == grid[i][k] and not merged[k-1]:
                    grid[i][k-1] *= 2
                    grid[i][k] = 0
                    merged[k-1] = True

# Function to move the tiles to the right
def move_right(grid):
    size = len(grid)
    for i in range(size):
        merged = [False] * size
        for j in range(size-2, -1, -1):
            if grid[i][j] != 0:
                k = j
                while k < size-1 and grid[i][k+1] == 0:
                    grid[i][k+1] = grid[i][k]
                    grid[i][k] = 0
                    k += 1
                if k < size-1 and grid[i][k+1] == grid[i][k] and not merged[k+1]:
                    grid[i][k+1] *= 2
                    grid[i][k] = 0
                    merged[k+1] = True

# Function to move the tiles up
def move_up(grid):
    size = len(grid)
    for j in range(size):
        merged = [False] * size
        for i in range(1, size):
            if grid[i][j] != 0:
                k = i
                while k > 0 and grid[k-1][j] == 0:
                    grid[k-1][j] = grid[k][j]
                    grid[k][j] = 0
                    k -= 1
                if k > 0 and grid[k-1][j] == grid[k][j] and not merged[k-1]:
                    grid[k-1][j] *= 2
                    grid[k][j] = 0
                    merged[k-1] = True

# Function to move the tiles down
def move_down(grid):
    size = len(grid)
    for j in range(size):
        merged = [False] * size
        for i in range(size-2, -1, -1):
            if grid[i][j] != 0:
                k = i
                while k < size-1 and grid[k+1][j] == 0:
                    grid[k+1][j] = grid[k][j]
                    grid[k][j] = 0
                    k += 1
                if k < size-1 and grid[k+1][j] == grid[k][j] and not merged[k+1]:
                    grid[k+1][j] *= 2
                    grid[k][j] = 0
                    merged[k+1] = True

# Function to check if the game is over
def is_game_over(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                return False
            if i > 0 and grid[i][j] == grid[i-1][j]:
                return False
            if i < size-1 and grid[i][j] == grid[i+1][j]:
                return False
            if j > 0 and grid[i][j] == grid[i][j-1]:
                return False
            if j < size-1 and grid[i][j] == grid[i][j+1]:
                return False
    return True

# Main game loop
def play_game():
    size = 4
    grid = initialize_grid(size)
    generate_tile(grid)
    generate_tile(grid)
    print_grid(grid)
    while not is_game_over(grid):
        move = input("Enter move (left/right/up/down): ")
        if move == 'left':
            move_left(grid)
        elif move == 'right':
            move_right(grid)
        elif move == 'up':
            move_up(grid)
        elif move == 'down':
            move_down(grid)
        generate_tile(grid)
        print_grid(grid)
    print("Game over!")

# Start the game
play_game()
