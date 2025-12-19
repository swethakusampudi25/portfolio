'''
This file will contain code for performing your comparisons. It should perform (or have a setting that lets us perform) ***ALL*** your comparisons when run. 
We recommend adding the ability to run a subset of the comparisons for testing purposes (as illustrated below). 
'''
from algorithms import TwoPlayer2048
import tkinter as tk
import matplotlib.pyplot as plt

def run_comparisons(total_games=5):
    wins_player1 = 0
    wins_player2 = 0
    no_winner = 0
    max_tiles_p1 = []
    max_tiles_p2 = []
    game_numbers = []

    for game_index in range(total_games):
        print(f"Starting Game {game_index + 1}")
        winner, max_tile_p1, max_tile_p2 = run_single_game_gui(game_index + 1)

        if winner == 1:
            wins_player1 += 1
            max_tiles_p1.append(2048)
            max_tiles_p2.append(max_tile_p2)
        elif winner == 2:
            wins_player2 += 1
            max_tiles_p1.append(max_tile_p1)
            max_tiles_p2.append(2048)
        else:
            no_winner += 1
            max_tiles_p1.append(max_tile_p1)
            max_tiles_p2.append(max_tile_p2)

        game_numbers.append(game_index + 1)

    avg_max_tile_p1 = sum(max_tiles_p1) / len(max_tiles_p1) if max_tiles_p1 else 0
    avg_max_tile_p2 = sum(max_tiles_p2) / len(max_tiles_p2) if max_tiles_p2 else 0

    final_result = (
        "===== 2048 MCTS Agent Comparison Results =====\n"
        f"Total Games Played: {total_games}\n"
        f"Player 1 Wins (Reached 2048): {wins_player1}\n"
        f"Player 2 Wins (Reached 2048): {wins_player2}\n"
        f"No Winner (2048 not reached): {no_winner}\n"
        f"Average Max Tile by Player 1: {avg_max_tile_p1:.2f}\n"
        f"Average Max Tile by Player 2: {avg_max_tile_p2:.2f}\n"
    )

    print("\n" + final_result)
    show_results_popup(final_result)
    plot_graphs(game_numbers, max_tiles_p1, max_tiles_p2, wins_player1, wins_player2, no_winner)

def run_single_game_gui(game_number):
    game = TwoPlayer2048()

    
    window = tk.Tk()
    window.title(f"2048 Game - Game {game_number}")
    grid_labels = [[tk.Label(window, text="", font=("Helvetica", 24), width=4, height=2, borderwidth=2, relief="groove")
                    for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            grid_labels[i][j].grid(row=i, column=j, padx=5, pady=5)

    def update_grid():
        for i in range(4):
            for j in range(4):
                val = game.game.grid[i][j]
                grid_labels[i][j]["text"] = str(val) if val != 0 else ""

    def play_turn():
        if not game.is_game_over() and game.turn_count < game.max_turns:
            player = "Player 1" if game.turn == 1 else "Player 2"
            agent = game.player1 if game.turn == 1 else game.player2
            highest_tile = agent.play_turn(player)
            update_grid()

            if highest_tile and highest_tile >= 2048:
                window.after(1000, window.destroy)
                return
            if highest_tile is None:
                window.after(1000, window.destroy)
                return

            game.turn = 3 - game.turn
            game.turn_count += 1
            window.after(300, play_turn)
        else:
            window.after(1000, window.destroy)

    update_grid()
    window.after(1000, play_turn)
    window.mainloop()

    max_tile_p1 = max(game.game.grid.flatten())
    max_tile_p2 = max(game.game.grid.flatten())
    if game.is_game_over() and max(game.game.grid.flatten()) >= 2048:
        return (1 if game.turn == 2 else 2), max_tile_p1, max_tile_p2
    return None, max_tile_p1, max_tile_p2

def show_results_popup(result_text):
    root = tk.Tk()
    root.title("2048 MCTS Agent Results")
    root.geometry("500x400")

    text_box = tk.Text(root, font=("Arial", 12))
    text_box.pack(expand=True, fill="both")
    text_box.insert("1.0", result_text)
    text_box.config(state="disabled")

    root.mainloop()

def plot_graphs(game_numbers, max_tiles_p1, max_tiles_p2, wins_player1, wins_player2, no_winner):
    plt.figure(figsize=(12, 5))
    plt.plot(game_numbers, max_tiles_p1, marker='o', label="Player 1 Max Tile")
    plt.plot(game_numbers, max_tiles_p2, marker='s', label="Player 2 Max Tile")
    plt.xlabel("Game Number")
    plt.ylabel("Maximum Tile Reached")
    plt.title("Player Maximum Tile Across Games")
    plt.legend()
    plt.grid(True)
    plt.show()

    
    plt.figure(figsize=(8, 5))
    labels = ['Player 1 Wins', 'Player 2 Wins', 'No Winner']
    counts = [wins_player1, wins_player2, no_winner]
    plt.bar(labels, counts, color=['blue', 'green', 'red'])
    plt.ylabel("Number of Games")
    plt.title("Win Counts for Players")
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    run_comparisons()




  
