from rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}

def test_stationary_rover_360():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["r"]
        }) == {"x": 0, "y": 0, "direction": "E"}
