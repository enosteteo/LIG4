from board import Board
from player import Player

empty = '0'
confirm_end = '-404'


class Game:
    round = 0
    player_one = Player
    player_two = Player
    board = Board
    end = False

    def settings(self, line, column, color_one, color_two):
        points = (line * column / 2)
        self.player_one = Player(color_one, points)
        self.player_two = Player(color_two, points)
        self.board = Board(line, column, empty)
        self.line = line
        self.column = column

    def move_piece(self, player, column):
        self.check_is_end_game(column)
        self.is_valid(column)
        for line in range(self.line):
            if self.board.board()[line][column] == empty:
                self.board.put_piece(player.color, line, column)
                break

    def is_valid(self, column):
        # column is valid (between 0 and max column)
        if not (0 <= column <= self.column):
            raise Exception('invalid column. Choose another')

        # column is full
        if self.board.board()[self.line - 1][column] != empty:
            raise Exception('Complete column. Choose another')

    def print_board(self):
        board = self.board.board()
        return board

    def check_is_end_game(self, column):
        # End game
        if column == confirm_end:
            self.end = True

    def check_point(self):
        pass

    def check_win(self):
        pass

    def verify_status_game(self):
        self.check_point()
        self.check_is_end_game()

    def start(self):
        while not self.end:
            print('press -404 to exit')

            print(f'Round {self.round} Player One')
            print(self.print_board())
            move = input('{what\'s your move?')
            self.move_piece(self.player_one, move) # self.board.put_piece(self.player_one.color, 0, move)
            self.verify_status_game()
            print(self.print_board())

            print(f'Round {self.round} Player Two')
            move = input('{what\'s your move?')
            self.move_piece(self.player_two, move) # self.board.put_piece(self.player_two.color, 0, move)
            print(self.print_board())
            print(f'end round {self.round}')

            self.round += 1

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
