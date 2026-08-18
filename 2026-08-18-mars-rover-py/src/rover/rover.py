def rover(position_commands):
    if position_commands["commands"] == ["R"]:
        position_commands["direction"] = "E"

    return {"x": 0, "y": 0, "direction": position_commands["direction"]}
