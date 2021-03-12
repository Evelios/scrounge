from dataclasses import dataclass
from deck import Card
from typing import Optional

from game import Game, Match


@dataclass
class Player:
    card: Optional[Card]


class Cooperative(Game):
    players: [Player]
    num_players: int

    def __init__(self, rows: int = 3, columns: int = 3, players: int = 2):
        super().__init__(rows, columns)
        self.num_players = players
        self.players_draw()

    def play(self, match: Match) -> None:
        for card in match.cards:
            self.players = [
                Player(self.deck.draw_card()) if player.card == card
                else player
                for player in self.players]

        super().play(match)

    def clear_cards(self):
        super().clear_cards()
        self.players_draw()

    def players_draw(self):
        self.players = [Player(self.deck.draw_card()) for _ in range(self.num_players)]

    def _set_moves(self):
        self._moves = self.player_moves() + self.matches(self.board) + self.runs(self.board)

    def player_moves(self) -> [Match]:
        """
        :return: Any moves that are only doable by the player
        """
        moves = []
        for player in self.players:
            if player.card is None:
                continue

            pair = self.pair_with_card(player.card, self.board)
            run = self.run_with_card(player.card, self.board)

            if pair:
                moves.append(pair)

            if run:
                moves.append(run)

        return moves

    @staticmethod
    def pair_with_card(player_card: Card, cards: [Card]) -> Optional[Match]:
        matches = [card for card in cards if player_card.number == card.number]
        matches.append(player_card)

        if len(matches) >= 3:
            return Match(Match.Type.Pair, matches)

        return None

    @staticmethod
    def run_with_card(player_card: Card, cards: [Card]) -> Optional[Match]:
        card_distances = [(card, abs(player_card.number - card.number)) for card in cards if
                          card.suit == player_card.suit]
        card_distances.sort(key=lambda x: x[1])  # Sort by distance

        run = [player_card]
        for (card, distance) in card_distances:
            if any(map(lambda run_card: run_card.number - card.number == 1, run)):
                run.append(card)

        if len(run) >= 3:
            return Match(Match.Type.Run, run)

        return None
