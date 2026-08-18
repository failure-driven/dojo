from rover.rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
    }) == {"x": 0, "y": 0, "direction": "N"}


def test_East_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["R"]
    }) == {"x": 0, "y": 0, "direction": "E"}

def test_right_again_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "E", "commands": ["R"]
    }) == {"x": 0, "y": 0, "direction": "S"}

def test_right_turn_from_west_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "W", "commands": ["R"]
    }) == {"x": 0, "y": 0, "direction": "N"}
