import tkinter as tk
import Board
import MinMax

window = tk.Tk()
window.geometry("650x650")

num_of_players = 0
is_piece_selected = False
selection = None
selected_button = None
buttons = []
game_board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]]
color = Board.white
other_color = Board.black


file_beginning = "C:/Users/Gaby/PycharmProjects/Chess/Images"
pawn_white: tk.PhotoImage = tk.PhotoImage(file=file_beginning + "/Pawn_white (2).gif")
pawn_black = tk.PhotoImage(file=file_beginning + "/Pawn_black (2).gif")
knight_white = tk.PhotoImage(file=file_beginning + "/Knight_white (2).gif")
knight_black = tk.PhotoImage(file=file_beginning + "/Knight_black (2).gif")
bishop_white = tk.PhotoImage(file=file_beginning + "/Bishop_white (2).gif")
bishop_black = tk.PhotoImage(file=file_beginning + "/Bishop_black (2).gif")
rook_white = tk.PhotoImage(file=file_beginning + "/Rook_white (2).gif")
rook_black = tk.PhotoImage(file=file_beginning + "/Rook_black (2).gif")
queen_white = tk.PhotoImage(file=file_beginning + "/Queen_white (2).gif")
queen_black = tk.PhotoImage(file=file_beginning + "/Queen_black (2).gif")
king_white = tk.PhotoImage(file=file_beginning + "/King_white (2).gif")
king_black = tk.PhotoImage(file=file_beginning + "/King_black (2).gif")
white_color = tk.PhotoImage(file=file_beginning + "/WHITE.gif")
black_color = tk.PhotoImage(file=file_beginning + "/BLACK.gif")

image_dictionary = {
    "<class 'Pawn.Pawn'>": (pawn_white, pawn_black),
    "<class 'Knight.Knight'>": (knight_white, knight_black),
    "<class 'Bishop.Bishop'>": (bishop_white, bishop_black),
    "<class 'Rook.Rook'>": (rook_white, rook_black),
    "<class 'Queen.Queen'>": (queen_white, queen_black),
    "<class 'King.King'>": (king_white, king_black)
}
piece_worth_dictionary = {
    "<class 'Pawn.Pawn'>": 1,
    "<class 'Knight.Knight'>": 3,
    "<class 'Bishop.Bishop'>": 3,
    "<class 'Rook.Rook'>": 5,
    "<class 'Queen.Queen'>": 9,
    "<class 'King.King'>": 90,
    "<class 'str'>": 0}


def replay():
    global game_board, color, other_color, buttons, score_white, score_black
    game_board = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "]]
    Board.populate_board(game_board)
    display_board_graphic()
    display_board_graphic()
    color, other_color = Board.white, Board.black
    score_black = 0
    score_white = 0
    replay_button.grid_forget()
    end_game_label.grid_forget()


# for end game etc.
end_game_label = tk.Label(text="")
end_game_label.config(font=("Courier", 20))
# replay button
replay_button = tk.Button(text="Play Again", command=replay)
replay_button.config(font=("Courier", 20))
# for score
score_label_white = tk.Label(text="")
score_label_white.grid(row=1, column=10)
score_label_white.config(font=("Courier", 15))
score_label_black = tk.Label(text="")
score_label_black.grid(row=2, column=10)
score_label_black.config(font=("Courier", 15))
score_black = 0
score_white = 0
# difficulty for minimax (depth)
difficulty = 0


def select_difficulty():

    def set_difficulty(difficulty_selected):
        global difficulty
        difficulty = difficulty_selected

        select_a_difficulty.grid_forget()
        diff_1.grid_forget()
        diff_2.grid_forget()
        diff_3.grid_forget()
        diff_4.grid_forget()

        # running the game
        replay()
        display_board_graphic()
        display_board_graphic()

    select_a_difficulty = tk.Label(window, text="Select a difficulty")
    select_a_difficulty.config(font=("Courier", 20))
    diff_1 = tk.Button(window, text="1", command=lambda: set_difficulty(1))
    diff_1.config(font=("Courier", 20))
    diff_2 = tk.Button(window, text="2", command=lambda: set_difficulty(2))
    diff_2.config(font=("Courier", 20))
    diff_3 = tk.Button(window, text="3", command=lambda: set_difficulty(3))
    diff_3.config(font=("Courier", 20))
    diff_4 = tk.Button(window, text="4", command=lambda: set_difficulty(4))
    diff_4.config(font=("Courier", 20))

    select_a_difficulty.grid(row=0, column=0)
    diff_1.grid(row=0, column=1)
    diff_2.grid(row=0, column=2)
    diff_3.grid(row=0, column=3)
    diff_4.grid(row=0, column=4)


class Controller:
    def __init__(self, y_location, x_location):
        self.y_location = y_location
        self.x_location = x_location
        self.button = tk.Button(window, command=lambda: select_piece(
            game_board, color, y_location, x_location))
        self.set_grid_location(y_location, x_location)

    def set_grid_location(self, y_location, x_location):
        self.button.grid(row=y_location, column=x_location)


def update_score():
    score_label_white.configure(text=f"White- {score_white}")
    score_label_black.configure(text=f"Black- {score_black}")


