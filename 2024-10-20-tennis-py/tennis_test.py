from tennis import tennis


def test_start_game():
    assert tennis() == 'love all'


def test_server_first_point():
    assert tennis(["server"]) == '15 love'


def test_server_wins_game():
    assert tennis(
            ["server", "server", "server", "server"]
            ) == 'game server'


def test_server_advantage():
    assert tennis(
            ["server", "server", "server", "receiver", "receiver", "receiver",
             "server"]
            ) == 'advantage server'


def test_server_30_love():
    assert tennis(
            ["server", "server"]
            ) == '30 love'


def test_server_40_love():
    assert tennis(
            ["server", "server", "server"]
            ) == '40 love'


def test_receiver_love_15():
    assert tennis(
            ["receiver"]
            ) == 'love 15'


def test_receiver_love_30():
    assert tennis(
            ["receiver", "receiver"]
            ) == 'love 30'


def test_receiver_love_40():
    assert tennis(
            ["receiver", "receiver", "receiver"]
            ) == 'love 40'


def test_receiver_30_all():
    assert tennis(
            ["receiver", "receiver", "server", "server"]
            ) == '30 all'
