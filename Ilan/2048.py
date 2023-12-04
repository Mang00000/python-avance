import random
# import keyboard
import Tools

class Grid:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def __str__(self) -> str:
        chaine = "\n"
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
        Grid.grid[tiles[0]][tiles[1]] = random.random() < 0.9 and 2 or 4


def droite(Grid: Grid, x: int, y: int):
    if check_coordinates(Grid.grid, x, y+1) == False:
        return " "
    else:
        if Grid.grid[x][y] != " ":
            if Grid.grid[x][y] == Grid.grid[x][y+1]:
                Grid.grid[x][y+1] = str(int(Grid.grid[x][y]) * 2)
                Grid.grid[x][y] = " "
                return droite(Grid, x, y+1)

#---------------------------------------------------------------------------------------------------------------#

def Game_init():
        tab: Grid = Grid(4)
        GenerateBlock(tab)
        
        while True:
            GenerateBlock(tab)
            print(tab.grid)
            print(tab)

            while True:
                direction: int = Tools.AskInt("Choisissez une direction : (haut : 1, bas : 2, gauche : 3, droite : 4)")
                if 0 < direction <= 4:
                    break
                else:
                    print("Mauvaise direction")
            # while True:
            #     if keyboard.is_pressed("up"):
            #         print("up")
            #     elif keyboard.is_pressed("down"):
            #         print("down")
            #     elif keyboard.is_pressed("left"):
            #         print("left")
            #     elif keyboard.is_pressed("right"):
            #         print("right")

            if direction == 4:
                for i in range(tab.size):
                    for j in range(tab.size):
                        droite(tab, i, j)
                #         if tab.grid[i][j] != "None":
                #             if check_coordinates(tab.grid, i, j+1):
                #                 if tab.grid[i][j] == tab.grid[i][j+1]:
                #                     tab.grid[i][j+1] = str(int(tab.grid[i][j]) * 2)
                #                     tab.grid[i][j] = "None"
                #         else:
                #             if check_coordinates(tab.grid, i, j+1):
                #                 tab.grid[i][j+1] = tab.grid[i][j]
                #                 tab.grid[i][j] = "None"
Game_init()