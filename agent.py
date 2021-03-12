import random

from game import Game, Match


class Agent:
    @staticmethod
    def play(game: Game) -> None:
        """
        Modifies the current game state to take an action
        :param game: The current game state
        """
        moves = game.moves()

        if len(moves) == 0:
            game.clear_cards()
            return

        random.shuffle(moves)
        moves.sort(key=lambda match: match.value)
        game.play(moves[0])

    @staticmethod
    def play_run_first(game: Game) -> None:
        """
        Modifies the current game state to take an action
        :param game: The current game state
        """
        moves = game.moves()

        if len(moves) == 0:
            game.clear_cards()
            return

        moves.sort(key=lambda match: match.value + (match.type == Match.Type.Pair))
        game.play(moves[0])

    @staticmethod
    def play_pair_first(game: Game) -> None:
        """
        Modifies the current game state to take an action
        :param game: The current game state
        """
        moves = game.moves()

        if len(moves) == 0:
            game.clear_cards()
            return

        moves.sort(key=lambda match: match.value + (match.type == Match.Type.Pair))
        game.play(moves[0])
