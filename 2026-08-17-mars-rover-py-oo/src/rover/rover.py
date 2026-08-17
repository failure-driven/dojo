from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0
    direction: str = "N"


class Rover:
    VECTOR = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }
    RIGHT_OF = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N",
    }
    LEFT_OF = {v: k for k, v in RIGHT_OF.items()}
    COMMANDS = {
        "l": "apply_turn",
        "r": "apply_turn",
        "f": "apply_move",
        "b": "apply_move",
    }

    def __init__(self, position: Position | None = None):
        self.position = position or Position()

    def move(self, commands):
        for command in commands:
            method = getattr(self, self.COMMANDS[command])
            method(command)

    def location(self) -> Position:
        return self.position

    def apply_turn(self, command):
        turns = self.RIGHT_OF if command == "r" else self.LEFT_OF
        self.position.direction = turns[self.position.direction]

    def apply_move(self, command):
        offset = 1 if command == "f" else -1
        dx, dy = self.VECTOR[self.position.direction]
        self.position.x += dx * offset
        self.position.y += dy * offset
