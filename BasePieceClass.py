class BasePiece:
    """
    this is the base class for all of the pieces in the game.
    """

    def __init__(self, color, location, board):
        self.color = color
        self.location = location
        board[self.location[0]][self.location[1]] = self

    def move_piece(self, position, board):
        board[self.location[0]][self.location[1]] = " "
        self.location = position
        self.update_location(board)

    def update_location(self, board):
        board[self.location[0]][self.location[1]] = self
