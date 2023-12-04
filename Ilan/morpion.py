from random import randint, choice
import Tools as T

def Create_Board(n: int) -> list[list[str]]:
    board = [[" " for i in range(n)] for i in range(n)]
    return board

def Load_Board(board: list[list[str]]):
    affiche = ""
    for i in board:
        affiche += "-" + "----"*len(board) + "\n"
        for j in i:
            affiche += "| " + str(j) + " "
        affiche += "| \n"
    affiche += "-" + "----"*len(board)
    return affiche

def Update_Board(x: int, y: int, board: list[list[str]], Player: str):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board):
            print("Erreur")
            return
        else:
            if board[x][y] == " ":
                board[x][y] = Player
                return board

def Update_User(board: list[list[str]]):
    while True:
        print("\n-------------------------------------------")
        x: int = T.AskInt("Choisir la ligne de la grille où tu souhaite jouer")-1
        y: int = T.AskInt("Choisir la colone de la grille où tu souhaite jouer")-1
        
        if Update_Board(x, y, board, "X") != None:
            board = Update_Board(x, y, board, "X")
            return x, y

def Update_IA(board: list[list[str]], win_length: int = 3) -> tuple[int, int]:
    # IA can Win
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == " ":
                board[row][col] = "O"
                if CheckWin(row, col, "O", board, win_length):
                    print("IA can Win")
                    return row, col
                else:
                    board[row][col] = " "
    # IA can Block
    else:
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    if CheckWin(row, col, "X", board, win_length):
                        board[row][col] = "O"
                        print("IA can Block")
                        return row, col
                    else:
                        board[row][col] = " "
    # IA play random
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == " "]
    if empty_cells:
        choice_IA = choice(empty_cells)
        board = Update_Board(choice_IA[0], choice_IA[1], board, "O")
        print("IA play randomly")
        return choice_IA
    else:
        return None

def check_coordinates(board, x, y):
    if x < 0 or y < 0 or x >= len(board)-1 or y >= len(board)-1:
        return False
    else:
        return True

def check_line(x: int, y: int, player: str, board, win_length: int = 3):
    compteur = 1
    for i in range(1, win_length):
        if check_coordinates(board, x+1, y) == False:
            continue
        if board[x+i][y] == player:
            compteur += 1
        else:
            break
    for i in range(1, win_length):
        if check_coordinates(board, x-1, y) == False:
            continue
        if board[x-i][y] == player:
            compteur += 1
        else:
            break
    return compteur >= win_length

def check_column(x: int, y: int, player: str, board, win_length: int = 3):
    compteur = 1
    for i in range(1, win_length):
        if check_coordinates(board, x, y+1) == False:
            continue
        if board[x][y+i] == player:
            compteur += 1
        else:
            break
    for i in range(1, win_length):
        if check_coordinates(board, x, y-1) == False:
            continue
        if board[x][y-i] == player:
            compteur += 1
        else:
            break
    return compteur >= win_length

def check_left_diagonal(x: int, y: int, player: str, board, win_length: int = 3):
    compteur = 1
    for i in range(1, win_length):
        if check_coordinates(board, x+i, y+i) == False:
            continue
        if board[x+i][y+i] == player:
            compteur += 1
        else:
            break
    for i in range(1, win_length):
        if check_coordinates(board, x-i, y-i) == False:
            continue
        if board[x-i][y-i] == player:
            compteur += 1
        else:
            break
    return compteur >= win_length

def check_right_diagonal(x: int, y: int, player: str, board, win_length: int = 3):
    compteur = 1
    for i in range(1, win_length):
        if check_coordinates(board, x-i, y+i) == False:
            continue
        if board[x-i][y+i] == player:
            compteur += 1
        else:
            break
    for i in range(1, win_length):
        if check_coordinates(board, x+i, y-i) == False:
            continue
        if board[x+i][y-i] == player:
            compteur += 1
        else:
            break
    return compteur >= win_length

def CheckWin(x: int, y: int, player: str, board: list[list[str]], win_length: int = 3):
    """Check if the player win the game
    Args:
        x (int): x coordinate
        y (int): y coordinate
        player (str): player symbol
        board (list[list[str]]): board
        win_length (int, optional): number of symbols to align to win. Defaults to 3.
    Returns:
        bool: True if the player win, else False
    """
    return check_line(x, y, player, board, win_length) or check_column(x, y, player, board, win_length) or check_left_diagonal(x, y, player, board, win_length) or check_right_diagonal(x, y, player, board, win_length)

def CheckEqual(board):
    for i in board:
        for j in i:
            if j == " ":
                return False
    return True

def find_empty_strings(list):
    return [(i, j) for i in range(len(list)) for j in range(len(list[i])) if list[i][j] == " "]

def Game():
    board = Create_Board(T.AskInt("Choisir une taille pour la grille de morpion"))
    win_length = T.AskInt("Combien de symboles à alignés pour gagner ?")

    while True:
        print(Load_Board(board))

        x, y = Update_User(board)

        if CheckWin(x, y, "X", board, win_length):
            print(Load_Board(board))
            print("X's Win !")
            break
        
        if CheckEqual(board):
            print(Load_Board(board))
            print ("Égalité")
            break
        
        #-------------------------------------------------------------------------
        
        IA_Coord_x, IA_Coord_y = Update_IA(board, win_length)
        
        if CheckWin(IA_Coord_x, IA_Coord_y, "O", board, win_length):
            print(Load_Board(board))
            print("O's Win !")
            break
        
        if CheckEqual(board):
            print(Load_Board(board))
            print ("Égalité")
            break
Game()

# def test_CheckWin():
#     # Test case 1: Horizontal win
#     board = [['X', 'X', 'X'],
#              ['O', 'O', ''],
#              ['', '', '']]
#     assert CheckWin(0, 0, 'X', board) == True

#     # Test case 2: Vertical win
#     board = [['X', 'O', ''],
#              ['X', 'O', ''],
#              ['X', '', '']]
#     assert CheckWin(2, 0, 'X', board) == True

#     # Test case 3: Left diagonal win
#     board = [['X', 'O', ''],
#              ['O', 'X', ''],
#              ['', '', 'X']]
#     assert CheckWin(2, 2, 'X', board) == True

#     # Test case 4: Right diagonal win
#     board = [['', 'O', 'X'],
#              ['O', 'X', ''],
#              ['X', '', '']]
#     assert CheckWin(0, 2, 'X', board) == True

#     # Test case 5: No win
#     board = [['X', 'O', 'X'],
#              ['O', 'X', ''],
#              ['', 'X', 'O']]
#     assert CheckWin(1, 1, 'X', board) == False

#     print("All test cases pass")
# test_CheckWin()