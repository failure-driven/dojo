import json
import sys
from rover.rover import rover


def main():
    position_commands = json.loads(sys.argv[1])
    print(rover(position_commands))


if __name__ == "__main__":
    main()
