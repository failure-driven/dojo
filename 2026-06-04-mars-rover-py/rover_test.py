from rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}


def test_rover_moves_north():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['f']
        }) == {"x": 0, "y": 1, "direction": "N"}
