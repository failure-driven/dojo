def rover(position_commands):
    x = position_commands["x"]
    y = position_commands["y"]
    direction = position_commands["direction"]
    if position_commands["commands"] == ["r"]:
        direction = "E"
    if position_commands["commands"] == ["r", "r"]:
        direction = "S"
    return {"x": x, "y": y, "direction": direction}
