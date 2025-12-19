import random
import numpy as np
from problems_connect4 import Connect4

class MCTSAgent:
    def __init__(self, simulations=1000):
        self.simulations = simulations

    def simulate(self, game):
        temp_game = game.copy()
        while not temp_game.check_winner() and not temp_game.is_full():
            moves = temp_game.get_valid_moves()
            move = random.choice(moves)
            temp_game.make_move(move)
            temp_game.switch_player()
        winner = temp_game.check_winner()
        if winner == game.current_player:
            return 1
        elif winner == 0:
            return 0.5
        else:
            return 0

    def get_move(self, game):
        move_scores = {move: 0 for move in game.get_valid_moves()}

        for _ in range(self.simulations):
            for move in move_scores:
                temp_game = game.copy()
                temp_game.make_move(move)
                temp_game.switch_player()
                move_scores[move] += self.simulate(temp_game)

        best_move = max(move_scores, key=move_scores.get)
        return best_move

class MinimaxAgent:
    def __init__(self, depth=3):
        self.depth = depth

    def minimax(self, game, depth, maximizing):
        winner = game.check_winner()
        if winner != 0:
            return (1 if winner == 1 else -1)
        if game.is_full() or depth == 0:
            return 0

        valid_moves = game.get_valid_moves()

        if maximizing:
            max_eval = -np.inf
            for move in valid_moves:
                temp_game = game.copy()
                temp_game.make_move(move)
                temp_game.switch_player()
                eval = self.minimax(temp_game, depth-1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = np.inf
            for move in valid_moves:
                temp_game = game.copy()
                temp_game.make_move(move)
                temp_game.switch_player()
                eval = self.minimax(temp_game, depth-1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_move(self, game):
        best_move = None
        best_value = -np.inf
        for move in game.get_valid_moves():
            temp_game = game.copy()
            temp_game.make_move(move)
            temp_game.switch_player()
            move_value = self.minimax(temp_game, self.depth-1, False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move
