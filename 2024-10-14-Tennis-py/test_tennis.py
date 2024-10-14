from tennis import Game


def test_start_game():
    game = Game()
    for _ in range(0):
        game.point("server")
    assert game.score() == 'love all'


def test_server_scores():
    game = Game()
    for _ in range(1):
        game.point("server")
    assert game.score() == '15 love'


def test_server_scores_twice():
    game = Game()
    for _ in range(2):
        game.point("server")
    assert game.score() == '30 love'


def test_server_scores_three_times():
    game = Game()
    for _ in range(3):
        game.point("server")
    assert game.score() == '40 love'


def test_receiver_scores_three_times():
    game = Game()
    for _ in range(3):
        game.point("receiver")
    assert game.score() == 'love 40'


def test_server_server_receiver_scores():
    game = Game()
    game.point("server")
    game.point("server")
    game.point("receiver")
    assert game.score() == '30 15'


def test_deuce():
    game = Game()
    for _ in range(3):
        game.point("receiver")
        game.point("server")
    assert game.score() == 'deuce'


def test_advantage_server():
    game = Game()
    for _ in range(3):
        game.point("receiver")
        game.point("server")
    game.point("server")
    assert game.score() == 'advantage server'


def test_game_server():
    game = Game()
    for _ in range(3):
        game.point("receiver")
        game.point("server")
    game.point("server")
    game.point("server")
    assert game.score() == 'game server'


def test_advantage_receiver():
    game = Game()
    for _ in range(3):
        game.point("receiver")
        game.point("server")
    game.point("receiver")
    assert game.score() == 'advantage receiver'


def test_game_receiver():
    game = Game()
    for _ in range(4):
        game.point("receiver")
    assert game.score() == 'game receiver'
