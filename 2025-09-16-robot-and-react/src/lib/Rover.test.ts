import Rover from "./Rover";

describe("Rover", () => {
  it("returns it's current location", () => {
    expect(
      Rover({
        coordinates: { x: 0, y: 0, direction: "N" },
      })
    ).toEqual({ x: 0, y: 0, direction: "N" });
  });

  it("turns around 360 degrees", () => {
    let location = Rover({
      coordinates: { x: 0, y: 0, direction: "N" },
    });
    expect(location).toEqual({ x: 0, y: 0, direction: "N" });

    location = Rover({
      coordinates: location,
      commands: ["R"],
    });

    expect(location).toEqual({ x: 0, y: 0, direction: "E" });

    location = Rover({
      coordinates: location,
      commands: ["R"],
    });

    expect(location).toEqual({ x: 0, y: 0, direction: "S" });

    location = Rover({
      coordinates: location,
      commands: ["R"],
    });

    expect(location).toEqual({ x: 0, y: 0, direction: "W" });

    location = Rover({
      coordinates: location,
      commands: ["R"],
    });

    expect(location).toEqual({ x: 0, y: 0, direction: "N" });
  });

  it("turns around a bunch of times", () => {
    const location = Rover({
      coordinates: { x: 0, y: 0, direction: "N" },
      commands: [
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
        "R",
      ],
    });
    expect(location).toEqual({ x: 0, y: 0, direction: "S" });
  });
});
