# README

## What is TDD and Pairing

**TDD** - Test Driven Development OR Test Driven Design

1. Do not write any production code without a failing test first.
2. Write only enough test code as is sufficient enough to fail.
3. Only implement a minimal code that makes the failing test pass.

- workspace
- lolcommits

## Rover challenge

**Requirements**

- You are given the initial starting point `(x,y)` of a rover and the direction
  `(N,S,E,W)` it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward `(f,b)`.
- Implement commands that turn the rover left/right `(l,r)`.
- Implement wrapping at edges. But be careful, planets are spheres.
- Implement obstacle detection before each move to a new square. If a given
- sequence of commands encounters an obstacle, the rover moves up to the last
  possible point, aborts the sequence and reports the obstacle.

## Setup

```sh
mkdir 2025-01-29-mars-rover-py
cd 2025-01-29-mars-rover-py

adsf local python 3.10.4
python -m venv .venv
source .venv/bin/activate
```

```
cat << EOF > requirements.txt
pytest
flake8
EOF

pip install -r requirements.txt

cat << EOF > rover_test.py
from rover import rover
def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}
EOF

cat << EOF > rover.py
def rover(position_commands):
    return {"x": 0, "y": 0, "direction": "N"}
EOF

pytest -vvv
cp ../2024-10-20-tennis-py/justfile .
cp ../2024-10-20-tennis-py/.gitignore .
just build
