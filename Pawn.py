import Board
from Queen import Queen
from Knight import Knight
from Bishop import Bishop
from Rook import Rook


class Pawn:
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
        if self.capture_piece_possible(board, (y_position, x_position)):
            return True

        if self.color == "white":
            # if the player wants to continue forward
            if self.location[0] == 6 and y_position == 4 and self.location[1] == x_position:
                if board[y_position][x_position] == " ":
                    return True
            elif y_position + 1 == self.location[0] and x_position == self.location[1]:
                if not Board.check_position_full(board, (y_position, x_position), "white") and\
                        not Board.check_position_full(board, (y_position, x_position), "black"):
                    return True
            return False

        elif self.color == "black":
            # if the player wants to continue forward
            if self.location[0] == 1 and y_position == 3 and self.location[1] == x_position:
                if board[y_position][x_position] == " ":
                    return True
            if y_position - 1 == self.location[0] and x_position == self.location[1]:
                if not Board.check_position_full(board, (y_position, x_position), "white") and \
                        not Board.check_position_full(board, (y_position, x_position), "black"):
                    return True
            return False

    def capture_piece_possible(self, board, position):
        if not Board.check_position_full(board, position, self.color):
            if board[position[0]][position[1]] != " ":

                if self.color == "white":
                    if board[position[0]][position[1]].color == "black":
                        # checking for the possibility of capturing
                        # right turn
                        if position[0] + 1 == self.location[0] and position[1] - 1 == self.location[1]:
                            return True
                        # left turn
                        elif position[0] + 1 == self.location[0] and position[1] + 1 == self.location[1]:
                            return True

                elif self.color == "black":
                    if board[position[0]][position[1]].color == "white":
                        # checking for the possibility of capturing
                        # right turn
                        if position[0] - 1 == self.location[0] and position[1] - 1 == self.location[1]:
                            return True
                        # left turn
                        elif position[0] - 1 == self.location[0] and position[1] + 1 == self.location[1]:
                            return True
        return False

    def switch_piece(self, board, piece_type):
        if piece_type == "queen":
            board[self.location[0]][self.location[1]] = Queen(self.color, self.location, board)
        elif piece_type == "rook":
            board[self.location[0]][self.location[1]] = Rook(self.color, self.location, board)
        elif piece_type == "bishop":
            board[self.location[0]][self.location[1]] = Bishop(self.color, self.location, board)
        elif piece_type == "knight":
            board[self.location[0]][self.location[1]] = Knight(self.color, self.location, board)

    def check_for_switch(self):
        if self.location[0] == 0 or self.location[0] == 7:
            return True
        return False
