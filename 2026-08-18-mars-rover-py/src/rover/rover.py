TURN_LIST = ["N", "E", "S", "W"]


def rover(position_commands):

    for command in position_commands["commands"]:
        offset = 1 if command == "R" else -1
        curr_direction_index = TURN_LIST.index(position_commands["direction"])
        new_index = (curr_direction_index + offset) % len(TURN_LIST)
        position_commands["direction"] = TURN_LIST[new_index]

    return {"x": 0, "y": 0, "direction": position_commands["direction"]}
