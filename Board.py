import random
import GraphicBoard
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from Knight import Knight
from King import King

white = "white"
black = "black"


# this function displays the board
def display_board(board):
    for num in range(len(board)):
        print(board[num])


def check_position_full(board, position, color):
    if position[0] < 0 or position[1] < 0:
        return True
    try:
        if board[position[0]][position[1]].color == color:
            return True
    except AttributeError:
        return False
    except IndexError:
        return True


def move_selected_piece(board, y_location, x_location, y_position, x_position, color):
    if not check_position_full(board, (y_position, x_position), color):
        temp = board[y_position][x_position]
        board[y_location][x_location].move_piece((y_position, x_position), board)
        score = GraphicBoard.piece_worth_dictionary[str(type(temp))]
        # checking for possible check in which case we move the piece that moved back
        if color == white:
            GraphicBoard.score_white += score
            if white_king.is_in_check(board, white_king.location[0], white_king.location[1]):
                board[y_position][x_position].move_piece((y_location, x_location), board)
                board[y_position][x_position] = temp
                return False

        elif color == black:
            GraphicBoard.score_black += score
            if black_king.is_in_check(board, black_king.location[0], black_king.location[1]):
                board[y_position][x_position].move_piece((y_location, x_location), board)
                board[y_position][x_position] = temp
                return False
        return True
    return False


white_king = ""
black_king = ""


def populate_board(board):
    global white_king, black_king
    Pawn(white, (6, 0), board)
    Pawn(white, (6, 1), board)
    Pawn(white, (6, 2), board)
    Pawn(white, (6, 3), board)
    Pawn(white, (6, 4), board)
    Pawn(white, (6, 5), board)
    Pawn(white, (6, 6), board)
    Pawn(white, (6, 7), board)
    Rook(white, (7, 0), board)
    Rook(white, (7, 7), board)
    Bishop(white, (7, 2), board)
    Bishop(white, (7, 5), board)
    Knight(white, (7, 1), board)
    Knight(white, (7, 6), board)
    Queen(white, (7, 3), board)
    white_king = King(white, (7, 4), board)

    Pawn(black, (1, 0), board)
    Pawn(black, (1, 1), board)
    Pawn(black, (1, 2), board)
    Pawn(black, (1, 3), board)
    Pawn(black, (1, 4), board)
    Pawn(black, (1, 5), board)
    Pawn(black, (1, 6), board)
    Pawn(black, (1, 7), board)
    Rook(black, (0, 7), board)
    Rook(black, (0, 0), board)
    Bishop(black, (0, 2), board)
    Bishop(black, (0, 5), board)
    Knight(black, (0, 1), board)
    Knight(black, (0, 6), board)
    Queen(black, (0, 3), board)
    black_king = King(black, (0, 4), board)


def find_all_moves(board, color):
    moves = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != " ":
                if board[y][x].color == color:
                    for move_y in range(len(board)):
                        for move_x in range(len(board[move_y])):
                            if board[y][x].find_possible_positions(
                                    board, move_y, move_x):
                                moves.append((y, x, move_y, move_x))

    return moves


def random_move(board, color):
    return random.choice(find_all_moves(board, color))


def get_evaluating_score(board, color):
    score = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != " ":
                if board[y][x].color == color:
                    score += GraphicBoard.piece_worth_dictionary[str(type(board[y][x]))]
    return score
