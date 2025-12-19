'''
This file will contain your the code for your problems. 
'''
import random
import numpy as np

class Game2048:
    def __init__(self):
        self.grid = np.zeros((4, 4), dtype=int)
        self.add_random_tile()
        self.add_random_tile()

    def print_grid(self):
        for row in self.grid:
            print("\t".join(str(tile) if tile != 0 else "." for tile in row))
        print("\n")

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if not empty_cells:
            return
        i, j = random.choice(empty_cells)
        self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def compress_and_merge(self, row):
        new_row = [tile for tile in row if tile != 0]
        merged_row = []
        skip = False
        for j in range(len(new_row)):
            if skip:
                skip = False
                continue
            if j < len(new_row) - 1 and new_row[j] == new_row[j + 1]:
                merged_row.append(new_row[j] * 2)
                skip = True
            else:
                merged_row.append(new_row[j])
        merged_row.extend([0] * (4 - len(merged_row)))
        return merged_row

    def move_left(self):
        new_grid = np.array([self.compress_and_merge(row) for row in self.grid])
        if not np.array_equal(new_grid, self.grid):
            self.grid = new_grid
            self.add_random_tile()

    def move_right(self):
        self.grid = np.flip(self.grid, axis=1)
        self.move_left()
        self.grid = np.flip(self.grid, axis=1)

    def move_up(self):
        self.grid = self.grid.T
        self.move_left()
        self.grid = self.grid.T

    def move_down(self):
        self.grid = np.flip(self.grid.T, axis=1)
        self.grid = np.flip(self.grid, axis=1).T
        self.move_left()
        self.grid = np.flip(self.grid.T, axis=1).T

    def is_game_over(self):
        if np.any(self.grid == 2048):
            return True
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
                if i < 3 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j < 3 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True
