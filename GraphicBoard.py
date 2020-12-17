import tkinter as tk
import Board

window = tk.Tk()
window.geometry("650x650")

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


def replay():
    global game_board, color, other_color, buttons
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
    color, other_color = "white", "black"
    replay_button.grid_forget()
    end_game_label.grid_forget()


is_piece_selected = False
selection = None
selected_button = None
buttons = []

# for end game etc.
end_game_label = tk.Label(text="")
end_game_label.config(font=("Courier", 20))
replay_button = tk.Button(text="Play Again", command=replay)
replay_button.config(font=("Courier", 20))

game_board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]]
color = "white"
other_color = "black"


class Controller:
    def __init__(self, board, y_location, x_location):
        self.y_location = y_location
        self.x_location = x_location
        self.button = tk.Button(window, command=lambda: select_piece(
            board, color, y_location, x_location))
        self.set_grid_location(y_location, x_location)

    def set_grid_location(self, y_location, x_location):
        self.button.grid(row=y_location, column=x_location)


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

            if str(type(board[selection[0]][selection[1]])) == "<class 'King.King'>":
                if board[selection[0]][selection[1]].castle(board, x_position):
                    color, other_color = other_color, color
                    display_board_graphic()
                    is_piece_selected = False
                    return

            if board[selection[0]][selection[1]].find_possible_positions(board, y_position, x_position):
                if Board.move_selected_piece(board,
                                             selection[0],
                                             selection[1],
                                             y_position, x_position, color):
                    color, other_color = other_color, color
                    display_board_graphic()
                    is_piece_selected = False
                    if str(type(board[y_position][x_position])) == "<class 'Pawn.Pawn'>":
                        if board[y_position][x_position].check_for_switch():
                            popup(board[y_position][x_position])

                    # checking for check_mate or stale_mate options
                    if Board.black_king.is_in_check_mate(board) or Board.white_king.is_in_check_mate(board):
                        end_game_label.configure(text=f"{other_color} has won!".upper())
                        end_game_label.grid(row=4, column=10)
                        replay_button.grid(row=5, column=10)

                    elif Board.black_king.is_in_stale_mate(board) or Board.white_king.is_in_stale_mate(board):
                        end_game_label.configure(text=f"IT'S A STALE MATE")
                        end_game_label.grid(row=4, column=10)
                        replay_button.grid(row=5, column=10)

                else:
                    display_board_graphic()
            else:
                if board[y_position][x_position] != " ":  # not empty
                    if board[y_position][x_position].color == color:
                        selection = (y_position, x_position)  # change selection to last press
                else:
                    is_piece_selected = False


def popup(pawn):
    switch_pawn = tk.Toplevel()

    def swap(piece_type):
        pawn.switch_piece(game_board, piece_type)
        switch_pawn.destroy()
        display_board_graphic()

    switch_pawn.wm_title(other_color)

    color_number = 0
    if other_color == "black":
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
                temp.append(Controller(game_board, y_location, x_location))
            buttons.append(temp)
    else:
        for y_location in range(len(game_board)):
            for x_location in range(len(game_board[y_location])):
                if game_board[y_location][x_location] != " ":
                    if game_board[y_location][x_location].color == "white":
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
