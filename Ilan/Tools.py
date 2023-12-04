Retry_List: list = ["y", "n"]

# ---------------------------------------------------------------------------

def AskInt(Message: str) -> int:
    while True:
        Integer: str = input(Message + "\n")

        if Integer.isdigit():
            return int(Integer)

        print("Erreur\n")

# ---------------------------------------------------------------------------

def Ask_Limited_Int(Message: str, MinInt: int, MaxInt: int) -> int:
    while True:
        Integer: str = input(Message + "\n")

        if Integer.isdigit() and MinInt <= int(Integer) <= MaxInt:
            return int(Integer)

        print("Erreur\n")

# ---------------------------------------------------------------------------

def Ask_Choice(allowed_choices: list[str]) -> str :
    message: str = "Choisir entre : "
    for i in allowed_choices:
        message += str(i) + "  "
        
    while True:
        choice: str = input(message+"\n").lower()
        if choice in allowed_choices:
            return choice
    
        print("Erreur\n")

# ---------------------------------------------------------------------------

