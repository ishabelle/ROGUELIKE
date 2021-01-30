def create_ikea_construction_worker(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "enemies"
    enemy["direction"] = "up"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_information_worker(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "enemies"
    enemy["direction"] = "down"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_bodyguard(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "enemies"
    enemy["direction"] = "left"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_detective(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\033[1;31;1m&\033[1;37;1m"
    enemy["type"] = "enemies"
    enemy["direction"] = "right"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_enemies_list(file_name):
    # sprawdzić indeksy na planszach , czy mieszczą się na mapach txt (wpisałam randomowe wartości)
    if file_name == "levels/map_level1.txt":
        X_INDEX = 0
        Y_INDEX =1
        ikea_contruction_worker_coordinates = [(15, 13)]
        ikea_information_worker_coordinates = [(20, 30)]
        ikea_bodyguard_coordinates = [(45, 30)]
        ikea_detective_coordinates = [(10, 25)]
        ikea_contruction_worker_enemy = [create_ikea_construction_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_contruction_worker_coordinates]
        ikea_information_worker_enemy = [create_ikea_information_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_information_worker_coordinates]
        ikea_bodyguard_enemy = [create_ikea_bodyguard(element[X_INDEX], element[Y_INDEX]) for element in ikea_bodyguard_coordinates]
        ikea_detective_enemy = [create_ikea_detective(element[X_INDEX], element[Y_INDEX]) for element in ikea_detective_coordinates]
        enemies_list = ikea_contruction_worker_enemy + ikea_information_worker_enemy + ikea_bodyguard_enemy + ikea_detective_enemy
    
    elif file_name == "levels/map_level2.txt":
        X_INDEX = 0
        Y_INDEX =1
        ikea_contruction_worker_coordinates = [(12, 19)]
        ikea_information_worker_coordinates = [(34, 10)]
        ikea_bodyguard_coordinates = [(43, 32)]
        ikea_detective_coordinates = [(9, 5)]
        ikea_contruction_worker_enemy = [create_ikea_construction_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_contruction_worker_coordinates]
        ikea_information_worker_enemy = [create_ikea_information_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_information_worker_coordinates]
        ikea_bodyguard_enemy = [create_ikea_bodyguard(element[X_INDEX], element[Y_INDEX]) for element in ikea_bodyguard_coordinates]
        ikea_detective_enemy = [create_ikea_detective(element[X_INDEX], element[Y_INDEX]) for element in ikea_detective_coordinates]
        enemies_list = ikea_contruction_worker_enemy + ikea_information_worker_enemy + ikea_bodyguard_enemy + ikea_detective_enemy
        
    elif file_name == "levels/map_level3.txt":
        X_INDEX = 0
        Y_INDEX =1
        ikea_contruction_worker_coordinates = [(3, 9)]
        ikea_information_worker_coordinates = [(12, 33)]
        ikea_bodyguard_coordinates = [(21, 10)]
        ikea_detective_coordinates = [(5, 3)]
        ikea_contruction_worker_enemy = [create_ikea_construction_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_contruction_worker_coordinates]
        ikea_information_worker_enemy = [create_ikea_information_worker(element[X_INDEX], element[Y_INDEX]) for element in ikea_information_worker_coordinates]
        ikea_bodyguard_enemy = [create_ikea_bodyguard(element[X_INDEX], element[Y_INDEX]) for element in ikea_bodyguard_coordinates]
        ikea_detective_enemy = [create_ikea_detective(element[X_INDEX], element[Y_INDEX]) for element in ikea_detective_coordinates]
        enemies_list = ikea_contruction_worker_enemy + ikea_information_worker_enemy + ikea_bodyguard_enemy + ikea_detective_enemy
    
    return enemies_list