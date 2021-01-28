import string

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 2

BOARD_WIDTH = 80
BOARD_HEIGHT = 15

OBSTACLES = {
    "wall" : "X",
    "door" : "|",
    "boss_door" : "#",
    "next_level_opening" : "O"
}

#WALK_ON_ITEMS = "ABCDEFGHIJKLMNPRSTUWYZ " #EXCLUDED 'X' BECAUSE IT IS OUR WALL and 'O' because its special
WALK_ON_ITEMS = [" "]
ITEMS_TO_PICK_UP = "BWSPF"

ENEMIES = {
    "IKEA_worker" : "W",
    "old_lady" : "H",
    "cashier" : "$"
}

KEY_MOVES = {"left": ["a", "4"],
                "right": ["d", "6"],
                "up": ["w", "8"],
                "down": ["s", "2"],
                }

KEY_INFO = set()
KEY_INFO = {"inventory": ("i"),
            "customize": ("k"),
                "stats" : ("b"),
                "exit": ("q"),
                "story": ("p"),
                "verbal_attack": ("v"),
                }

KEY_FIGHT = {
                "Fight": ("1"),
                "Use inventory": ("2"),
                "Try to escape": ("3")
}