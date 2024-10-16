from mars_rover import MarsRover


def test_mars_rover_stationary():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": []
        }).position() == {"x": 0, "y": 0, "direction": "N"}


def test_mars_rover_rotate_right_once():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": ["r"]
        }).position() == {"x": 0, "y": 0, "direction": "E"}


def test_mars_rover_rotate_right_twice():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": ["r", "r"]
        }).position() == {"x": 0, "y": 0, "direction": "S"}


def test_mars_rover_rotate_right_thrice():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": ["r", "r", "r"]
        }).position() == {"x": 0, "y": 0, "direction": "W"}


def test_mars_rover_rotate_right_fully():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": ["r", "r", "r", "r"]
        }).position() == {"x": 0, "y": 0, "direction": "N"}


def test_mars_rover_rotate_left():
    result = MarsRover({
        "x": 0,
        "y": 0,
        "direction": "N",
        "commands": ["l"]
        }).position()
    assert result == {"x": 0, "y": 0, "direction": "W"}
    result.update({"commands": ["l"]})
    result = MarsRover(result).position()
    assert result == {"x": 0, "y": 0, "direction": "S"}
    result.update({"commands": ["l"]})
    result = MarsRover(result).position()
    assert result == {"x": 0, "y": 0, "direction": "E"}
    result.update({"commands": ["l"]})
    result = MarsRover(result).position()
    assert result == {"x": 0, "y": 0, "direction": "N"}


def test_mars_rover_forward_N():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "N",
            "commands": ["f"]
        }).position() == {"x": 0, "y": 1, "direction": "N"}


def test_mars_rover_forward_E():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "E",
            "commands": ["f"]
        }).position() == {"x": 1, "y": 0, "direction": "E"}


def test_mars_rover_forward_S():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "S",
            "commands": ["f"]
        }).position() == {"x": 0, "y": -1, "direction": "S"}


def test_mars_rover_forward_W():
    assert MarsRover({
            "x": 0,
            "y": 0,
            "direction": "W",
            "commands": ["f"]
        }).position() == {"x": -1, "y": 0, "direction": "W"}


def test_mars_rover_backward():
    result = MarsRover({
        "x": 0,
        "y": 0,
        "direction": "N",
        "commands": ["b"]
        }).position()
    assert result == {"x": 0, "y": -1, "direction": "N"}
    result.update({"commands": ["r", "b"]})
    result = MarsRover(result).position()
    assert result == {"x": -1, "y": -1, "direction": "E"}
    result.update({"commands": ["r", "b"]})
    result = MarsRover(result).position()
    assert result == {"x": -1, "y": 0, "direction": "S"}
    result.update({"commands": ["r", "b"]})
    result = MarsRover(result).position()
    assert result == {"x": 0, "y": 0, "direction": "W"}


def test_mars_rover_complex_path_and_revers():
    result = MarsRover({
        "x": 0,
        "y": 0,
        "direction": "N",
        "commands": ["f", "r", "f", "r", "f", "f", "r", "f", "f", "r", "f"]
        }).position()
    assert result == {"x": -1, "y": 0, "direction": "N"}
    result.update(
        {"commands": ["b", "l", "b", "l", "b", "b", "l", "b", "b", "l", "b"]}
        )
    result = MarsRover(result).position()
    # assert(result) == {"x": 0, "y": 0, "direction": "N"}
    assert result == {"x": -2, "y": 0, "direction": "N"}
