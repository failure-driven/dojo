/**
 * Generate input form
 * @param {element} world
 * @param {json} initialInstruct
 */
const generateInput = (world, initialInstruct) => {
  const form = document.createElement("form");
  form.setAttribute("class", "form");
  form.setAttribute("onSubmit", "runSimulation(event)");
  const input = document.createElement("textarea");
  input.setAttribute("rows", "10");
  input.setAttribute("class", "input");
  input.value = JSON.stringify(initialInstruct, null, 2);
  const submit = document.createElement("input");
  submit.setAttribute("value", "run simulation");
  submit.setAttribute("type", "submit");
  submit.classList.add("submit");
  form.appendChild(input);
  form.appendChild(submit);
  world.appendChild(form);
};

/**
 * generate grid
 * @param {element} world
 * @param {number} size
 */
const generateGrid = (world, size) => {
  const grid = document.createElement("div");
  grid.setAttribute("class", "grid");
  const offset = parseInt(size / 2); // 5
  [...Array(size).keys()].map((row) => {
    [...Array(size).keys()].map((col) => {
      const cell = document.createElement("div");
      cell.setAttribute("class", "cell");
      const cellInternals = document.createElement("div");
      cellInternals.setAttribute("class", "cell-internals");
      const x = col - offset;
      const y = size - row - 1 - offset;
      cell.dataset.coordinate = JSON.stringify([x, y]);
      const coordText = document.createElement("div");
      coordText.setAttribute("class", "coord-text");
      coordText.appendChild(document.createTextNode(`${x}, ${y}`));
      cellInternals.appendChild(coordText);
      cell.appendChild(cellInternals);
      grid.appendChild(cell);
    });
    const rowBreak = document.createElement("br");
    grid.appendChild(rowBreak);
  });
  world.appendChild(grid);
};

  const directionClasses = {
    N: "north",
    E: "east",
    S: "south",
    W: "west",
  };
/**
 * Append a rover
 *
 * @param {element} world
 */
const appendRover = (x, y, direction) => {
  const north = document.createElement("div");
  north.setAttribute("class", "direction-pointer north");
  const east = document.createElement("div");
  east.setAttribute("class", "direction-pointer east");
  const south = document.createElement("div");
  south.setAttribute("class", "direction-pointer south");
  const west = document.createElement("div");
  west.setAttribute("class", "direction-pointer west");
  const rover = document.createElement("div");
  rover.setAttribute("class", "rover");
  rover.appendChild(north);
  rover.appendChild(east);
  rover.appendChild(south);
  rover.appendChild(west);
  const currentCell = document.querySelector(
    `.grid .cell[data-coordinate="[${x},${y}]"] .cell-internals`
  );
  currentCell.appendChild(rover);
  const currentDirection = currentCell.querySelector(
    `.${directionClasses[direction]}`
  );
  currentDirection.classList.add("active");
};

/**
 * Append styling
 * @param {element} world
 */
const appendStyle = (world) => {
  const style = document.createElement("style");
  style.appendChild(
    document.createTextNode(`
.form {
    display: block;
    max-width: 360px;
}
.input {
    display: block;
    width: 100%;
    max-width: 100%;
}
.submit {
    display: block;
    width: 100%;
    max-width: 100%;
    text-align: center;
    margin: 5px 0;
}
.grid {
    padding-top: 10px;
    width: ${(size + 1) * 40}px;
}
.cell {
    display: inline-block;
    width: 40px;
    height: 40px;
    margin-left: -1px;
    margin-top: -5px;
    border: 1px black solid;
}
.cell-internals {
    position: absolute;
}
.coord-text {
    position: absolute;
    width: 40px;
    top: 10px;
    left: 5px;
    color: #dddddd;
}
.cell:hover .coord-text {
    color: #555555;
}
.rover {
    position: absolute;
    top: 0px;
    .direction-pointer {
        position: absolute;
        opacity: 0.3;
    }
    .direction-pointer.active {
        position: absolute;
        opacity: 1;
    }
    .north {
        top: -5px;
        left: 12px;
    }
    .east {
        top: 10px;
        left: 27px;
    }
    .south {
        top: 24px;
        left: 12px;
    }
    .west {
        top: 8px;
        left: -2px;
    }
    .north::after {
        content: "\\25B2"; // ▲
    }
    .east::after {
        content: "\\25B6"; // ▶
    }
    .south::after {
        content: "\\25BC"; // ▼
    }
    .west::after {
        content: "\\25C0"; // ◀
    }
}
`)
  );
  world.appendChild(style);
};

/**
 * perform a single command on the backend server port 5000
 *
 * @param {json} instructions
 * @param {number} index
 * @param {element} rover
 */
const performCommand = (instructions, index, rover) => {
  const wait = 300;
  fetch("http://127.0.0.1:5000/", {
    method: "post",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      x: instructions.x,
      y: instructions.y,
      direction: instructions.direction,
      commands: [instructions.commands[index]],
    }),
  })
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
      instructions.x = json.x;
      instructions.y = json.y;
      instructions.direction = json.direction;
    });
  if (index < instructions.commands.length) {
    setTimeout(() => performCommand(instructions, index + 1, rover), wait);
  }
  const currentCell = document.querySelector(
    `.grid .cell[data-coordinate="[${instructions.x},${instructions.y}]"] .cell-internals`
  );
  currentCell.appendChild(rover);
  currentCell
    .querySelectorAll(".direction-pointer")
    .forEach((element) => element.classList.remove("active"));
  const currentDirection = currentCell.querySelector(
    `.${directionClasses[instructions.direction]}`
  );
  currentDirection.classList.add("active");
};

/**
 * Run simulation from form
 *
 * @param {event} event
 * @returns
 */
function runSimulation(event) {
  event.preventDefault();
  const instructions = JSON.parse(document.querySelector(".input").value);
  const rover = document.querySelector(".rover");
  performCommand(instructions, 0, rover);
  return false;
}

/**
 * Main program setup
 */
const initialInstruct = {
  x: 0,
  y: 0,
  direction: "N",
  commands: ["r", "f", "l", "b"],
};
const world = document.getElementById("world");
generateInput(world, initialInstruct);
const size = 11;
generateGrid(world, size);
appendRover(initialInstruct.x, initialInstruct.y, initialInstruct.direction);
appendStyle(world);
