
import React from "react";

type Direction = "N" | "E" | "S" | "W";

const GRID_SIZE = 10;
const ROBOT_EMOJI = "🤖";

// Direction arrow mapping
const directionArrows: Record<Direction, string> = {
  N: "↑",
  E: "→",
  S: "↓",
  W: "←",
};

interface Robot {
  x: number;
  y: number;
  direction: Direction;
}

interface RobotMapProps {
  robot?: Robot;
}

const RobotMap: React.FC<RobotMapProps> = ({
  robot = { x: 0, y: 0, direction: "N" }
}) => {
  // Center (0,0) in the grid
  const centerX = Math.floor(GRID_SIZE / 2);
  const centerY = Math.floor(GRID_SIZE / 2);
  const robotX = centerX + robot.x;
  const robotY = centerY - robot.y;

  return (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <div className="mb-4 text-xl font-bold">Robot Map</div>
      <div className="grid grid-cols-10 gap-1 bg-gray-100 p-4 rounded-lg shadow-lg">
        {[...Array(GRID_SIZE * GRID_SIZE)].map((_, idx) => {
          const x = idx % GRID_SIZE;
          const y = Math.floor(idx / GRID_SIZE);
          const isRobot = x === robotX && y === robotY;
          return (
            <div
              key={idx}
              className={`w-8 h-8 flex items-center justify-center border border-gray-300 rounded-md bg-white text-lg transition-all duration-200
                ${isRobot ? "bg-blue-200 font-bold shadow-md" : ""}
              `}
            >
              {isRobot ? (
                <span className="flex flex-col items-center">
                  <span>{ROBOT_EMOJI}</span>
                  <span className="text-xs">{directionArrows[robot.direction]}</span>
                </span>
              ) : null}
            </div>
          );
        })}
      </div>
      <div className="mt-4 text-gray-600">Position: ({robot.x}, {robot.y}) &nbsp; Direction: {robot.direction}</div>
    </div>
  );
};

export default RobotMap;
