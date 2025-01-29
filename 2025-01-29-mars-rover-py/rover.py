

VECTOR_MOVEMENTS = {
    ("f", "N"): (1, 0),
    ("f", "E"): (0, 1),
    ("f", "S"): (-1, 0),
    ("f", "W"): (0, -1),
    ("b", "N"): (-1, 0),
    ("b", "E"): (0, -1),
    ("b", "S"): (1, 0),
    ("b", "W"): (0, 1),
}


def rover(position_commands):
    y = position_commands["y"]
    x = position_commands["x"]
    direction = position_commands["direction"]
    for command in position_commands['commands']:
        x += VECTOR_MOVEMENTS[(command, direction)][0]
        y += VECTOR_MOVEMENTS[(command, direction)][1]
    return {"x": x, "y": y, "direction": direction}
