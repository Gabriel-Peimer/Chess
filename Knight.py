import BasePieceClass


class Knight(BasePieceClass.BasePiece):
    def find_possible_positions(self, board, y_position, x_position):
        for position in [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            if y_position == self.location[0] + position[0] and x_position == self.location[1] + position[1]:
                return True
        return False
