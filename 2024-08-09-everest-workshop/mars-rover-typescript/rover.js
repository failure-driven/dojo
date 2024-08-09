const RULES = {
  Sf: +1,
  Sb: -1,
  Nf: -1,
  Nb: +1,
};
const DIRECTIONS = ["N", "S"];

function rover({ location, grid, commands }) {
  commands.forEach((command) => {
    if (command == "f" || command == "b")
      move(location, grid, RULES[`${location.direction}${command}`]);
    if (command == "l") location.direction = "N";
  });
  return location;
}

function move(location, grid, amount) {
  location.y += amount;
  if (location.y < 0) {
    location.y = grid.col - 1;
  }
  location.y = location.y % grid.col;
}

module.exports = rover;
