"use client";

import React, { useState, useCallback } from 'react';
import RobotInput from './RobotInput';
import RobotTimeline from './RobotTimeline';
import RobotMap from './RobotMap';
import Rover from '../lib/Rover';

interface RobotCommandData {
  coordinates: {
    x: number;
    y: number;
    direction: 'N' | 'E' | 'S' | 'W';
  };
  commands: ('L' | 'R' | 'M')[];
}

interface RobotState {
  x: number;
  y: number;
  direction: 'N' | 'E' | 'S' | 'W';
}

const RobotController: React.FC = () => {
  const [initialState, setInitialState] = useState<RobotState>({
    x: 0,
    y: 0,
    direction: 'N'
  });
  const [commands, setCommands] = useState<string[]>([]);
  const [currentRobotState, setCurrentRobotState] = useState<RobotState>({
    x: 0,
    y: 0,
    direction: 'N'
  });
  const [hasLoadedCommands, setHasLoadedCommands] = useState(false);

  // Handle input from RobotInput component
  const handleCommandInput = useCallback((data: RobotCommandData) => {
    const newInitialState = {
      x: data.coordinates.x,
      y: data.coordinates.y,
      direction: data.coordinates.direction
    };

    setInitialState(newInitialState);
    setCurrentRobotState(newInitialState);
    setCommands(data.commands);
    setHasLoadedCommands(true);
  }, []);

  // Handle state changes from RobotTimeline
  const handleTimelineStateChange = useCallback((state: RobotState, stepIndex: number) => {
    // Use Rover to calculate the exact state at this step
    const commandsUpToStep = commands.slice(0, stepIndex);
    const calculatedState = Rover({
      coordinates: {
        x: initialState.x,
        y: initialState.y,
        direction: initialState.direction
      },
      commands: commandsUpToStep as ("L" | "R" | "M")[]
    });

    setCurrentRobotState({
      x: calculatedState.x,
      y: calculatedState.y,
      direction: calculatedState.direction as 'N' | 'E' | 'S' | 'W'
    });
  }, [commands, initialState]);

  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl font-bold text-center mb-8">Robot Controller</h1>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          {/* Input Section */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <RobotInput onSubmit={handleCommandInput} />
          </div>

          {/* Map Section */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <RobotMap robot={currentRobotState} />
          </div>
        </div>

        {/* Timeline Section - Only show after commands are loaded */}
        {hasLoadedCommands && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <RobotTimeline
              commands={commands}
              initialState={initialState}
              onStateChange={handleTimelineStateChange}
            />
          </div>
        )}

        {/* Status Section */}
        <div className="mt-8 bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-bold mb-4">Current Status</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-blue-50 p-4 rounded-lg">
              <h3 className="font-semibold text-blue-800 mb-2">Position</h3>
              <p className="text-2xl font-mono text-blue-600">
                ({currentRobotState.x}, {currentRobotState.y})
              </p>
            </div>
            <div className="bg-green-50 p-4 rounded-lg">
              <h3 className="font-semibold text-green-800 mb-2">Direction</h3>
              <p className="text-2xl font-mono text-green-600">
                {currentRobotState.direction}
              </p>
            </div>
            <div className="bg-purple-50 p-4 rounded-lg">
              <h3 className="font-semibold text-purple-800 mb-2">Commands Loaded</h3>
              <p className="text-2xl font-mono text-purple-600">
                {commands.length}
              </p>
            </div>
          </div>

          {commands.length > 0 && (
            <div className="mt-4 bg-gray-50 p-4 rounded-lg">
              <h3 className="font-semibold text-gray-800 mb-2">Commands Sequence</h3>
              <p className="font-mono text-gray-600">
                [{commands.map(cmd => `"${cmd}"`).join(', ')}]
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default RobotController;