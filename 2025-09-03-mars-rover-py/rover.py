def rover(position_commands):
    x = position_commands["x"]
    if position_commands["commands"] == ["r"]:
        return {"x": x, "y": 0, "direction": "E"}
    return {"x": x, "y": 0, "direction": "N"}