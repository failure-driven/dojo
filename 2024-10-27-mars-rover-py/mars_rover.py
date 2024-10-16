class MarsRover:
    DIRECTIONS = ["N", "E", "S", "W"]
    MOVES = {
            "N": {"x": 0, "y": 1},
            "E": {"x": 1, "y": 0},
            "S": {"x": 0, "y": -1},
            "W": {"x": -1, "y": 0},
            }

    def __init__(self, start_parameters):
        self.start_parameters = start_parameters
        self.x = start_parameters["x"]
        self.y = start_parameters["y"]
        self.direction = start_parameters["direction"]

        for command in start_parameters["commands"]:
            self.apply(command)

    def position(self):
        return {
                "x": self.x,
                "y": self.y,
                "direction": self.direction,
                }

    def apply(self, command):
        if command in ["r", "l"]:
            self.apply_rotation(command)
        if command in ["f", "b"]:
            self.apply_move(command)

    def apply_move(self, command):
        move = self.MOVES[self.direction]
        direction = 1 if command == "f" else -1
        self.x += move["x"] * direction
        self.y += move["y"] * direction

    def apply_rotation(self, command):
        direction = 1 if command == "r" else -1
        index = self.DIRECTIONS.index(self.direction)
        index = (index + direction) % len(self.DIRECTIONS)
        self.direction = self.DIRECTIONS[index]