def select_piece(board, current_color, y_position, x_position):
    global is_piece_selected, selection, color, other_color

    if not is_piece_selected:
        if board[y_position][x_position] != " ":  # not empty
            if board[y_position][x_position].color == current_color:
                is_piece_selected = True
                selection = (y_position, x_position)

    else:  # there is a piece selected
        # only run the following code if a piece actually has the ability to move there
        if board[selection[0]][selection[1]] != " ":

            # in case of a king. otherwise it may make the game freeze
            if str(type(board[selection[0]][selection[1]])) == "<class 'King.King'>":
                if board[selection[0]][selection[1]].castle(board, x_position):
                    color, other_color = other_color, color
                    display_board_graphic()
                    is_piece_selected = False

                    is_game_over(board)
                    computer_move(board)
                    is_game_over(board)
                    return

            # no longer a king...
            if board[selection[0]][selection[1]].find_possible_positions(
                    board, y_position, x_position):
                if Board.move_selected_piece(board,
                                             selection[0], selection[1],
                                             y_position, x_position, color):
                    update_score()
                    color, other_color = other_color, color
                    display_board_graphic()
                    is_piece_selected = False
                    if str(type(board[y_position][x_position])) == "<class 'Pawn.Pawn'>":
                        if board[y_position][x_position].check_for_switch():
                            popup(board[y_position][x_position])

                    is_game_over(board)
                    computer_move(board)
                    is_game_over(board)
            else:
                if board[y_position][x_position] != " ":  # not empty
                    if board[y_position][x_position].color == color:
                        selection = (y_position, x_position)  # change selection to last press
                else:
                    is_piece_selected = False


# if the game is one player and it is now the computers turn- run the following code
def computer_move(board):
    global color, other_color
    if num_of_players == 1 and color == Board.black:
        move_to_make = MinMax.minimax(board, difficulty, True, -99999, 99999)[0]
        if type(move_to_make) == tuple:
            if Board.move_selected_piece(board,
                                         move_to_make[0], move_to_make[1],
                                         move_to_make[2], move_to_make[3], color):
                update_score()
                color, other_color = other_color, color
                display_board_graphic()
            else:
                num_of_moves = len(Board.find_all_moves(board, color))
                for move in Board.find_all_moves(board, color):
                    if num_of_moves != 0:
                        num_of_moves -= 1
                        move_to_make = move

                        if Board.move_selected_piece(board,
                                                     move_to_make[0], move_to_make[1],
                                                     move_to_make[2], move_to_make[3], color):
                            update_score()
                            color, other_color = other_color, color
                            display_board_graphic()
                            break

            # if this statement is true, a black pawn has made it to the end
            if str(type(board[7][move_to_make[3]])) == "<class 'Pawn.Pawn'>":
                # change the pawn to a queen
                board[7][move_to_make[3]].switch_piece(board, "queen")
                display_board_graphic()


def is_game_over(board):
    # checking for check_mate or stale_mate options
    if Board.black_king.is_in_check_mate(board) or Board.white_king.is_in_check_mate(board):
        end_game_label.configure(text=f"{other_color} has won!".upper())
        end_game_label.grid(row=4, column=10)
        replay_button.grid(row=5, column=10)

    elif Board.black_king.is_in_stale_mate(board) or Board.white_king.is_in_stale_mate(board):
        end_game_label.configure(text=f"IT'S A STALE MATE")
        end_game_label.grid(row=4, column=10)
        replay_button.grid(row=5, column=10)


def popup(pawn):
    switch_pawn = tk.Toplevel()

    def swap(piece_type):
        pawn.switch_piece(game_board, piece_type)
        switch_pawn.destroy()
        display_board_graphic()

    switch_pawn.wm_title(other_color)

    color_number = 0
    if other_color == Board.black:
        color_number = 1

    label = tk.Label(switch_pawn, text="Pick a piece to swap the pawn ")
    queen_button = tk.Button(switch_pawn,
                             image=image_dictionary["<class 'Queen.Queen'>"][color_number],
                             command=lambda: swap("queen"))
    rook_button = tk.Button(switch_pawn,
                            image=image_dictionary["<class 'Rook.Rook'>"][color_number],
                            command=lambda: swap("rook"))
    bishop_button = tk.Button(switch_pawn,
                              image=image_dictionary["<class 'Bishop.Bishop'>"][color_number],
                              command=lambda: swap("bishop"))
    knight_button = tk.Button(switch_pawn,
                              image=image_dictionary["<class 'Knight.Knight'>"][color_number],
                              command=lambda: swap("knight"))

    label.pack(side="top")
    queen_button.pack()
    rook_button.pack()
    bishop_button.pack()
    knight_button.pack()
    switch_pawn.mainloop()


def display_board_graphic():
    global buttons, game_board
    if len(buttons) == 0:
        for y_location in range(len(game_board)):
            temp = []
            for x_location in range(len(game_board[y_location])):
                temp.append(Controller(y_location, x_location))
            buttons.append(temp)
    else:
        for y_location in range(len(game_board)):
            for x_location in range(len(game_board[y_location])):
                if game_board[y_location][x_location] != " ":
                    if game_board[y_location][x_location].color == Board.white:
                        buttons[y_location][x_location].button.configure(
                            image=image_dictionary[str(type(game_board[y_location][x_location]))][0])
                    else:
                        buttons[y_location][x_location].button.configure(
                            image=image_dictionary[str(type(game_board[y_location][x_location]))][1])
                else:
                    if abs(x_location - y_location) % 2 == 0:
                        buttons[y_location][x_location].button.configure(image=white_color)
                    else:
                        buttons[y_location][x_location].button.configure(image=black_color)
