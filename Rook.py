from BasePieceClass import BasePiece
import Board


class Rook(BasePiece):
    def __init__(self, color, location, board):
        super().__init__(color, location, board)
        self.has_moved = False

    def move_piece(self, position, board):
        board[self.location[0]][self.location[1]] = " "
        self.location = position
        self.update_location(board)
        self.has_moved = True

    def find_possible_positions(self, board, y_position, x_position):
        is_way_free = True

        if self.location[0] != y_position and self.location[1] == x_position:
            for index in range(abs(y_position - self.location[0]) - 1):
                if self.location[0] < y_position:
                    if board[self.location[0] + (index + 1)][self.location[1]] != " ":
                        is_way_free = False
                else:
                    if board[self.location[0] - (index + 1)][self.location[1]] != " ":
                        is_way_free = False

            if is_way_free:
                if not Board.check_position_full(board, (y_position, x_position), self.color):
                    return True

        elif self.location[0] == y_position and self.location[1] != x_position:
            for index in range(abs(x_position - self.location[1]) - 1):
                if self.location[1] < x_position:
                    if board[self.location[0]][self.location[1] + (index + 1)] != " ":
                        is_way_free = False
                else:
                    if board[self.location[0]][self.location[1] - (index + 1)] != " ":
                        is_way_free = False

            if is_way_free:
                if not Board.check_position_full(board, (y_position, x_position), self.color):
                    return True
        return False
