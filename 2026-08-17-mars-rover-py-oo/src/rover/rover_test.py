from rover import Rover
from rover.rover import Position


def test_stationary_rover():
    rover = Rover()
    assert rover.location() == Position(x=0, y=0, direction="N")


def test_rover_turns_left():
    rover = Rover()
    rover.move(["l"])
    assert rover.location() == Position(x=0, y=0, direction="W")
    rover.move(["l"])
    assert rover.location() == Position(x=0, y=0, direction="S")
    rover.move(["l"])
    assert rover.location() == Position(x=0, y=0, direction="E")
    rover.move(["l"])
    assert rover.location() == Position(x=0, y=0, direction="N")


def test_rover_turns_right():
    rover = Rover()
    rover.move(["r"])
    assert rover.location() == Position(x=0, y=0, direction="E")
    rover.move(["r"])
    assert rover.location() == Position(x=0, y=0, direction="S")
    rover.move(["r"])
    assert rover.location() == Position(x=0, y=0, direction="W")
    rover.move(["r"])
    assert rover.location() == Position(x=0, y=0, direction="N")


def test_rover_moves_forward():
    rover = Rover()
    rover.move(["f"])
    assert rover.location() == Position(x=0, y=1, direction="N")
    rover = Rover(Position(x=0, y=0, direction="E"))
    rover.move(["f"])
    assert rover.location() == Position(x=1, y=0, direction="E")
    rover = Rover(Position(x=0, y=0, direction="S"))
    rover.move(["f"])
    assert rover.location() == Position(x=0, y=-1, direction="S")
    rover = Rover(Position(x=0, y=0, direction="W"))
    rover.move(["f"])
    assert rover.location() == Position(x=-1, y=0, direction="W")


def test_rover_moves_backward():
    rover = Rover()
    rover.move(["b"])
    assert rover.location() == Position(x=0, y=-1, direction="N")
    rover = Rover(Position(x=0, y=0, direction="E"))
    rover.move(["b"])
    assert rover.location() == Position(x=-1, y=0, direction="E")
    rover = Rover(Position(x=0, y=0, direction="S"))
    rover.move(["b"])
    assert rover.location() == Position(x=0, y=1, direction="S")
    rover = Rover(Position(x=0, y=0, direction="W"))
    rover.move(["b"])
    assert rover.location() == Position(x=1, y=0, direction="W")
