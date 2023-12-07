import random
import os
import time
 
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
 
 
def is_game_won(grid):
    for row in grid:
        for cell in row:
            if cell == "2048":
                return True
    return False

def is_game_over(grid):
    for row in grid:
        for cell in row:
            if cell == " ":
                return False

    for l in range(grid_length):
        for c in range(grid_length-1):
            if grid[l][c] == grid[l][c+1] or grid[c][l] == grid[c+1][l]:
                return False

    return True



def is_valid_movement(movement):
    valid_movements = ["D", "DROITE", "RIGHT", "G", "GAUCHE", "LEFT", "Q", "H", "HAUT", "TOP", "Z", "B", "BAS", "BOTTOM", "S"]
    return movement in valid_movements

def display_grid(grid):
    cell_width = 6
    line_width = (cell_width + 1) * grid_length + 1 

    print("-" * line_width)
    for line in grid:
        formatted_line = "|" + "|".join("{:^{width}}".format(cell, width=cell_width) for cell in line) + "|"
        print(formatted_line)
        print("-" * line_width)

def init_available(grid):
    available = []
 
    for i in range(grid_length):
        for j in range(grid_length):
            if grid[i][j] == " ":
                available.append((i,j))
    return available
 
print("---------------------☺---------------------")
print("Bienvenue sur ce jeu du 2048 !")

reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
if reponse.upper() == "Y":
    # Affichage des règles du jeu
    print("---------------------☺---------------------")
    print("Règles :")
    print("- Le but du jeu est d'additionner des chiffres afin d'atteindre 2048. - ")
    print("------> - La partie se joue sur plusieurs tour.")
    print("------> - A chaque tour un chiffre (2 ou 4) est generé aleatoirement sur une case.")
    print("------> - Vous avez le choix de déplacer l'intégralité du tableau vers une direction.")
    print("------> - Lors du deplacement les chiffres égaux entrant en collision sont additionés.")
    print("------> - Pour gagner, il vous faudra reussir à atteindre le chiffre 2048 sans etre bloquer.")
    print("------> - Réfléchissez bien et n'oubliez pas que lorsque que plus aucune fusion n'est possible et que le tableau est plein, c'est perdu !")
 
print("---------------------☺---------------------") 
grid_length = ask_int("Choisissez la taille de la grille entre 4 et 10 : ", 4, 10)
print("")
print("\n+" + "-" * 37 + "+")
print("|{:^27}|".format("C'est parti alors, Amusez-vous bien !"))
print("+" + "-" * 37 + "+")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")
 
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
    print("")
    print(f"Nouveau chiffre -> {value} <- aux coordonnées {line }, {column}")
 
 

def is_grid_empty(grid):
    for row in grid:
        for cell in row:
            if cell != " ":
                return False
    return True




