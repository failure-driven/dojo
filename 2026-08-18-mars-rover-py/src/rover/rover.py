def rover(position_commands):
    if position_commands["commands"] == ["R"]:
        right_turn_list = ["N", "E", "S", "W"]
        current_direction_index = right_turn_list.index(position_commands["direction"])
        new_index = (current_direction_index + 1) % len(right_turn_list)
        position_commands["direction"] = right_turn_list[new_index]

    return {"x": 0, "y": 0, "direction": position_commands["direction"]}
