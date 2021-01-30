def create_baby_angel_head(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mB\033[1;37;1m"
    item["type"] = "inventory"
    item["HP"] = 5
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_shopping_bags(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mS\033[1;37;1m"
    item["type"] = "weapons"
    item["HP"] = 5
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_shopping_trolley(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mT\033[1;37;1m"
    item["type"] = "weapons"
    item["HP"] = 15
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_pencil(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mP\033[1;37;1m"
    item["type"] = "key"
    item["HP"] = 10
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_frying_pan(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mF\033[1;37;1m"
    item["type"] = "weapons"
    item["HP"] = 20
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_knife(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mK\033[1;37;1m"
    item["type"] = "weapons"
    item["HP"] = 15
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_broccoli(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mL\033[1;37;1m"
    item["type"] = "weapons"
    item["HP"] = 10
    item["on_board"] = 1
    item["weight"] = 5
    return item


def create_hot_dog(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mH\033[1;37;1m"
    item["type"] = "food"
    item["HP"] = 15
    item["on_board"] = 1
    item["weight"] = 5
    return item   


def create_meat_balls(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mM\033[1;37;1m"
    item["type"] = "food"
    item["HP"] = 20
    item["on_board"] = 1
    item["weight"] = 5
    return item 


def create_ice_cream(x_position, y_position):
    item = {}
    item["x"] = x_position
    item["y"] = y_position
    item["icon"] = "\033[1;32;1mC\033[1;37;1m"
    item["type"] = "food"
    item["HP"] = 25
    item["on_board"] = 1
    item["weight"] = 5
    return item 