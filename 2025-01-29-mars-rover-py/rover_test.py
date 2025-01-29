from rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}


def test_rover_forwards():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['f']
        }) == {"x": 1, "y": 0, "direction": "N"}


def test_rover_forwards_multiple_times():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['f', 'f']
        }) == {"x": 2, "y": 0, "direction": "N"}
