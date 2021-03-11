from game import Game
import random


def main():
    games = [play_game() for _ in range(1000)]


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


if __name__ == '__main__':
    main()