run = True
def play():
    grid = [[" " for _ in range(grid_length)] for _ in range(grid_length)]
    if is_grid_empty(grid):
        available = init_available(grid)
        create_new_block(grid, available)
        create_new_block(grid, available)
 
    #grid test Droite
    """
    grid = [
                ["2","2","2","2"],
                ["32","32"," "," "],
                ["4","2","2"," "],
                ["2"," "," ","2"]
             ]
   """

    #grid test Gauche
    """
    grid = [
                [" "," "," ","4"],
                [" "," ","32","32"],
                [" ","2","2","4"],
                ["2"," "," ","2"]
             ]
    """

    #grid test Haut
    """
    grid = [
                [" ","4"," ","2"],
                [" "," ","2","2"],
                ["32","4","2","2"],
                ["32","4","4","2"]
             ]
    """

    #grid test Bas
    """
    grid = [
                ["32","4","4","2"],
                ["32","4","2","2"],
                [" "," ","2","2"],
                [" ","4"," ","2"]
             ]
    """

    available = init_available(grid)
    

    while run:
        display_grid(grid)
        
        print("")
        movement = input("Dans quelle direction voulez vous allez ? ").strip().upper()
        print("")
        initial_grid = [row[:] for row in grid]

        if not is_valid_movement(movement):
            os.system("cls" if os.name == "nt" else "clear")
            print("")
            print("!! Mouvement invalide. !!")
            print("")
            print("4 types de commandes disponibles : - Z/Q/S/D")
            print("                                   - H/B/G/D")
            print("                                   - Haut/Bas/Gauche/Droite")
            print("                                   - Top/Bottom/Left/Right")
            continue

        os.system("cls" if os.name == "nt" else "clear")

        """
        if movement == "D":
            dx = 1
        if movement == "G":
            dx = -1
        """

        if movement == "D" or movement == "DROITE" or movement == "RIGHT":
            for l in range(grid_length):
                #déplacement
                for c in range(grid_length - 1, 0, -1):
                    for i in range(c,0,-1):
                        if grid[l][i] != " ":
                            index = i
                            break
                        else:
                            index = 0

                    grid[l][index], grid[l][c] = grid[l][c], grid[l][index]
                #addition
                for c in range(grid_length - 1, 0, -1):
                    if grid[l][c] != " ":

                        if grid[l][c-1] == grid[l][c]:
                            value = int(grid[l][c]) * 2
                            grid[l][c] = str(value)
                            grid[l][c-1] = " "

                #déplacement    
                
                for c in range(grid_length - 1, 0, -1):
                    for i in range(c,0,-1):
                        if grid[l][i] != " ":
                            index = i
                            break
                        else:
                            index = 0

                    grid[l][index], grid[l][c] = grid[l][c], grid[l][index]


       
        if movement == "G" or movement == "GAUCHE" or movement == "LEFT" or movement == "Q":
            for l in range(grid_length):
                #déplacement
                for c in range(grid_length - 1):
                    for i in range(c,grid_length-1):
                        if grid[l][i] != " ":
                            index = i
                            break
                        else:
                            index = -1

                    grid[l][index], grid[l][c] = grid[l][c], grid[l][index]
                #addition
                for c in range(grid_length - 1):
                    if grid[l][c] != " ":

                        if grid[l][c+1] == grid[l][c]:
                            value = int(grid[l][c]) * 2
                            grid[l][c] = str(value)
                            grid[l][c+1] = " "

                #déplacement
                for c in range(grid_length - 1):
                    for i in range(c,grid_length-1):
                        if grid[l][i] != " ":
                            index = i
                            break
                        else:
                            index = -1

                    grid[l][index], grid[l][c] = grid[l][c], grid[l][index]


        if movement == "H" or movement == "HAUT" or movement == "TOP" or movement == "Z":
            for l in range(grid_length - 1):
                #déplacement
                for c in range(grid_length):
                    for i in range(l,grid_length-1): # itérer toutes les cases au dessus de la case acutelle
                        if grid[i][c] != " ":
                            index = i
                            break
                        else:
                            index = -1

                    grid[index][c], grid[l][c] = grid[l][c], grid[index][c]
                #addition
                for c in range(grid_length):
                    if l != 0:
                        if grid[l][c] != " ":

                            if grid[l-1][c] == grid[l][c]:
                                value = int(grid[l][c]) * 2
                                grid[l-1][c] = str(value)
                                grid[l][c] = " "

                #déplacement    
                
                for c in range(grid_length):
                    for i in range(l,grid_length-1): # itérer toutes les cases au dessus de la case acutelle
                        if grid[i][c] != " ":
                            index = i
                            break
                        else:
                            index = -1

                    grid[index][c], grid[l][c] = grid[l][c], grid[index][c]
 

        if movement == "B" or movement == "BAS" or movement == "BOTTOM" or movement == "S":
            for l in range(grid_length - 1, 0, -1):
                #déplacement
                for c in range(grid_length):
                    for i in range(l,0,-1): # itérer toutes les cases au dessus de la case acutelle
                        if grid[i][c] != " ":
                            index = i
                            break
                        else:
                            index = 0

                    grid[index][c], grid[l][c] = grid[l][c], grid[index][c]
                #addition
                for c in range(grid_length):
                    if l != grid_length -1:
                        if grid[l][c] != " ":

                            if grid[l+1][c] == grid[l][c]:
                                value = int(grid[l][c]) * 2
                                grid[l+1][c] = str(value)
                                grid[l][c] = " "

                #déplacement    
                
                for c in range(grid_length):
                    for i in range(l,0,-1): # itérer toutes les cases au dessus de la case acutelle
                        if grid[i][c] != " ":
                            index = i
                            break
                        else:
                            index = 0

                    grid[index][c], grid[l][c] = grid[l][c], grid[index][c]
                       
        display_grid(grid)
        os.system("cls" if os.name == "nt" else "clear")

        if movement == "D" or movement == "DROITE" or movement == "RIGHT":
            print("\n+" + "-" * 41 + "+")
            print("|{:^27}|".format("Vous avez déplacé le tout vers la droite."))
            print("+" + "-" * 41 + "+")
        elif movement == "G" or movement == "GAUCHE" or movement == "LEFT" or movement == "Q":
            print("\n+" + "-" * 41 + "+")
            print("|{:^27}|".format("Vous avez déplacé le tout vers la gauche."))
            print("+" + "-" * 41 + "+")
        elif movement == "H" or movement == "HAUT" or movement == "TOP" or movement == "Z":
            print("\n+" + "-" * 39 + "+")
            print("|{:^27}|".format("Vous avez déplacé le tout vers le haut."))
            print("+" + "-" * 39 + "+")
        elif movement == "B" or movement == "BAS" or movement == "BOTTOM" or movement == "S":
            print("\n+" + "-" * 38 + "+")
            print("|{:^27}|".format("Vous avez déplacé le tout vers le bas."))
            print("+" + "-" * 38 + "+")

        if is_game_won(grid):
            print("\n+" + "-" * 27 + "+")
            print("|{:^27}|".format("Victory !"))
            print("+" + "-" * 27 + "+")
            break
        elif is_game_over(grid):
            print("\n+" + "-" * 27 + "+")
            print("|{:^27}|".format("Game Over!"))
            print("+" + "-" * 27 + "+")
            break
 
        

        try:
            available = init_available(grid)
            create_new_block(grid, available)
        except Exception as e:
            if grid == initial_grid:
                display_grid(grid)
                print("\n+" + "-" * 27 + "+")
                print("|{:^27}|".format("Game Over!"))
                print("+" + "-" * 27 + "+")
                break

         

        available = init_available(grid)

        
play()