'''
This file will contain implementations of each algorithm/agent type.
'''
import random
import copy
import numpy as np
from problems import Game2048

class MCTSAgent:
    def __init__(self, game, simulations=100):
        self.game = game
        self.simulations = simulations

    def simulate(self, game_copy):
        for _ in range(self.simulations):
            possible_moves = ["left", "right", "up", "down"]
            move = random.choice(possible_moves)
            getattr(game_copy, f"move_{move}")()

    def get_best_move(self):
        best_move = None
        best_score = -1
        original_grid = self.game.grid.copy()

        for move in ["left", "right", "up", "down"]:
            game_copy = copy.deepcopy(self.game)
            getattr(game_copy, f"move_{move}")()

            if np.array_equal(game_copy.grid, original_grid):
                continue

            self.simulate(game_copy)
            score = np.max(game_copy.grid)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def play_turn(self, player_name):
        if self.game.is_game_over():
            return None

        move = self.get_best_move()
        if move is None:
            return None

        getattr(self.game, f"move_{move}")()
        return np.max(self.game.grid)

class TwoPlayer2048:
    def __init__(self, max_turns=500):
        self.game = Game2048()
        self.player1 = MCTSAgent(self.game)
        self.player2 = MCTSAgent(self.game)
        self.max_turns = max_turns
        self.turn = 1
        self.turn_count = 0

    def play_game(self):
        while not self.game.is_game_over() and self.turn_count < self.max_turns:
            player = "Player 1" if self.turn == 1 else "Player 2"
            agent = self.player1 if self.turn == 1 else self.player2
            highest_tile = agent.play_turn(player)

            if highest_tile and highest_tile >= 2048:
                return 1 if self.turn == 1 else 2
            if highest_tile is None:
                break

            self.turn = 3 - self.turn
            self.turn_count += 1
        return None

    def is_game_over(self):
        return self.game.is_game_over()












