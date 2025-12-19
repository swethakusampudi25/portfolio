import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ROWS = 6
COLUMNS = 7
CONNECT = 4

class Connect4:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), dtype=int)
        self.current_player = 1
        self.fig, self.ax = None, None

    def get_valid_moves(self):
        return [col for col in range(COLUMNS) if self.board[0][col] == 0]

    def make_move(self, col):
        for row in range(ROWS-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                break

    def switch_player(self):
        self.current_player = 1 if self.current_player == 2 else 2

    def check_winner(self):
        for row in range(ROWS):
            for col in range(COLUMNS-3):
                if all(self.board[row, col+i] == self.current_player for i in range(CONNECT)):
                    return self.current_player

        for row in range(ROWS-3):
            for col in range(COLUMNS):
                if all(self.board[row+i, col] == self.current_player for i in range(CONNECT)):
                    return self.current_player

        for row in range(ROWS-3):
            for col in range(COLUMNS-3):
                if all(self.board[row+i, col+i] == self.current_player for i in range(CONNECT)):
                    return self.current_player

        for row in range(3, ROWS):
            for col in range(COLUMNS-3):
                if all(self.board[row-i, col+i] == self.current_player for i in range(CONNECT)):
                    return self.current_player

        return 0

    def is_full(self):
        return all(self.board[0][col] != 0 for col in range(COLUMNS))

    def copy(self):
        new_game = Connect4()
        new_game.board = np.copy(self.board)
        new_game.current_player = self.current_player
        return new_game

    def initialize_display(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, COLUMNS)
        self.ax.set_ylim(0, ROWS)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        for r in range(ROWS):
            for c in range(COLUMNS):
                rect = patches.Rectangle((c, r), 1, 1, linewidth=1, edgecolor='black', facecolor='blue')
                self.ax.add_patch(rect)

        plt.ion()
        self.fig.show()

    def update_display(self):
        for artist in self.ax.patches[ROWS*COLUMNS:]:
            artist.remove()

        for r in range(ROWS):
            for c in range(COLUMNS):
                if self.board[ROWS-1 - r][c] == 1:
                    circle = patches.Circle((c+0.5, r+0.5), 0.4, color='yellow')  
                    self.ax.add_patch(circle)
                elif self.board[ROWS-1 - r][c] == 2:
                    circle = patches.Circle((c+0.5, r+0.5), 0.4, color='red')
                    self.ax.add_patch(circle)

        self.fig.canvas.draw()
        plt.pause(0.5)
