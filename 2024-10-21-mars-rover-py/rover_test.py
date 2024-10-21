from rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        }) == {"x": 0, "y": 0, "direction": "N"}


def test_rotates_right():
    location = rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        })
    assert location == {"x": 0, "y": 0, "direction": "N"}
    location.update({"commands": ["r"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "E"}
    location.update({"commands": ["r"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "S"}
    location.update({"commands": ["r"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "W"}
    location.update({"commands": ["r"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "N"}


def test_rotates_left():
    location = rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
        })
    assert location == {"x": 0, "y": 0, "direction": "N"}
    location.update({"commands": ["l"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "W"}
    location.update({"commands": ["l"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "S"}
    location.update({"commands": ["l"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "E"}
    location.update({"commands": ["l"]})
    location = rover(location)
    assert location == {"x": 0, "y": 0, "direction": "N"}


def test_moves_forward():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["f"]
        }) == {"x": 0, "y": 1, "direction": "N"}
    assert rover({
        "x": 0, "y": 0, "direction": "E", "commands": ["f"]
        }) == {"x": 1, "y": 0, "direction": "E"}
    assert rover({
        "x": 0, "y": 0, "direction": "S", "commands": ["f"]
        }) == {"x": 0, "y": -1, "direction": "S"}
    assert rover({
        "x": 0, "y": 0, "direction": "W", "commands": ["f"]
        }) == {"x": -1, "y": 0, "direction": "W"}


def test_moves_backward():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["b"]
        }) == {"x": 0, "y": -1, "direction": "N"}
    assert rover({
        "x": 0, "y": 0, "direction": "E", "commands": ["b"]
        }) == {"x": -1, "y": 0, "direction": "E"}
    assert rover({
        "x": 0, "y": 0, "direction": "S", "commands": ["b"]
        }) == {"x": 0, "y": 1, "direction": "S"}
    assert rover({
        "x": 0, "y": 0, "direction": "W", "commands": ["b"]
        }) == {"x": 1, "y": 0, "direction": "W"}
