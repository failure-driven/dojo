DIRECTIONS = ["N", "E", "S", "W"]
DIRECTION_OFFSET = {
        "r": 1,
        "l": -1
        }
MOVE = {
        "N": {"x": 0, "y": 1},
        "E": {"x": 1, "y": 0},
        "S": {"x": 0, "y": -1},
        "W": {"x": -1, "y": 0},
        }
MOVE_DIRECTION = {
        "f": 1,
        "b": -1
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
    if command in ["f", "b"]:
        apply_move(position_commands, command)


def apply_turn(position_commands, command):
    position_commands.update({
        "direction": new_direction(position_commands["direction"], command)
    })
    return position_commands


def new_direction(direction, command):
    current_index = DIRECTIONS.index(direction)
    new_index = (current_index + DIRECTION_OFFSET[command]) % len(DIRECTIONS)
    return DIRECTIONS[new_index]


def apply_move(position_commands, command):
    position_commands.update({
        "x": position_commands["x"] +
        MOVE_DIRECTION[command] *
        MOVE[position_commands["direction"]]["x"],
        "y": position_commands["y"] +
        MOVE_DIRECTION[command] *
        MOVE[position_commands["direction"]]["y"]
    })
    return position_commands
