from problems_connect4 import Connect4
from algorithms_connect4 import MCTSAgent, MinimaxAgent
import matplotlib.pyplot as plt

def play_game(agent1, agent2):
    game = Connect4()
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

    return winner

def compare_agents_single_game():
    agent1 = MCTSAgent(simulations=500)
    agent2 = MinimaxAgent(depth=3)

    winner = play_game(agent1, agent2)

   
    mcts_wins = 0
    minimax_wins = 0
    draws = 0

    if winner == 1:
        mcts_wins += 1
    elif winner == 2:
        minimax_wins += 1
    else:
        draws += 1

    print("\nResult after 1 game:")
    print(f"MCTS Agent Wins: {mcts_wins}")
    print(f"Minimax Agent Wins: {minimax_wins}")
    print(f"Draws: {draws}")

    plot_results(mcts_wins, minimax_wins, draws)

def plot_results(mcts_wins, minimax_wins, draws):
    labels = ['MCTS Wins', 'Minimax Wins', 'Draws']
    values = [mcts_wins, minimax_wins, draws]
    colors = ['red', 'blue', 'grey']

    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, values, color=colors)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=12)

    plt.title('Result of Single Game', fontsize=16)
    plt.xlabel('Result')
    plt.ylabel('Count')
    plt.ylim(0, 1.5)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show(block=True)

if __name__ == "__main__":
    compare_agents_single_game()
