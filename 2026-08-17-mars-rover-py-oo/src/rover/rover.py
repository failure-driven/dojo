class Rover:
    DIRECTIONS = ["N", "E", "S", "W"]
    VECTOR = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]

    def __init__(self, position=None):
        self.position = position or {"x": 0, "y": 0, "direction": "N"}

    def move(self, commands):
        for command in commands:
            if command in ["l", "r"]:
                self.apply_turn(command)
            if command in ["f", "b"]:
                self.apply_move(command)

    def location(self):
        return self.position

    def apply_turn(self, command):
        offset = 1 if command == "r" else -1
        new_direction = (self.dir_index() + offset) % len(self.DIRECTIONS)
        self.position["direction"] = self.DIRECTIONS[new_direction]

    def apply_move(self, command):
        offset = 1 if command == "f" else -1
        self.position["x"] += self.VECTOR[self.dir_index()][0] * offset
        self.position["y"] += self.VECTOR[self.dir_index()][1] * offset

    def dir_index(self):
        return self.DIRECTIONS.index(self.position["direction"])
