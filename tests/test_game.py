from game import Game


def test_game():
    game = Game(6, 7, 'x', 't')
    assert len(game.board.board()) == 7
    assert game.player_one.color == 'x'
    assert game.player_two.color == 't'