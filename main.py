import util
import engine
import ui

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
    pass


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
