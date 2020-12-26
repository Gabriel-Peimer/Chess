import Board


def minimax(board, depth, maximizing, alpha, beta):
    if depth == 0:
        return None, Board.get_evaluating_score(board, Board.black) - Board.get_evaluating_score(board, Board.white)

    has_moved_temp = True

    if maximizing:
        max_evaluation = -99999
        best_move = Board.random_move(board, Board.black)

        # the following for loops find every possible position a piece can move to
        for move in Board.find_all_moves(board, Board.black):
            y, x, move_y, move_x = move[0], move[1], move[2], move[3]

            if not Board.check_position_full(board, (move_y, move_x), Board.black):
                # saving castling information
                if str(type(board[y][x])) == "<class 'Rook.Rook'>" or \
                        str(type(board[y][x])) == "<class 'King.King'>":
                    has_moved_temp = board[y][x].has_moved

                temp = board[move_y][move_x]
                board[y][x].move_piece((move_y, move_x), board)

                if not Board.black_king.is_in_check(
                        board, Board.black_king.location[0], Board.black_king.location[1]):
                    evaluation = minimax(board, depth - 1, False, alpha, beta)[1]

                    board[move_y][move_x].move_piece((y, x), board)
                    board[move_y][move_x] = temp
                    # so that the king will still have the ability to castle
                    if not has_moved_temp:
                        board[y][x].has_moved = False

                    if Board.white_king.is_in_check_mate(board):
                        evaluation = 99999

                    if max_evaluation < evaluation:
                        best_move = move
                        max_evaluation = evaluation

                    alpha = max(alpha, evaluation)
                    if beta <= alpha:
                        break
                else:
                    board[move_y][move_x].move_piece((y, x), board)
                    board[move_y][move_x] = temp
                    if not has_moved_temp:
                        board[y][x].has_moved = False

        return best_move, max_evaluation
    
    else:
        min_evaluation = 99999
        best_move = Board.random_move(board, Board.white)

        # the following for loops find every possible position a piece can move to
        for move in Board.find_all_moves(board, Board.white):
            y, x, move_y, move_x = move[0], move[1], move[2], move[3]

            if not Board.check_position_full(board, (move_y, move_x), Board.white):
                # saving castling information
                if str(type(board[y][x])) == "<class 'Rook.Rook'>" or \
                        str(type(board[y][x])) == "<class 'King.King'>":
                    has_moved_temp = board[y][x].has_moved

                temp = board[move_y][move_x]
                board[y][x].move_piece((move_y, move_x), board)

                if not Board.white_king.is_in_check(
                        board, Board.white_king.location[0], Board.white_king.location[1]):

                    evaluation = minimax(board, depth - 1, True, alpha, beta)[1]

                    board[move_y][move_x].move_piece((y, x), board)
                    board[move_y][move_x] = temp
                    # so that the king still can castle
                    if not has_moved_temp:
                        board[y][x].has_moved = False

                    if Board.black_king.is_in_check_mate(board):
                        evaluation = -99999

                    if min_evaluation > evaluation:
                        best_move = move
                        min_evaluation = evaluation

                    beta = min(beta, evaluation)
                    if beta <= alpha:
                        break
                else:
                    board[move_y][move_x].move_piece((y, x), board)
                    board[move_y][move_x] = temp
                    # so the castling stays in tact
                    if not has_moved_temp:
                        board[y][x].has_moved = False

        return best_move, min_evaluation
