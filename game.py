from dataclasses import dataclass
from itertools import groupby
from enum import Enum, auto
from more_itertools import consecutive_groups

from deck import Deck, Card


@dataclass
class Match:
    class Type(Enum):
        Pair = auto()
        Run = auto()

    BONUS_VALUE = 1
    type: Type
    cards: [Card]
    value: int

    def __init__(self, the_type: Type, cards: [Card]):
        assert len(cards) >= 3, "Must provide three or more cards"
        self.type = the_type
        self.cards = frozenset(cards)
        self.value = self._value(cards)

    @staticmethod
    def _value(cards: [Card]) -> int:
        return (len(cards) - 2) * Match.BONUS_VALUE

    def __hash__(self):
        return hash((self.type, self.cards, self.value))

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        return (self.type == other.type and
                self.cards == other.cards and
                self.value == other.value)


class Game:
    rows: int
    columns: int
    deck: Deck
    board: [Card]
    score = 0
    can_clear = True
    _moves: [Match] = []

    def board_size(self):
        return self.rows * self.columns

    def __init__(self, rows: int = 3, columns: int = 3):
        self.rows = rows
        self.columns = columns
        self.deck = Deck()
        self.deck.shuffle()
        self.board = self.deck.draw(self.rows)
        self.score = 0

    def completed(self) -> bool:
        return not self._moves and not self.can_clear

    def play(self, match: Match) -> None:
        for card in match.cards:
            if card in self.board:
                self.board.remove(card)
        self.score += match.value
        self.refill_board()

    def clear_cards(self):
        self.can_clear = False
        cards_to_clear = -(max(self.rows, self.columns))
        self.board = self.board[:cards_to_clear]
        self.refill_board()

    def refill_board(self):
        self.board += self.deck.draw(self.board_size() - len(self.board))
        self._set_moves()

    def moves(self) -> [Match]:
        return self._moves

    def _set_moves(self):
        self._moves = self.matches(self.board) + self.runs(self.board)

    @staticmethod
    def matches(cards: [Card]) -> [Match]:
        """ This function modifies the input array """
        cards.sort(key=lambda card: card.number)
        matches = []

        for _, match in groupby(cards, lambda card: card.number):
            match_list = list(match)
            if len(match_list) >= 3:
                matches.append(Match(Match.Type.Pair, match_list))

        return matches

    @staticmethod
    def runs(cards: [Card]) -> [Match]:
        """ This function modifies the input array """
        cards.sort(key=lambda card: card.suit.value)
        matches = []

        of_suits = [list(g) for _, g in groupby(cards, lambda card: card.suit)]
        for of_suit in of_suits:
            of_suit.sort(key=lambda card: card.number)

            for group in consecutive_groups(of_suit, lambda card: card.number):
                group_list = list(group)
                if len(group_list) >= 3:
                    matches.append(Match(Match.Type.Run, group_list))

        return matches
