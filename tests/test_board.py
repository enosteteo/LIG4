from board import Board


def test_create_board_with_6_lines_7_columns():
    tab = Board(6, 7)   # linhas / colunas
    assert type(tab) == Board
    assert len(tab.board()) == 7
    assert len(tab.board()[0]) == 6


def test_put_piece():
    tab = Board(6, 7)   # linhas / colunas
    tab.put_piece('x', 2, 4)
    assert tab.board()[2][4] == 'x'
