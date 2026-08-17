from rover.rover import rover


def test_stationary_rover():
    assert rover({
        "x": 0, "y": 0, "direction": "N", "commands": []
    }) == {"x": 0, "y": 0, "direction": "N"}


def test_turn_rover_right():
    next_location = rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["r"]
    })
    assert next_location == {"x": 0, "y": 0, "direction": "E"}
    next_location.update({"commands": ["r"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "S"}
    next_location.update({"commands": ["r"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "W"}
    next_location.update({"commands": ["r"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "N"}


def test_turn_rover_left():
    next_location = rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["l"]
    })
    assert next_location == {"x": 0, "y": 0, "direction": "W"}
    next_location.update({"commands": ["l"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "S"}
    next_location.update({"commands": ["l"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "E"}
    next_location.update({"commands": ["l"]})
    next_location = rover(next_location)
    assert next_location == {"x": 0, "y": 0, "direction": "N"}


def test_3_turns_to_left():
    next_location = rover({
        "x": 0, "y": 0, "direction": "N", "commands": ["l", "l", "l"]
    })
    assert next_location == {"x": 0, "y": 0, "direction": "E"}


def test_can_move_forward_in_all_directions():
    defaults = {"x": 0, "y": 0, "direction": "N", "commands": ["f"]}
    next_location = rover(defaults | {"direction": "N"})
    assert next_location == {"x": 0, "y": 1, "direction": "N"}
    next_location = rover(defaults | {"direction": "E"})
    assert next_location == {"x": 1, "y": 0, "direction": "E"}
    next_location = rover(defaults | {"direction": "S"})
    assert next_location == {"x": 0, "y": -1, "direction": "S"}
    next_location = rover(defaults | {"direction": "W"})
    assert next_location == {"x": -1, "y": 0, "direction": "W"}


def test_can_move_backward_in_all_directions():
    defaults = {"x": 0, "y": 0, "direction": "N", "commands": ["b"]}
    next_location = rover(defaults | {"direction": "N"})
    assert next_location == {"x": 0, "y": -1, "direction": "N"}
    next_location = rover(defaults | {"direction": "E"})
    assert next_location == {"x": -1, "y": 0, "direction": "E"}
    next_location = rover(defaults | {"direction": "S"})
    assert next_location == {"x": 0, "y": 1, "direction": "S"}
    next_location = rover(defaults | {"direction": "W"})
    assert next_location == {"x": 1, "y": 0, "direction": "W"}
