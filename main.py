import matplotlib.pyplot as plt

from game import Game
from agent import Agent
from cooperative import Cooperative
from statistics import mean


def main():
    agent_comparison()


def agent_comparison():
    players = 1
    grid_size = (3, 4)
    iterations = 100000
    bin_width = 1

    fig, axs = plt.subplots(3, 1)

    random_agent_scores = [play_game(players, grid_size, Agent.play) for _ in range(iterations)]
    run_first_scores = [play_game(players, grid_size, Agent.play_run_first) for _ in range(iterations)]
    pair_first_scores = [play_game(players, grid_size, Agent.play_pair_first) for _ in range(iterations)]

    max_range = max(pair_first_scores + run_first_scores + random_agent_scores)
    min_range = min(pair_first_scores + run_first_scores + random_agent_scores)

    bins = range(min_range, max_range + bin_width, bin_width)

    axis = axs[0]
    axis.set_title(f'Max Value Random Agent, average = {mean(random_agent_scores)}')
    axis.hist(random_agent_scores, bins=bins, density=True)

    axis = axs[1]
    axis.set_title(f'Run First Agent, average = {mean(run_first_scores)}')
    axis.hist(run_first_scores, bins=bins, density=True)

    axis = axs[2]
    axis.set_title(f'Pair First Agent, average = {mean(pair_first_scores)}')
    axis.hist(pair_first_scores, bins=bins, density=True)

    # Set common labels
    fig.text(0.5, 0.04, 'Game Score', ha='center', va='center')
    fig.text(0.06, 0.5, 'Probability Distribution', ha='center', va='center', rotation='vertical')

    plt.subplots_adjust(hspace=0.5)
    plt.show()


def player_count_vs_grid_size():
    max_players = 4
    players = range(1, max_players + 1)
    grid_sizes = [(3, 3), (3, 4)]
    iterations = 100000

    fig, axs = plt.subplots(len(players), len(grid_sizes))

    for (x, player_count) in enumerate(players):
        for (y, grid_size) in enumerate(grid_sizes):
            scores = [play_game(player_count, grid_size, Agent.play) for _ in range(iterations)]

            bin_width = 1
            bins = range(min(scores), max(scores) + bin_width, bin_width)

            rows, columns = grid_size
            axis = axs[x, y]
            axis.hist(scores, bins=bins, density=True)
            axis.set_title(f'{player_count} Players on {rows}x{columns}')

    fig.tight_layout()
    plt.show()


def play_game(player_count, grid_size: (int, int), agent) -> int:
    """
    Play a single game of scrounge and get the resulting score

    :param agent: The agent that takes in the game state and takes a turn
    :param player_count: The number of players playing the game
    :param grid_size: The size of the game grid
    :return: The score from playing the game
    """
    rows, columns = grid_size
    if player_count == 1:
        game = Game(rows, columns)
    else:
        game = Cooperative(rows, columns, player_count)

    while not game.completed():
        agent(game)

    return game.score


if __name__ == '__main__':
    main()
