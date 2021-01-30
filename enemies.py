def create_ikea_worker(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "x_move"
    enemy["direction"] = "right"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_client(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "y_move"
    enemy["direction"] = "up"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_enemies_list(file_name):
    # sprawdzić indeksy na planszach , czy mieszczą się na mapach txt (wpisałam randomowe wartości)
    if file_name == "levels/map_level1.txt":
        X_INDEX = 0
        Y_INDEX = 1
        ikea_worker_coordinates = [(11, 13)]
        ikea_client_coordinates = [(20, 4)]
        ikea_worker_enemy = [create_ikea_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_worker_coordinates]
        ikea_client_enemy = [create_ikea_client(element[X_INDEX], element[Y_INDEX]) for element in ikea_client_coordinates]
        enemies_list = ikea_worker_enemy + ikea_client_enemy
    
    elif file_name == "levels/map_level2.txt":
        X_INDEX = 0
        Y_INDEX = 1
        ikea_worker_coordinates = [(1, 4)]
        ikea_client_coordinates = [(5, 5)]
        ikea_worker_enemy = [create_ikea_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_worker_coordinates]
        ikea_client_enemy = [create_ikea_client(element[X_INDEX], element[Y_INDEX]) for element in ikea_client_coordinates]
        enemies_list = ikea_worker_enemy + ikea_client_enemy
        
    elif file_name == "levels/map_level3.txt":
        X_INDEX = 0
        Y_INDEX = 1
        ikea_worker_coordinates = [(33, 4)]
        ikea_client_coordinates = [(3, 10)]
        ikea_worker_enemy = [create_ikea_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_worker_coordinates]
        ikea_client_enemy = [create_ikea_client(element[X_INDEX], element[Y_INDEX]) for element in ikea_client_coordinates]
        enemies_list = ikea_worker_enemy + ikea_client_enemy
    
    return enemies_list