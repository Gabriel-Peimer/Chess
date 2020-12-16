import Board


class Piece:
    """
    this is the base class for all of the pieces in the game.
    """

    def move_piece(self, position, board, location):
        board[location[0]][location[1]] = " "
        location = position
        self.update_location(board, location)
        Board.display_board(board)

    def update_location(self, board, location):
        board[location[0]][location[1]] = self
