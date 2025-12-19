from problems_connect4 import Connect4
from algorithms_connect4 import MCTSAgent, MinimaxAgent
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Connect 4: MCTS Agent vs Minimax Agent")

    game = Connect4()
    agent1 = MCTSAgent(simulations=500)
    agent2 = MinimaxAgent(depth=3)

    agents = {1: agent1, 2: agent2}

    game.initialize_display()
    game.update_display()

    while not game.check_winner() and not game.is_full():
        current_agent = agents[game.current_player]
        move = current_agent.get_move(game)
        game.make_move(move)
        print(f"Player {game.current_player} placed at column {move}")
        game.update_display()

        if game.check_winner() or game.is_full():
            break

        game.switch_player()

    plt.ioff()
    winner = game.check_winner()

    if winner == 1:
        print("MCTS Agent wins!")
        game.ax.text(1.5, 7, "MCTS Agent Wins!", fontsize=20, color='green')
    elif winner == 2:
        print("Minimax Agent wins!")
        game.ax.text(1.5, 7, "Minimax Agent Wins!", fontsize=20, color='green')
    else:
        print("It's a draw!")
        game.ax.text(2, 7, "Draw!", fontsize=20, color='green')

    game.fig.canvas.draw()
    plt.show(block=True)
