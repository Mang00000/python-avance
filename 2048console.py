import random
import os
os.system('cls')

def ask_int(message: str, min: int, max: int):
    while True:
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
    while True:
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

def init_available(grid):
    available = []

    for i in range(grid_length):
        for j in range(grid_length):
            if grid[i][j] == " ":
                available.append((i,j))
    return available


grid_length = ask_int("Choisissez la taille de la grille entre 4 et 10\n", 4, 10)


def create_new_block(grid, available):
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
    print(f"j'ai placé le bloc de valeur {value} aux coordonnées {line}, {column}")
 



def play():
    grid = [[" " for _ in range(grid_length)] for _ in range(grid_length)]
    available = init_available(grid)

    grid = [
        [" ","4","8","2"],
        ["16","4","4"," "],
        ["32","4"," "," "],
        [" "," "," "," "],
    ]


    while True:
        display_grid(grid)

        movement = input("Dans quelle direction voulez vous allez ?\n").strip().upper()
        print(movement)
        """
        if movement == "D":
            dx = 1
        if movement == "G":
            dx = -1
        """
        

        if movement == "D":
            for l in range(grid_length):
                for c in range(grid_length - 1, 0, -1):
                    if grid[l][c] != " ":

                        if grid[l][c-1] == grid[l][c]:
                            value = int(grid[l][c]) * 2
                            grid[l][c] = str(value)
                            grid[l][c-1] = " "

                else:
                    for c in range(grid_length - 1, 0, -1):
                        for i in range(c,0,-1):
                            if grid[l][i] != " ":
                                index = i
                                break
                            else:
                                index = 0

                        grid[l][index], grid[l][c] = grid[l][c], grid[l][index]

                        


        if movement == "G":
            for l in range(grid_length):
                for c in range(grid_length - 1):
                    if grid[l][c] != " ":

                        if grid[l][c+1] == grid[l][c]:
                            value = int(grid[l][c]) * 2
                            grid[l][c] = str(value)
                            grid[l][c+1] = " "

                else:
                    for c in range(grid_length - 1):
                        for i in range(c,grid_length-1):
                            if grid[l][i] != " ":
                                index = i
                                break
                            else:
                                index = -1

                        grid[l][index], grid[l][c] = grid[l][c], grid[l][index]

                            

        if movement == "B":
            for l in range(grid_length-1):
                for c in range(grid_length):
                    if grid[l][c] != " ":
                        if grid[l+1][c] == " ":
                            grid[l+1][c] = grid[l][c]
                            grid[l][c] = " "
                        
                        if grid[l+1][c] == grid[l][c]:
                            value = int(grid[l+1][c]) * 2
                            grid[l+1][c] = str(value)
                            grid[l][c] = " "
                            
        if movement == "H":
            for l in range(grid_length - 1, 0 ,-1):
                for c in range(grid_length):
                    if grid[l][c] != " ":
                        if grid[l-1][c] == " ":
                            grid[l-1][c] = grid[l][c]
                            grid[l][c] = " "
                        
                        if grid[l-1][c] == grid[l][c]:
                            value = int(grid[l-1][c]) * 2
                            grid[l-1][c] = str(value)
                            grid[l][c] = " "


        
        available = init_available(grid)
        create_new_block(grid, available)
        

play()