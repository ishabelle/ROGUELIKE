import util
import engine
import ui
import items_to_collect
import enemies
import time

PLAYER_ICON = "@"
PLAYER_START_X = 3
PLAYER_START_Y = 2

BOARD_WIDTH = 80
BOARD_HEIGHT = 15
#map_elements = []


def create_player():
    """
    Creates a "player" dictionary for storing all player related informations - i.e. player icon, player position.
    Feel free to extend this dictionary!

    Returns:
    dictionary
    """
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["collection"] = 0
    player["food"] = 0
    player["weapons"] = 0
    player["weapon"] = "None"
    player["attack"] = 0
    player["HP"] = 50
    player["armor"] = 0
    player["capacity"] = "0/100"
    player["level"] = 1
    return player
    

# def main():
#     player = create_player()
#     #board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
#     board = engine.create_board(file_name="levels/map_level1.txt")

#     util.clear_screen()
#     is_running = True
#     while is_running:
#         engine.put_player_on_board(board, player)
#         ui.display_board(board)

#         key = util.key_pressed()

#         if key == "q":
#             is_running = False
#         else:
#             pass
#         util.clear_screen()


def level_one_start(player, enemies_list, file_name):

    # Creating objects and items

    item_one = items_to_collect.create_baby_angel_head(1, 2)

    # item_two = items.create_banana(23, 6)
    # item_three = items.create_knife(15, 14)
    # item_four = items.create_shoes(63, 5)
    # item_five = items.create_apple(35, 27)
    # item_six = items.create_banana(77, 2)

    # Creating interactions

    objects_one = [player, item_one]
    # objects_two = [player, item_two]
    # objects_three = [player, item_three]
    # objects_four = [player, item_four]
    # objects_five = [player, item_five]
    # objects_six = [player, item_six]

    is_running = True
    
    time.sleep(1)

    while is_running:
        key = util.key_pressed()
        util.clear_screen()
        if key == "q":
            assert False
        board = engine.create_board(file_name)
        lift = player["capacity"]
        lift_list = lift.split("/")
        engine.put_gate(board, player)
        if int(lift_list[0]) < 100:
            player = engine.player_coordinates_change(key, player, board)
        board = engine.put_player_on_board(board, player)
        if player["x"] == 77 and player["y"] == 28:
            player["level"] = 2
            is_running = False
        for index in range(len(enemies_list)):
            enemy = enemies_list[index]
            if enemy["HP"] > 0:
                enemy = engine.enemy_movement(board, enemy)
                board = engine.put_enemies_on_board(board, enemy)
                fight = engine.enemy_board_interaction(board, enemy, player)
                player = fight[0]
                enemy = fight[1]
                enemies_list[index] = enemy
        if item_one["on_board"] == 1:
            board = engine.put_items_on_board(board, item_one)
            player = objects_one[0]
            item_one = objects_one[1]
            objects_one = engine.item_board_interaction(board, item_one, player)
        if item_two["on_board"] == 1:
            board = engine.put_items_on_board(board, item_two)
            player = objects_two[0]
            item_two = objects_two[1]
            objects_two = engine.item_board_interaction(board, item_two, player)
        if item_three["on_board"] == 1:
            board = engine.put_items_on_board(board, item_three)
            player = objects_three[0]
            item_three = objects_three[1]
            objects_three = engine.item_board_interaction(board, item_three, player)
        if item_four["on_board"] == 1:
            board = engine.put_items_on_board(board, item_four)
            player = objects_four[0]
            item_four = objects_four[1]
            objects_four = engine.item_board_interaction(board, item_four, player)
        if item_five["on_board"] == 1:
            board = engine.put_items_on_board(board, item_five)
            player = objects_five[0]
            item_five = objects_five[1]
            objects_five = engine.item_board_interaction(board, item_five, player)
        if item_six["on_board"] == 1:
            board = engine.put_items_on_board(board, item_six)
            player = objects_six[0]
            item_six = objects_six[1]
            objects_six = engine.item_board_interaction(board, item_six, player)
        if player["HP"] <= 0:
            print("Game over")
            return player
        engine.put_gate(board, player)
        ui.display_board(board)
        ui.display_inventory(player)

    return player


def level_two_start(player, enemies_list, file_name):
    pass


def level_three_start(player, enemies_list, file_name):
    pass


def restart(player, hp):
    if util.key_pressed() == "n":
        return player
    if util.key_pressed() == "y":
        player["HP"] = hp

def main():
    
    player = create_player()
    while player["level"] == 1 and player["HP"] > 0:
        try:
            file_name = "levels/map_level1.txt"
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_one_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            util.clear_screen()
            ui.display_board(engine.create_board("messages/restart_screen.txt"))
            key = util.key_pressed()
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player["x"] = 1
        player["y"] = 1
    while player["level"] == 2 and player["HP"] > 0:
        try:
            file_name = "levels/map_level2.txt"
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_two_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            util.clear_screen()
            ui.display_board(engine.create_board("messages/restart_screen.txt"))
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player["x"] = 1
        player["y"] = 1
    while player["level"] == 3 and player["HP"] > 0:
        try:
            file_name = "levels/map_level3.txt"
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_three_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            util.clear_screen()
            ui.display_board(engine.create_board("messages/restart_screen.txt"))
            key = util.key_pressed()
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player["x"] = 1
        player["y"] = 1
    while player["level"] == 4 and player["HP"] > 0:
        util.clear_screen()
        player = engine.boss(player)
        if player["HP"] == 0:
            util.clear_screen()
            ui.display_board(engine.create_board("messages/restart_screen.txt"))
            key = util.key_pressed()
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 100
    return player


if __name__ == "__main__":
    while True:
        util.clear_screen()
        start_screen.main() #utworzyć plik start_screen i poprzeklejać funkcje
        util.clear_screen()
        player = main()
        util.clear_screen()
        t_end = time.time() + 5
        if player["level"] == 5:
            ui.display_board(engine.create_board("messages/winner.txt"))
            time.sleep(5)
        if player["level"] != 5:
            ui.display_board(engine.create_board("messages/loser.txt"))
            time.sleep(5)
