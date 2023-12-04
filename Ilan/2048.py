import random
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

#---------------------------------------------------------------------------------------------------------------#

def Game_init():
        tab: Grid = Grid(4)
        GenerateBlock(tab)
        
        while True:
            GenerateBlock(tab)
            print(tab)

            while True:
                direction: int = Tools.AskInt("Choisissez une direction : (haut : 1, bas : 2, gauche : 3, droite : 4)")
                if 0 < direction <= 4:
                    break
                else:
                    print("Mauvaise direction")
    
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

            if direction == 3:
                for i in range(tab.size):
                    for j in range(tab.size - 1, 0, -1):
                        if tab.grid[i][j] != " ":
                            
                            if tab.grid[i][j-1] == " ":
                                tab.grid[i][j-1] = tab.grid[i][j]
                                tab.grid[i][j] = " "
                                
                            if tab.grid[i][j] == tab.grid[i][j-1]:
                                value = int(tab.grid[i][j-1])*2
                                tab.grid[i][j-1] = str(value)
                                tab.grid[i][j] = " "
                            
                            

            if direction == 4:
                for i in range(tab.size):
                    for j in range(tab.size - 1):
                        if tab.grid[i][j] != " ":
                            
                            if tab.grid[i][j+1] == " ":
                                tab.grid[i][j+1] = tab.grid[i][j]
                                tab.grid[i][j] = " "
                                
                            if tab.grid[i][j] == tab.grid[i][j+1]:
                                value = int(tab.grid[i][j+1])*2
                                tab.grid[i][j+1] = str(value)
                                tab.grid[i][j] = " "


Game_init()