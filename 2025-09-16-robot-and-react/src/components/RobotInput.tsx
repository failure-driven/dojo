"use client"
import React, { useState } from 'react';
import Editor from '@monaco-editor/react';

interface RobotCommandData {
  coordinates: {
    x: number;
    y: number;
    direction: 'N' | 'E' | 'S' | 'W';
  };
  commands: ('L' | 'R' | 'M')[];
}

interface RobotInputProps {
  onSubmit?: (data: RobotCommandData) => void;
}

const RobotInput: React.FC<RobotInputProps> = ({ onSubmit }) => {
  const [editorValue, setEditorValue] = useState<string>(() =>
    JSON.stringify(
      {
        coordinates: { x: 0, y: 0, direction: 'N' },
        commands: ['R', 'R']
      },
      null,
      2
    )
  );
  const [isValid, setIsValid] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  // JSON Schema for validation
  const jsonSchema = {
    type: 'object',
    properties: {
      coordinates: {
        type: 'object',
        properties: {
          x: { type: 'number' },
          y: { type: 'number' },
          direction: { type: 'string', enum: ['N', 'E', 'S', 'W'] }
        },
        required: ['x', 'y', 'direction']
      },
      commands: {
        type: 'array',
        items: { type: 'string', enum: ['L', 'R', 'M'] }
      }
    },
    required: ['coordinates', 'commands']
  };

  const validateJSON = (value: string) => {
    try {
      const parsed = JSON.parse(value);
      // Basic validation - could be enhanced with a proper JSON schema validator
      if (
        parsed.coordinates &&
        typeof parsed.coordinates.x === 'number' &&
        typeof parsed.coordinates.y === 'number' &&
        ['N', 'E', 'S', 'W'].includes(parsed.coordinates.direction) &&
        Array.isArray(parsed.commands) &&
        parsed.commands.every((cmd: string) => ['L', 'R', 'M'].includes(cmd))
      ) {
        setIsValid(true);
        setError('');
        return true;
      } else {
        setIsValid(false);
        setError('Invalid data structure. Please follow the schema.');
        return false;
      }
    } catch {
      setIsValid(false);
      setError('Invalid JSON format');
      return false;
    }
  };

  const handleEditorChange = (value: string | undefined) => {
    if (value !== undefined) {
      setEditorValue(value);
      validateJSON(value);
    }
  };

  const handleEditorDidMount = (editor: unknown, monaco: unknown) => {
    // Configure JSON schema validation
    const monacoInstance = monaco as {
      languages: {
        json: {
          jsonDefaults: {
            setDiagnosticsOptions: (options: { validate: boolean; schemas: Array<{ uri: string; fileMatch: string[]; schema: object }> }) => void
          }
        }
      }
    };

    monacoInstance.languages.json.jsonDefaults.setDiagnosticsOptions({
      validate: true,
      schemas: [{
        uri: 'http://myserver/robot-schema.json',
        fileMatch: ['*'],
        schema: jsonSchema
      }]
    });
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-4">
      <h2 className="text-xl font-bold mb-4">Robot Command Input</h2>
      <div className="mb-4">
        <div className="border rounded-lg overflow-hidden">
          <Editor
            height="300px"
            defaultLanguage="json"
            value={editorValue}
            onChange={handleEditorChange}
            onMount={handleEditorDidMount}
            options={{
              minimap: { enabled: false },
              lineNumbers: 'on',
              formatOnPaste: true,
              formatOnType: true,
              automaticLayout: true,
              scrollBeyondLastLine: false,
              wordWrap: 'on',
              theme: 'vs-light'
            }}
          />
        </div>
        {error && (
          <div className="mt-2 text-red-600 text-sm bg-red-50 border border-red-200 rounded p-2">
            {error}
          </div>
        )}
        {isValid && (
          <div className="mt-2 text-green-600 text-sm bg-green-50 border border-green-200 rounded p-2">
            Valid JSON structure ✓
          </div>
        )}
      </div>
      <button
        onClick={() => {
          if (validateJSON(editorValue) && onSubmit) {
            try {
              const parsed = JSON.parse(editorValue);
              onSubmit(parsed as RobotCommandData);
            } catch {
              setError('Failed to parse JSON');
            }
          }
        }}
        disabled={!isValid}
        className={`px-4 py-2 rounded font-medium transition-colors ${
          isValid
            ? 'bg-blue-500 text-white hover:bg-blue-600'
            : 'bg-gray-300 text-gray-500 cursor-not-allowed'
        }`}
      >
        Load Commands
      </button>
      <div className="mt-4 text-sm text-gray-600">
        <p className="font-medium">Expected format:</p>
        <pre className="mt-1 bg-gray-100 p-2 rounded text-xs">
{`{
  "coordinates": { "x": 0, "y": 0, "direction": "N" },
  "commands": ["R", "R"]
}`}
        </pre>
      </div>
    </div>
  );
};

export default RobotInput;
