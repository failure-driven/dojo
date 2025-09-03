
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
    if position_commands["commands"] == ["r"] and direction == DIRECTIONS[0]:
        direction = DIRECTIONS[1]

    if position_commands["commands"] == ["r"] and direction == DIRECTIONS[2]:
        direction = DIRECTIONS[3]

    if position_commands["commands"] == ["r", "r"] and direction == DIRECTIONS[0]:
        direction = DIRECTIONS[2]
    return {"x": x, "y": y, "direction": direction}
