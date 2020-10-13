class Board:
    def __init__(self, lines, columns):
        """
        :param lines: int > 0
        :param columns: int > 0
        """

        self.lines = lines
        self.columns = columns
        self.atr_board = [['0' for lines in range(self.lines)] for columns in range(self.columns)]

    def board(self):
        return self.atr_board

    def put_piece(self, piece, line, column):
        """
        :param column: int | columns
        :param line: int | line
        :param piece: str | player.color
        """
        self.board()[line][column] = piece


class Player:
    def __init__(self, color, qnt_piece, points=0):
        self.color = color
        self.qnt_piece = qnt_piece
        self.points = points


class Game:
    def __init__(self, line, column, color_one, color_two):
        self.board = Board(line, column)
        points = (line * column / 2)
        self.player_one = Player(color_one, points)
        self.player_two = Player(color_two, points)
        self.round = 0

    def move_piece(self, player, column):
        line = 0
        self.board.put_piece(player.color, line, column)

    def start(self):
        end = False
        while not end:
            print(f'Round {self.round} Player One')
            print(self.board())
            move = input('{what\'s your move?')
            self.move_piece(self.player_one, move)
            self.board.put_piece(self.player_one.color, 0, move)
            print(f'Round {self.round} Player Two')
            move = input('{what\'s your move?')

    # def vez_de_jogar(self):
    #     if self.jogador_1.qnt_piece % 2 == 1:
    #         return self.jogador_1
    #     else:
    #         return self.jogador_2
    #
    # def colocar_peca(self, lugar_de_colocar_a_peca):
    #     jogador = self.vez_de_jogar()
    #     self.tabuleiro.put_piece(jogador.color, lugar_de_colocar_a_peca)
    #     return self.imprimir()
    #
    # def imprimir(self):
    #     return self.tabuleiro.board()
    #
    # def regra_do_jogo(self):
    #     pass

# start


if __name__ == '__main__':
    line = input('How many lines should the board contains?')
    column = input('How many column should the board contains?')
    color_one = input('What color you want play with Player One?')
    color_two = input('What color you want play with Player Two?')
    game = Game(line, column, color_one, color_two)
    game.start()
