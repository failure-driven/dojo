DIRECTIONS = ["N", "E", "S", "W"]


def rover(position_commands):
    direction = position_commands["direction"]
    for command in position_commands["commands"]:
        direction = apply(direction, command)
    return {"x": 0, "y": 0, "direction": direction}


def apply(direction, command):
    dir_index = DIRECTIONS.index(direction)
    offset = +1 if command == "r" else -1
    new_dir_index = (dir_index + offset) % len(DIRECTIONS)
    return DIRECTIONS[new_dir_index]
