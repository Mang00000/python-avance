import random


def ask_int(message: str, min: int, max: int):
    run2 = True
    while run2:
        try:
            check: int = int(input(message))
            if min <= check <= max:
                break
            else:
                print(f'veuillez rentrer un nombre entre {min} et {max}')
        except ValueError:
            print("veuillez rentrer un nombre valide")
    return check

numbers = "1234567890"

def ask_str(message: str):
    run = True
    while run:
        try_number = True
        check: str = str(input(message)).strip().upper()
        for e in check:
            if e in numbers:
                try_number = False
            if try_number:
                break
            else:
                print("veuillez rentrer une chaine de caractères svp")
 
    return check

def display_grid(grid):
    for line in grid:
        print(" | ".join(line))
        print("-" * (3*(grid_length+1)))

available = []
 
def init_available(grid):
 
    for i in range(grid_length):
        for j in range(grid_length):
            if grid[i][j] == " ":
                available.append((i,j))
    return available


grid_length = ask_int("Choisissez la taille de la grille entre 4 et 10", 4, 10)


def create_new_block(grid):
    coordinates = random.choice(available)
    line = coordinates[0]
    column = coordinates[1]

    value = 0
    temp = random.randint(0,10)
    if temp == 10:
        value = 4
    else: 
        value = 2


    grid[line][column] = str(value) 
    available.pop(available.index((line, column)))
 



run = True
def play():
    grid = [[" " for _ in range(grid_length)] for _ in range(grid_length)]
    available = init_available(grid)


    while run:
        display_grid(grid)

        movement = input("Dans quelle direction voulez vous allez ?").strip().upper()
        print(movement)

        if movement == "DROITE":
            for l in range(grid_length):
                for c in range(grid_length - 1):
                    if grid[l][c] != " ":
                        if grid[l][c+1] == " ":
                            grid[l][c+1] = grid[l][c]
                            grid[l][c] = " "
                        if grid[l][c+1] == grid[l][c]:
                            value = int(grid[l][c+1]) * 2
                            grid[l][c+1] = str(value)
                            grid[l][c] = " "
        available = init_available(grid)
        create_new_block(grid)





play()

