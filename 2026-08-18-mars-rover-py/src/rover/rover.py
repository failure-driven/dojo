TURN_LIST = ["N", "E", "S", "W"]

def rover(position_commands):

    if len(position_commands["commands"]) > 0:
        offset = 1 if position_commands["commands"] == ["R"] else -1
        current_direction_index = TURN_LIST.index(position_commands["direction"])
        new_index = (current_direction_index + offset) % len(TURN_LIST)
        position_commands["direction"] = TURN_LIST[new_index]

    return {"x": 0, "y": 0, "direction": position_commands["direction"]}
