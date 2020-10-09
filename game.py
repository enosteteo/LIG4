class Tabuleiro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tab = [[0 for x in range(self.x)] for y in range(self.y)]

    def colocar_peca(self, peca,lugar_de_colocar_a_peca):
        self.tab[0][lugar_de_colocar_a_peca] = peca
        return self.imprimir()

    def imprimir(self):
        return self.tab


class Jogador:
    def __init__(self, peca, qnt_peca):
        self.peca = peca
        self.qnt_peca = qnt_peca
        self.pontos = 0


class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro(6, 7)
        self.jogador_1 = Jogador('x', 21)
        self.jogador_2 = Jogador('y', 21)
        self.round = 0

    def vez_de_jogar(self):
        if self.jogador_1.qnt_peca % 2 == 1:
            return self.jogador_1
        else:
            return self.jogador_2

    def colocar_peca(self, lugar_de_colocar_a_peca):
        jogador = self.vez_de_jogar()
        self.tabuleiro.colocar_peca(jogador.peca, lugar_de_colocar_a_peca)
        return self.imprimir()

    def imprimir(self):
        return self.tabuleiro.imprimir()

    def regra_do_jogo(self):
        pass


def jogada_valida():
    pass


if __name__ == '__main__':
    jogo = Jogo()
    jogo.colocar_peca(2)
    print(jogo.imprimir())
