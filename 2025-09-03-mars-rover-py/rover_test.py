from rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}


def test_stationary_rover_360():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["r"]
        }) == {"x": 0, "y": 0, "direction": "E"}

    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["r", "r"]
        }) == {"x": 0, "y": 0, "direction": "S"}


def test_right_rotation():
    assert rover({
        "x": 0, "y": 0, "direction": "S", "commands": ["r"]
        }) == {"x": 0, "y": 0, "direction": "W"}
