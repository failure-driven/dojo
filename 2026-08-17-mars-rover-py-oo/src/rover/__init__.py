import json
import sys
from rover.rover import Rover


def main():
    position_commands = json.loads(sys.argv[1])
    print("executing: ", position_commands)
    rover = Rover()
    rover = Rover({k: position_commands[k] for k in ("x", "y", "direction")})
    rover.move(position_commands["commands"])
    print(rover.location())


if __name__ == "__main__":
    main()
