import BasePieceClass
import Board


class King(BasePieceClass.BasePiece):
    def __init__(self, color, location, board):
        super().__init__(color, location, board)
        self.has_moved = False

    def move_piece(self, position, board):
        board[self.location[0]][self.location[1]] = " "
        self.location = position
        self.update_location(board)
        self.has_moved = True

    def castle(self, board, x_position):
        if not self.has_moved:
            if x_position == 6:
                if not board[self.location[0]][7].has_moved:
                    if board[self.location[0]][5] == " " and board[self.location[0]][6] == " ":
                        if not self.is_in_check(board, self.location[0], 5) and \
                                not self.is_in_check(board, self.location[0], 6):
                            Board.move_selected_piece(
                                board,
                                self.location[0], 4,
                                self.location[0], 6,
                                self.color)
                            Board.move_selected_piece(
                                board,
                                self.location[0], 7,
                                self.location[0], 5,
                                self.color)
                            return True
            elif x_position == 2:
                if not board[self.location[0]][0].has_moved:
                    if board[self.location[0]][3] == " " and board[self.location[0]][2] == " ":
                        if not self.is_in_check(board, self.location[0], 3) and\
                                not self.is_in_check(board, self.location[0], 2):
                            Board.move_selected_piece(
                                board,
                                self.location[0], 4,
                                self.location[0], 2,
                                self.color)
                            Board.move_selected_piece(
                                board, self.location[0], 0,
                                self.location[0], 3,
                                self.color)
                            return True
        return False

    def is_in_check(self, board, y_location, x_location):
        for y_position in range(len(board)):
            for x_position in range(len(board[y_position])):
                if board[y_position][x_position] != " ":  # the location is containing a piece
                    if board[y_position][x_position].color != self.color:
                        if str(type(board[y_position][x_position])) != "<class 'Pawn.Pawn'>":
                            if board[y_position][x_position].find_possible_positions(
                                    board, y_location, x_location):
                                return True

                        else:
                            if board[y_position][x_position].capture_piece_possible(board, (y_location, x_location)):
                                return True
        return False

    def is_in_check_mate(self, board):
        if self.is_in_check(board, self.location[0], self.location[1]):  # in basic check
            for position in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if not self.is_in_check(
                        board, self.location[0] + position[0], self.location[1] + position[1]):
                    if not Board.check_position_full(board, (self.location[0] + position[0],
                                                             self.location[1] + position[1]),
                                                     self.color):
                        return False

            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] != " ":
                        if board[y][x].color == self.color:
                            for move_y in range(len(board)):
                                for move_x in range(len(board[move_y])):
                                    if board[y][x].find_possible_positions(board, move_y, move_x):
                                        temp = board[move_y][move_x]
                                        board[y][x].move_piece((move_y, move_x), board)
                                        if not self.is_in_check(board, self.location[0], self.location[1]):
                                            board[move_y][move_x].move_piece((y, x), board)
                                            board[move_y][move_x] = temp
                                            return False
                                        board[move_y][move_x].move_piece((y, x), board)
                                        board[move_y][move_x] = temp
            return True

    def is_in_stale_mate(self, board):
        if not self.is_in_check(board, self.location[0], self.location[1]):  # not in check
            for position in [(0, 1), (0, -1), (1, 0),
                             (-1, 0), (-1, -1), (1, 1),
                             (-1, 1), (1, -1)]:
                if not self.is_in_check(  # make sure he doesn't move into check
                        board, self.location[0] + position[0], self.location[1] + position[1]):
                    if not Board.check_position_full(  # make sure that location is not occupied
                            board, (self.location[0] + position[0],
                                    self.location[1] + position[1]), self.color):
                        return False

            # the following loops check to see if any piece of self.color can move
            # if none of them can- we're at a stale mate
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] != " ":
                        if board[y][x].color == self.color:
                            for move_y in range(len(board)):
                                for move_x in range(len(board[move_y])):
                                    if board[y][x].find_possible_positions(board, move_y, move_x):
                                        return False
            return True

    def find_possible_positions(self, board, y_position, x_position):
        if not Board.check_position_full(board, (y_position, x_position), self.color):
            for position in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if self.color == "white":
                    if Board.black_king.location[0] + position[0] == y_position and\
                            Board.black_king.location[1] + position[1] == x_position:
                        return False
                if self.color == "black":
                    if Board.white_king.location[0] + position[0] == y_position and\
                            Board.white_king.location[1] + position[1] == x_position:
                        return False

            for position in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                if y_position == self.location[0] + position[0] and \
                        x_position == self.location[1] + position[1]:
                    # the next line checks if the king wouldn't be in check in the given position
                    if not self.is_in_check(board, y_position, x_position):
                        return True
            return False
        return False
