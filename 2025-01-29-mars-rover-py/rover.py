

def rover(position_commands):
    y = position_commands["y"]
    x = position_commands["x"]
    direction = position_commands["direction"]
    if position_commands['commands'] == ['f']:
        x += 1
    return {"x": x, "y": y, "direction": direction}
