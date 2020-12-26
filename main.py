import GraphicBoard
import Board
import tkinter as tk


def select_screen():

    def selected(num_of_players):
        if num_of_players == 1:
            GraphicBoard.num_of_players = num_of_players

            # forgetting the select screen widgets
            question.grid_forget()
            single_player.grid_forget()
            two_players.grid_forget()
            GraphicBoard.select_difficulty()

        elif num_of_players == 2:
            GraphicBoard.num_of_players = num_of_players
            # running the game
            GraphicBoard.display_board_graphic()
            GraphicBoard.display_board_graphic()

            # forgetting the select screen widgets
            question.grid_forget()
            single_player.grid_forget()
            two_players.grid_forget()

    question = tk.Label(GraphicBoard.window, text="Select a game mode")
    question.config(font=("Courier", 20))
    single_player = tk.Button(GraphicBoard.window, text="1 Player", command=lambda: selected(1))
    single_player.config(font=("Courier", 20))
    two_players = tk.Button(GraphicBoard.window, text="2 Players", command=lambda: selected(2))
    two_players.config(font=("Courier", 20))
    question.grid(row=1, column=5)
    single_player.grid(row=3, column=5)
    two_players.grid(row=4, column=5)


select_screen()
# This runs the game
Board.populate_board(GraphicBoard.game_board)
GraphicBoard.window.mainloop()
