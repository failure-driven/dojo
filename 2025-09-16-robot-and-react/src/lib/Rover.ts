type Coordinates = {
  x: number;
  y: number;
  direction: string;
};

type Command = "R";

const DIRECTIONS = ["N", "E", "S", "W"];

const Rover = ({
  coordinates,
  commands = [],
}: {
  coordinates: Coordinates;
  commands?: Command[];
}) => {
  const { x, y } = coordinates;
  let { direction } = coordinates;

  commands.forEach((command) => {
    if (command === "R") {
      const index = DIRECTIONS.findIndex((dir) => dir === direction);
      direction = DIRECTIONS[(index + 1) % DIRECTIONS.length];
    }
  });
  return { x, y, direction };
};

export default Rover;
