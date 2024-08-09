"use strict";

const rover = require("./rover");

describe("Rover", () => {
  it("it retruns with current conditions as same as initiall if no commands were run", () => {
    expect(
      rover({
        location: { x: 0, y: 2, direction: "N" },
        grid: { col: 5 },
        commands: [],
      })
    ).toEqual({ x: 0, y: 2, direction: "N" });
  });
  it("on a grid of 5 taking 4 steps should take you to the edge", () => {
    expect(
      rover({
        location: { x: 0, y: 0, direction: "S" },
        grid: { col: 5 },
        commands: ["f", "f", "f", "f"],
      })
    ).toEqual({ x: 0, y: 4, direction: "S" });
  });
  it("on a grid of 5, 5 steps should take you back to the start", () => {
    expect(
      rover({
        location: { x: 0, y: 0, direction: "S" },
        grid: { col: 5 },
        commands: ["f", "f", "f", "f", "f"],
      })
    ).toEqual({ x: 0, y: 0, direction: "S" });
  });
  it("on a grid of 5, 4 steps backwards takes you to edge", () => {
    expect(
      rover({
        location: { x: 0, y: 0, direction: "S" },
        grid: { col: 5 },
        commands: ["f", "b", "b", "b", "b"],
      })
    ).toEqual({ x: 0, y: 2, direction: "S" });
  });
  it("on a grid of 5, taking a direction North, 3 steps forward and 1 step backwards", () => {
    expect(
      rover({
        location: { x: 0, y: 0, direction: "N" },
        grid: { col: 5 },
        commands: ["f", "f", "f", "b"],
      })
    ).toEqual({ x: 0, y: 3, direction: "N" });
  });
  it("south 2 turn left in 1D world and 2 forward puts us at 0,0N", () => {
    expect(
      rover({
        location: { x: 0, y: 0, direction: "S" },
        grid: { col: 5 },
        commands: ["f", "f", "l", "f", "f"],
      })
    ).toEqual({ x: 0, y: 0, direction: "N" });
  });
});
