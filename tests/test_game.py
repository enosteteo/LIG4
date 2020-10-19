from game import Game
from player import Player


def test_game():
    line = 6
    column = 7

    game = Game()
    game.settings(line, column, 'x', 't')
    assert len(game.board.board()) == 7
    assert game.player_one.color == 'x'
    assert game.player_two.color == 't'


def test_move_piece():

    line = 6
    column = 7
    points = (line * column / 2)

    game = Game()
    game.settings(line, column, 'x', 't')
    player_one = Player('x', points)

    game.move_piece(player_one, 3)
    print(game.print_board())
    assert game.print_board()[0][3] == player_one.color