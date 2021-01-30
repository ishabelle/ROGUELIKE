def create_ikea_construction_worker(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\U0001F477"
    enemy["type"] = "enemies"
    enemy["direction"] = "up"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy

def create_ikea_information_worker(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\U0001F481"
    enemy["type"] = "enemies"
    enemy["direction"] = "down"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_bodyguard(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\U0001f46e"
    enemy["type"] = "enemies"
    enemy["direction"] = "left"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy


def create_ikea_detective(x_position, y_position):
    enemy = {}
    enemy["x"] = x_position
    enemy["y"] = y_position
    enemy["icon"] = "\U0001f575"
    enemy["type"] = "enemies"
    enemy["direction"] = "right"
    enemy["attack"] = 10
    enemy["HP"] = 20
    return enemy