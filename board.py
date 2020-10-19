class Board:
    def __init__(self, lines, columns, empty='0'):
        """
        :param lines: int > 0
        :param columns: int > 0
        """

        self.lines = lines
        self.columns = columns
        self.atr_board = [[empty for lines in range(self.lines)] for columns in range(self.columns)]

    def board(self):
        return self.atr_board

    def put_piece(self, piece, line, column):
        """
        :param column: int | columns
        :param line: int | line
        :param piece: str | player.color
        """
        self.board()[line][column] = piece