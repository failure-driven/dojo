"use client";

import React, { useState, useEffect, useCallback } from "react";

interface RobotState {
  x: number;
  y: number;
  direction: "N" | "E" | "S" | "W";
}

interface RobotTimelineProps {
  commands?: string[];
  initialState?: RobotState;
  onStateChange?: (state: RobotState, stepIndex: number) => void;
}

type Speed = "slow" | "medium" | "fast";

const speedSettings = {
  slow: 2000,
  medium: 1000,
  fast: 500,
};

const RobotTimeline: React.FC<RobotTimelineProps> = ({
  commands = [],
  initialState = { x: 0, y: 0, direction: "N" },
  onStateChange,
}) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speed, setSpeed] = useState<Speed>("medium");
  const [robotStates, setRobotStates] = useState<RobotState[]>([]);

  // Calculate all robot states based on commands
  const calculateStates = useCallback(() => {
    const states: RobotState[] = [initialState];
    let currentState = { ...initialState };

    commands.forEach((command) => {
      switch (command.toUpperCase()) {
        case "L":
          currentState = {
            ...currentState,
            direction: turnLeft(currentState.direction),
          };
          break;
        case "R":
          currentState = {
            ...currentState,
            direction: turnRight(currentState.direction),
          };
          break;
        case "M":
          currentState = moveForward(currentState);
          break;
      }
      states.push({ ...currentState });
    });

    return states;
  }, [commands, initialState]);

  const turnLeft = (
    direction: "N" | "E" | "S" | "W"
  ): "N" | "E" | "S" | "W" => {
    const directions = ["N", "E", "S", "W"] as const;
    const currentIndex = directions.indexOf(direction);
    return directions[(currentIndex + 3) % 4];
  };

  const turnRight = (
    direction: "N" | "E" | "S" | "W"
  ): "N" | "E" | "S" | "W" => {
    const directions = ["N", "E", "S", "W"] as const;
    const currentIndex = directions.indexOf(direction);
    return directions[(currentIndex + 1) % 4];
  };

  const moveForward = (state: RobotState): RobotState => {
    switch (state.direction) {
      case "N":
        return { ...state, y: state.y + 1 };
      case "E":
        return { ...state, x: state.x + 1 };
      case "S":
        return { ...state, y: state.y - 1 };
      case "W":
        return { ...state, x: state.x - 1 };
      default:
        return state;
    }
  };

  // Initialize states when commands change
  useEffect(() => {
    const states = calculateStates();
    setRobotStates(states);
    setCurrentStep(0);
  }, [calculateStates]);

  // Notify parent of state changes
  useEffect(() => {
    if (robotStates.length > 0 && onStateChange) {
      onStateChange(robotStates[currentStep], currentStep);
    }
  }, [currentStep, robotStates, onStateChange]);

  // Auto-play functionality
  useEffect(() => {
    if (!isPlaying) return;

    const interval = setInterval(() => {
      setCurrentStep((prev) => {
        if (prev >= robotStates.length - 1) {
          setIsPlaying(false);
          return prev;
        }
        return prev + 1;
      });
    }, speedSettings[speed]);

    return () => clearInterval(interval);
  }, [isPlaying, speed, robotStates.length]);

  const handlePrevious = () => {
    setCurrentStep((prev) => Math.max(0, prev - 1));
  };

  const handleNext = () => {
    setCurrentStep((prev) => Math.min(robotStates.length - 1, prev + 1));
  };

  const handlePlay = () => {
    if (currentStep >= robotStates.length - 1) {
      setCurrentStep(0);
    }
    setIsPlaying(!isPlaying);
  };

  const handleStepClick = (stepIndex: number) => {
    setCurrentStep(stepIndex);
    setIsPlaying(false);
  };

  const currentState = robotStates[currentStep] || initialState;
  const currentCommand = currentStep > 0 ? commands[currentStep - 1] : null;

  return (
    <div className="w-full max-w-4xl mx-auto p-4 bg-white rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Robot Timeline</h2>

      {/* Current State Display */}
      <div className="mb-6 p-4 bg-gray-50 rounded-lg">
        <div className="flex justify-between items-center">
          <div>
            <span className="text-sm text-gray-600">Position:</span>
            <span className="ml-2 font-mono">
              ({currentState.x}, {currentState.y})
            </span>
          </div>
          <div>
            <span className="text-sm text-gray-600">Direction:</span>
            <span className="ml-2 font-mono">{currentState.direction}</span>
          </div>
          <div>
            <span className="text-sm text-gray-600">Step:</span>
            <span className="ml-2 font-mono">
              {currentStep} / {Math.max(0, robotStates.length - 1)}
            </span>
          </div>
        </div>
        {currentCommand && (
          <div className="mt-2">
            <span className="text-sm text-gray-600">Current Command:</span>
            <span className="ml-2 px-2 py-1 bg-blue-100 text-blue-800 rounded font-mono">
              {currentCommand}
            </span>
          </div>
        )}
      </div>

      {/* Controls */}
      <div className="mb-6 flex items-center justify-center space-x-4">
        <button
          onClick={handlePrevious}
          disabled={currentStep === 0}
          className="px-3 py-2 bg-gray-200 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
        >
          ◀️
        </button>

        <button
          onClick={handlePlay}
          className="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg transition-colors flex items-center space-x-2"
        >
          <span>{isPlaying ? "⏸️" : "▶️"}</span>
          <span>{isPlaying ? "Pause" : "Play"}</span>
        </button>

        <button
          onClick={handleNext}
          disabled={currentStep >= robotStates.length - 1}
          className="px-3 py-2 bg-gray-200 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed rounded-lg transition-colors"
        >
          ▶️
        </button>
      </div>

      {/* Speed Control */}
      <div className="mb-6 flex items-center justify-center space-x-4">
        <span className="text-sm text-gray-600">Speed:</span>
        {(["slow", "medium", "fast"] as const).map((speedOption) => (
          <button
            key={speedOption}
            onClick={() => setSpeed(speedOption)}
            className={`px-3 py-1 rounded-lg text-sm transition-colors ${
              speed === speedOption
                ? "bg-blue-500 text-white"
                : "bg-gray-200 hover:bg-gray-300 text-gray-700"
            }`}
          >
            {speedOption.charAt(0).toUpperCase() + speedOption.slice(1)}
          </button>
        ))}
      </div>

      {/* Timeline Visualization */}
      {commands.length > 0 && (
        <div className="mb-4">
          <h3 className="text-lg font-semibold mb-2">Command Timeline</h3>
          <div className="flex items-center space-x-2 overflow-x-auto pb-2">
            {/* Initial state */}
            <div
              onClick={() => handleStepClick(0)}
              className={`min-w-[60px] h-12 flex items-center justify-center rounded-lg cursor-pointer transition-colors ${
                currentStep === 0
                  ? "bg-green-500 text-white"
                  : "bg-gray-200 hover:bg-gray-300"
              }`}
            >
              <span className="text-xs">Start</span>
            </div>

            {commands.map((command, index) => (
              <React.Fragment key={index}>
                <div className="flex-shrink-0 w-4 h-0.5 bg-gray-300"></div>
                <div
                  onClick={() => handleStepClick(index + 1)}
                  className={`min-w-[60px] h-12 flex flex-col items-center justify-center rounded-lg cursor-pointer transition-colors ${
                    currentStep === index + 1
                      ? "bg-blue-500 text-white"
                      : "bg-gray-200 hover:bg-gray-300"
                  }`}
                >
                  <span className="font-mono text-sm">{command}</span>
                  <span className="text-xs">{index + 1}</span>
                </div>
              </React.Fragment>
            ))}
          </div>
        </div>
      )}

      {commands.length === 0 && (
        <div className="text-center text-gray-500 py-8">
          No commands to display. Add some commands to see the timeline.
        </div>
      )}
    </div>
  );
};

export default RobotTimeline;
