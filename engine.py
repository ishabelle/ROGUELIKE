
def read_map(file_name):

    with open(file_name, 'r') as file:
        read_data = file.read().splitlines()

    board = [list(x) for x in read_data]

    return board


# def create_board(width, height):
#     '''
#     Creates a new game board based on input parameters.

#     Args:
#     int: The width of the board
#     int: The height of the board

#     Returns:
#     list: Game board
#     '''
#     pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass


# name = "map_level1.txt"
# print(read_map(name))