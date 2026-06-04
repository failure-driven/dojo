def rover(position_commands):
    y = position_commands["y"]
    x = position_commands["x"]
    direction = position_commands["direction"]
    if len(position_commands["commands"]) > 0:
        y += 1

    return {
         'x': x,
         'y': y,
         'direction': direction,
     }
