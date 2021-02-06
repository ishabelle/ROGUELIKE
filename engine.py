import ui
import random
import util

# def read_map(file_name):

#     with open(file_name, "r") as file:
#         read_data = file.read().splitlines()

#     board = [list(x) for x in read_data]

#     return board


def create_board(file_name):
    """
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    """
    with open(file_name, "r") as board_file:
        board = []
        for lines in board_file:
            elements = []
            for char in lines:
                if char == "\n":
                    break
                elements.append(char)
            board.append(elements)

    return board


def put_player_on_board(board, player):
    """
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    """
    board[player["y"]][player["x"]] = player["icon"]

    return board

    # player = {
    #     "icon" : "@",
    #     "y": 2,
    #     "x" : 3
        
    # }

    # for row in board:
    #     stat_y = player["y"]
    #     for col in board[stat_y]:
    #         stat_x = player["x"]
    #         board[stat_y][stat_x ]= player["icon"]

def player_coordinates_change(movement, player, board):
    """
    Changes player coordinates depending on user input

    Args:
    string: Key pressed by user
    dictionary: The player information - the icon and coordinates
    list: The game board

    Returns:
    dictionary: Updated player information
    """
    x = player["x"]
    y = player["y"]

    if movement == "w" and board[y-1][x] != "X":
        y -= 1
    elif movement == "s" and board[y+1][x] != "X":
        y += 1
    elif movement == "a" and board[y][x-1] != "X":
        x -= 1
    elif movement == "d" and board[y][x+1] != "X":
        x += 1
    # else:
    #     pass

    player["x"] = x
    player["y"] = y

    return player

def put_enemies_on_board(board, enemy):
    
    board[enemy["y"]][enemy["x"]] = enemy["icon"]
    return board


def enemy_movement(board, enemy):
    x = enemy["x"]
    y = enemy["y"]

    if enemy["type"] == "x_move":
        if board[y][x+1] == "X":
            enemy["direction"] = "left"
        elif board[y][x-1] == "X":
            enemy["direction"] = "right"
        if enemy["direction"] == "left":
            x -= 1
        elif enemy["direction"] == "right":
            x += 1
    enemy["x"] = x

    if enemy["type"] == "y_move":
        if board[y-1][x] == "X":
            enemy["direction"] = "up"
        elif board[y+1][x] == "X":
            enemy["direction"] = "down"
        if enemy["direction"] == "down":
            y -= 1
        elif enemy["direction"] == "up":
            y += 1
    enemy["y"] = y

    return enemy

def put_items_on_board(board, item):

    board[item["y"]][item["x"]] = item["icon"]
    return board


def enemy_board_interaction(board, enemy, player):
    
    player_nearby_x = player["x"]
    player_nearby_y = player["y"]
    enemy_nearby_x = enemy["x"]
    enemy_nearby_y = enemy["y"]
    if enemy_nearby_x == player_nearby_x and enemy_nearby_y == player_nearby_y:
        return enemy_interaction(player, enemy)
    return [player, enemy]

def item_board_interaction(board, item, player):
    player_nearby_x = player["x"]
    player_nearby_y = player["y"]
    item_nearby_x = item["x"]
    item_nearby_y = item["y"]
    if item_nearby_x == player_nearby_x and item_nearby_y == player_nearby_y:
        player = item_interaction(player, item)
        item["on_board"] = 0
    #ui.display_inventory(player)
    return [player, item]

def item_interaction(player, item):
    if item["type"] == "clothes":
        player["clothes"] += 1
        player["armor"] = player["armor"] + item["armor"]
        lift = player["capacity"]
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item["weight"]
        player["capacity"] = f"{new_weight}/100"
        #ui.display_inventory(player)
        
    
    elif item["type"] == "weapon":
        player["attack"] = item["damage"]
        player["weapon"] = item["name"]
        lift = player["capacity"]
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item["weight"]
        player["capacity"] = f"{new_weight}/100"
        #ui.display_inventory(player)
        
   
    elif item["type"] == "food":
        player["food"] += 1
        player["HP"] = player["HP"] + item["HP"]
        lift = player["capacity"]
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item["weight"]
        player["capacity"] = f"{new_weight}/100"
        #ui.display_inventory(player)
   
    return player


# def put_gate(board, player):
#     if player["food"] != 4:
#         board[28][75] = "X"
#     return board


def enemy_interaction(player, enemy):
    while player["HP"] > 0 and enemy["HP"] > 0:
        enemy["HP"] = enemy["HP"] - player["attack"]
        player["HP"] = player["HP"] - enemy["attack"]*((100 - player["armor"])/100)
    print([player, enemy])
    return [player, enemy]

