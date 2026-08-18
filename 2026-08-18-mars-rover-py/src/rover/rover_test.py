from rover.rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
    }) == {"x": 0, "y": 0, "direction": "N"}


def test_East_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["R"]
    }) == {"x": 0, "y": 0, "direction": "E"}
