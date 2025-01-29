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


def test_rover_forwards_backwards():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['f', 'b']
        }) == {"x": 0, "y": 0, "direction": "N"}


def test_rover_forwards_in_all_directions():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['f']
        }) == {"x": 1, "y": 0, "direction": "N"}
    assert rover({
        "x": 0, "y": 0, "direction": "E", "commands": ['f']
        }) == {"x": 0, "y": 1, "direction": "E"}
    assert rover({
        "x": 0, "y": 0, "direction": "S", "commands": ['f']
        }) == {"x": -1, "y": 0, "direction": "S"}
    assert rover({
        "x": 0, "y": 0, "direction": "W", "commands": ['f']
        }) == {"x": 0, "y": -1, "direction": "W"}


def test_rover_backwards_in_all_directions():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ['b']
        }) == {"x": -1, "y": 0, "direction": "N"}
    assert rover({
        "x": 0, "y": 0, "direction": "E", "commands": ['b']
        }) == {"x": 0, "y": -1, "direction": "E"}
    assert rover({
        "x": 0, "y": 0, "direction": "S", "commands": ['b']
        }) == {"x": 1, "y": 0, "direction": "S"}
    assert rover({
        "x": 0, "y": 0, "direction": "W", "commands": ['b']
        }) == {"x": 0, "y": 1, "direction": "W"}
