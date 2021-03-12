import matplotlib.pyplot as plt

from game import Game
from agent import Agent
from cooperative import Cooperative


def main():
    max_players = 4
    players = range(1, max_players + 1)
    grid_sizes = [(3, 3), (3, 4)]
    iterations = 100000

    fig, axs = plt.subplots(len(players), len(grid_sizes))

    for (x, player_count) in enumerate(players):
        for (y, grid_size) in enumerate(grid_sizes):
            scores = [play_game(player_count, grid_size) for _ in range(iterations)]

            bin_width = 1
            bins = range(min(scores), max(scores) + bin_width, bin_width)

            rows, columns = grid_size
            axis = axs[x, y]
            axis.hist(scores, bins=bins, density=True)
            axis.set_title(f"{player_count} Players on {rows}x{columns}")

    fig.tight_layout()
    plt.show()


def play_game(player_count, grid_size: (int, int)) -> int:
    """
    Play a single game of scrounge and get the resulting score

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
        Agent.play(game)

    return game.score


if __name__ == '__main__':
    main()
