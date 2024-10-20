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
