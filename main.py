import util
import engine
import ui
import constants


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 2


BOARD_WIDTH = 80
BOARD_HEIGHT = 15
#map_elements = []

CONTROL_DICT = {
    'w':[-1,0],
    's':[1,0],
    'a':[0,-1],
    'd':[0,1]
}


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Feel free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "height": 1,
        "width": 1,
        "health": 9,
        "lvl": 1,
        "strength": 1, # increases once you eat FOOD
        "charisma": 1, # increases as a bonus from events/meetings
        "sanity" : 1,   # Increases once you find another one of your babies 
        "max_hp": 10,
        "attack": 5   # for enemies
    }



def main():
    player = create_player()
    #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.read_map(file_name="map_level1.txt")

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()

        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()


        # #checking for obstacles around player before move
        # # side = 1
        # # no_obstacle_up = board[player["y"]-side][player["x"]] in constants.WALK_ON_ITEMS
        # # no_obstacle_down = board[player["y"]+side][player["x"]] in constants.WALK_ON_ITEMS
        # # no_obstacle_left = board[player["y"]][player["x"]-side] in constants.WALK_ON_ITEMS
        # # no_obstacle_right = board[player["y"]][player["x"]+side] in constants.WALK_ON_ITEMS

        # #player walking moves
        # # move_keys = constants.KEY_MOVES
        # # if key == 'w':
        #     player[PLAYER_START_Y] -= 1
        # # if key in 'wsad':
        # #     if key == 'w': # and no_obstacle_up:
        # #         player["y"] -= 1
        #     # if key in move_keys["down"] and no_obstacle_down:
        #     #     player["y"] += 1
        #     # if key in move_keys["left"] and no_obstacle_left:
        #     #     player["x"] -= 1
        #     # if key in move_keys["right"] and no_obstacle_right:
        #     #     player["x"] += 1        
