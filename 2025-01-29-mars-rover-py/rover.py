

def rover(position_commands):
    y = position_commands["y"]
    x = position_commands["x"]
    direction = position_commands["direction"]
    for command in position_commands['commands']:
        if command == 'f':
            x += 1
    return {"x": x, "y": y, "direction": direction}
