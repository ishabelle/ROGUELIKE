import engine

def display_board(board):
    ''' Displays complete game board on the screen. Returns nothing'''

    for row in board:
        print(''.join(row))


#display_board(engine.read_map("map_level1.txt"))

def display_inventory(player):
    inventory = f"Level:{player['level']} HP:{player['HP']} Attack:{player['attack']} Armor:{player['armor']} Weapon:{player['weapon']} Capacity:{player['capacity']}"
    print(inventory)