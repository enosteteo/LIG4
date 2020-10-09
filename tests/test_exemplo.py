from game import Tabuleiro, Jogador


def test_tab():
    tab = Tabuleiro(6, 7)
    assert type(tab) == Tabuleiro
    assert tab.imprimir()[0].count(0) == 6


def test_jogador():
    jogador_1 = Jogador('x', 21)
    assert jogador_1.peca == 'x'
    assert jogador_1.qnt_peca == 21
    assert jogador_1.pontos == 0


def test_logica_do_jogo():
    tab = Tabuleiro(6, 7)
    for y in tab.imprimir():
        for x in y:
            assert x == 0
    # tab.colocar_peca('x', 2)
    # assert tab.imprimir()[6][2] == 'x'
    # assert tab.imprimir()[6].count('x') == 1
