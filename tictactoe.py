import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("400x450")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create reset button
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game, font=('Helvetica', 12, 'bold'))
        self.reset_button.pack(pady=20)

        # Create the tic-tac-toe buttons
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(9):
            button = tk.Button(frame, text="", width=10, height=3, font=('Helvetica', 20), command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Helvetica', 12, 'bold'))
        self.status_label.pack(pady=20)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")
        for button in self.buttons:
            button.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()