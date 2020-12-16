import Board


class Queen:
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
        is_way_free = True

        if abs(self.location[0] - y_position) == abs(self.location[1] - x_position):
            for index in range(abs(self.location[0] - y_position) - 1):
                if self.location[1] < x_position:
                    if self.location[0] < y_position:
                        if board[self.location[0] + (index + 1)][self.location[1] + (index + 1)] != " ":
                            is_way_free = False
                            break
                    else:
                        if board[self.location[0] - (index + 1)][self.location[1] + (index + 1)] != " ":
                            is_way_free = False
                            break

                else:
                    if self.location[0] < y_position:
                        if board[self.location[0] + (index + 1)][self.location[1] - (index + 1)] != " ":
                            is_way_free = False
                            break
                    else:
                        if board[self.location[0] - (index + 1)][self.location[1] - (index + 1)] != " ":
                            is_way_free = False
                            break

        else:
            if self.location[0] != y_position and self.location[1] == x_position:
                for index in range(abs(y_position - self.location[0]) - 1):
                    if self.location[0] < y_position:
                        if board[self.location[0] + (index + 1)][self.location[1]] != " ":
                            is_way_free = False
                    else:
                        if board[self.location[0] - (index + 1)][self.location[1]] != " ":
                            is_way_free = False

            elif self.location[0] == y_position and self.location[1] != x_position:
                for index in range(abs(x_position - self.location[1]) - 1):
                    if self.location[1] < x_position:
                        if board[self.location[0]][self.location[1] + (index + 1)] != " ":
                            is_way_free = False
                    else:
                        if board[self.location[0]][self.location[1] - (index + 1)] != " ":
                            is_way_free = False
            else:
                is_way_free = False

        if is_way_free:
            if not Board.check_position_full(board, (y_position, x_position), self.color):
                return True
        return False
