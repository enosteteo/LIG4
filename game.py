class Tabuleiro():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tab = [[0 for x in range(self.x)] for y in range(self.y)]

    def colocar_peca(self, peca, x):
        self[0][x] = peca
        return self.tab

    def imprimir(self):
        for x_linha in range(self.x):
            for y_linha in range(self.y):
                if y_linha == y - 1:
                    print(f'{tabuleiro[x_linha][y_linha]}')
                else:
                    print(f'{tabuleiro[x_linha][y_linha]}', end=" ")


class Jogador():
    def __init__(self, peca, qnt_peca):
        self.peca = peca
        self.qnt_peca = qnt_peca
        self.pontos = 0


if __name__ == '__main__':
    jogador_1 = Jogador('x', 21)
    jogador_2 = Jogador('z', 21)
    tabuleiro = Tabuleiro(6, 7)
    tabuleiro.colocar_peca(jogador_1.peca, 2)
    tabuleiro.imprimir_tabuleiro()
