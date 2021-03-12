from game import Game


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

        moves.sort(key=lambda match: match.value)
        game.play(moves[0])
