import random
import matplotlib.pyplot as plt

from game import Game


def main():
    games = [play_game() for _ in range(10000)]
    plot(games)


def play_game() -> int:
    game = Game()

    while not game.completed():
        moves = game.moves()

        if moves:
            move = random.choice(moves)
            game.play(move)
        else:
            game.clear()

    return game.score


def plot(games: [int]) -> None:
    bin_width = 1
    bins = range(min(games), max(games) + bin_width, bin_width)
    plt.hist(games, bins=bins, density=True)
    plt.xlabel = "Game Score"
    plt.ylabel = "Percentage"
    plt.show()


if __name__ == '__main__':
    main()
