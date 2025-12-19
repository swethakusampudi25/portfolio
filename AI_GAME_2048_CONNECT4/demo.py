import tkinter as tk
from algorithms import TwoPlayer2048

def run_game_with_gui():
    game = TwoPlayer2048()
    window = tk.Tk()
    window.title("2048 Game - Agent Playing")

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
                print(f"\n{player} WINS by reaching 2048!\n")
                window.after(2000, window.destroy)
                return
            if highest_tile is None:
                window.after(2000, window.destroy)
                return

            game.turn = 3 - game.turn
            game.turn_count += 1
            window.after(500, play_turn)
        else:
            print("Game Over!! No player reached 2048.\n")
            window.after(2000, window.destroy)

    update_grid()
    window.after(1000, play_turn) 
    window.mainloop()

if __name__ == "__main__":
    run_game_with_gui()
