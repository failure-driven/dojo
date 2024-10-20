DIRECTIONS = ["N", "E", "S", "W"]
DIRECTION_OFFSET = {
        "r": 1,
        "l": -1
        }


def rover(position_commands):
    for command in position_commands["commands"]:
        apply_command(position_commands, command)
    return {
            "x": position_commands["x"],
            "y": position_commands["y"],
            "direction": position_commands["direction"]}


def apply_command(position_commands, command):
    if command in ["l", "r"]:
        apply_turn(position_commands, command)


def apply_turn(position_commands, command):
    position_commands.update({
        "direction": new_direction(position_commands["direction"], command)
    })
    return position_commands


def new_direction(direction, command):
    current_index = DIRECTIONS.index(direction)
    new_index = (current_index + DIRECTION_OFFSET[command]) % len(DIRECTIONS)
    return DIRECTIONS[new_index]
