import random
import os


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def __str__(self) -> str:
        os.system("cls")
        chaine = ""
        for i in self.grid:
            chaine += "-" + "----"*self.size + "\n"
            for j in i:
                chaine += "| " + str(j) + " "
            chaine += "| \n"
        chaine += "-" + "----"*self.size + "\n"
        return chaine

#---------------------------------------------------------------------------------------------------------------#

def check_coordinates(Grid: Grid, x: int, y: int):
    if x < 0 or y < 0 or x >= len(Grid)-1 or y >= len(Grid)-1:
        return False
    else:
        return True

def EmptyTiles(Grid: Grid):
    return [(i, j) for i in range(Grid.size) for j in range(Grid.size) if Grid.grid[i][j] == " "]

def GenerateBlock(Grid: Grid) -> None:
    if len(EmptyTiles(Grid)) > 0:
        tiles: tuple[int, int] = random.choice(EmptyTiles(Grid))
        Grid.grid[tiles[0]][tiles[1]] = str(random.random() < 0.9 and 2 or 4)

#---------------------------------------------------------------------------------------------------------------#

def check_coordinates(Grid: Grid, x: int, y: int):
    if x < 0 or y < 0 or x >= len(Grid)-1 or y >= len(Grid)-1:
        return False
    else:
        return True

def EmptyTiles(Grid: Grid):
    return [(i, j) for i in range(Grid.size) for j in range(Grid.size) if Grid.grid[i][j] == " "]

def GenerateBlock(Grid: Grid) -> None:
    if len(EmptyTiles(Grid)) > 0:
        tiles: tuple[int, int] = random.choice(EmptyTiles(Grid))
        Grid.grid[tiles[0]][tiles[1]] = str(random.random() < 0.9 and 2 or 4)

#---------------------------------------------------------------------------------------------------------------#

def Game_init():
        tab: Grid = Grid(4)

        GenerateBlock(tab)

        tab.grid = [["4", "4", "2", " "],
                    ["8", "8", " ", "8"],
                    ["4", "8", "16", "32"],
                    [" ", "2", " ", " "]
                    ]
        
        GenerateBlock(tab)
        GenerateBlock(tab)
        print(tab)

        while not is_game_over(grid):
            while True:
                direction: int = int(input("Choisissez une direction : (haut : 1, bas : 2, gauche : 3, droite : 4)\n"))
                if 0 < direction <= 4:
                    break
                else:
                    print("Mauvaise direction")
            
            if direction == 'left' or direction == 'l':
                direction_left(grid)
            elif direction == 'right' or direction == 'r':
                direction_right(grid)
            elif direction == 'up' or direction == 'u':
                direction_up(grid)
            elif direction == 'down' or direction == 'd':
                direction_down(grid)
            generate_tile(grid)
            print_grid(grid)
        print("Game over!")
        
            # Haut
            if direction == 1:
                for i in range(tab.size - 1, 0, -1):
                    for j in range(tab.size):
                        if tab.grid[i][j] != " ":
                            
                            if tab.grid[i-1][j] == " ":
                                tab.grid[i-1][j] = tab.grid[i][j]
                                tab.grid[i][j] = " "
                                
                            if tab.grid[i][j] == tab.grid[i-1][j]:
                                value = int(tab.grid[i-1][j])*2
                                tab.grid[i-1][j] = str(value)
                                tab.grid[i][j] = " "
            
            # Bas
            if direction == 2:
                for i in range(tab.size - 1):
                    for j in range(tab.size):
                        if tab.grid[i][j] != " ":
                            
                            if tab.grid[i+1][j] == " ":
                                tab.grid[i+1][j] = tab.grid[i][j]
                                tab.grid[i][j] = " "
                                
                            if tab.grid[i][j] == tab.grid[i+1][j]:
                                value = int(tab.grid[i+1][j])*2
                                tab.grid[i+1][j] = str(value)
                                tab.grid[i][j] = " "
            
            # Gauche
            if direction == 3:
            
                for i in range(tab.size):
                    for j in range(tab.size - 1):
                        if tab.grid[i][j] != " ":
                            
                            if tab.grid[i][j-1] == " ":
                                tab.grid[i][j-1] = tab.grid[i][j]
                                tab.grid[i][j] = " "
                                
                            if tab.grid[i][j] == tab.grid[i][j-1]:
                                value = int(tab.grid[i][j-1])*2
                                tab.grid[i][j-1] = str(value)
                                tab.grid[i][j] = " "
            
            # Droite
            if direction == 4:
                for i in range(tab.size):
                    for _ in range(tab.size):
                        for j in range(tab.size -1, 0, -1):
                            if tab.grid[i][j] != " ":

                                if tab.grid[i][j] == tab.grid[i][j-1]:
                                    value = int(tab.grid[i][j])*2
                                    tab.grid[i][j] = str(value)
                                    tab.grid[i][j-1] = " "
                                
                            if tab.grid[i][j] == " ":
                                    tab.grid[i][j] = tab.grid[i][j-1]
                                    tab.grid[i][j-1] = " "

Game_init()