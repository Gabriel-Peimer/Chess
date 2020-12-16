class Knight:
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

    def find_possible_positions(self, board, y_position, x_position):
        for position in [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
            if y_position == self.location[0] + position[0] and x_position == self.location[1] + position[1]:
                return True
        return False
