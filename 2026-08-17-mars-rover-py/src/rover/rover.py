DIRECTIONS = ["N", "E", "S", "W"]
VECTORS = {
    "N": [0, 1],
    "E": [1, 0],
    "S": [0, -1],
    "W": [-1, 0],
}


def rover(position_commands):
    x = position_commands["x"]
    y = position_commands["y"]
    direction = position_commands["direction"]
    for command in position_commands["commands"]:
        [x, y, direction] = apply(x, y, direction, command)
    return {"x": x, "y": y, "direction": direction}


def apply(x, y, direction, command):
    dir_index = DIRECTIONS.index(direction)
    if command == "r" or command == "l":
        offset = +1 if command == "r" else -1
        dir_index = (dir_index + offset) % len(DIRECTIONS)
    if command == "f" or command == "b":
        offset = 1 if command == "f" else -1
        x = x + VECTORS[direction][0] * offset
        y = y + VECTORS[direction][1] * offset
    return [x, y, DIRECTIONS[dir_index]]
