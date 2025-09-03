
DIRECTIONS = [
    "N",
    "E",
    "S",
    "W",
]
def rover(position_commands):
    x = position_commands["x"]
    y = position_commands["y"]
    direction = position_commands["direction"]
    index = DIRECTIONS.index(direction)
    for command in position_commands['commands']:
        index += 1
    direction = DIRECTIONS[index]
    return {"x": x, "y": y, "direction": direction}
