from dataclasses import dataclass
from itertools import groupby
from enum import Enum, auto
from more_itertools import consecutive_groups
from copy import deepcopy

from deck import Deck, Card


@dataclass
class Match:
    class Type(Enum):
        Pair = auto()
        Run = auto()

    BONUS_VALUE = 10
    type: Type
    cards: [Card]
    value: int

    def __init__(self, the_type: Type, cards: [Card]):
        assert len(cards) >= 3, "Must provide three or more cards"
        self.type = the_type
        self.cards = cards
        self.value = self._value(the_type, cards)

    def _value(self, the_type: Type, cards: [Card]) -> int:
        if the_type is self.Type.Pair:
            bonus = (len(cards) - 3) * self.BONUS_VALUE
            return cards[0].number + bonus

        elif the_type is self.Type.Run:
            bonus = (len(cards) - 3) * self.BONUS_VALUE
            return max(map(lambda card: card.number, cards)) + bonus

        else:
            raise NotImplementedError()


class Game:
    BOARD_SIZE = 4 * 3

    deck: Deck
    board: [Card]
    score = 0
    can_clear = True

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.board = self.deck.next_cards(self.BOARD_SIZE)
        self.score = 0

    def completed(self) -> bool:
        return not self.moves() and not self.can_clear

    def play(self, match: Match) -> None:
        for card in match.cards:
            self.board.remove(card)
        self.score += match.value
        self.refill_board()

    def clear(self):
        self.can_clear = False
        self.board = self.board[:-4]
        self.refill_board()

    def refill_board(self):
        self.board += self.deck.next_cards(self.BOARD_SIZE - len(self.board))

    def moves(self) -> [Match]:
        return self._matches() + self._runs()

    def _matches(self) -> [Match]:
        test_board = deepcopy(self.board)
        test_board.sort(key=lambda card: card.number)
        matches = []

        for _, match in groupby(test_board, lambda card: card.number):
            match_list = list(match)
            if len(match_list) >= 3:
                matches.append(Match(Match.Type.Pair, match_list))

        return matches

    def _runs(self) -> [Match]:
        test_board = deepcopy(self.board)
        test_board.sort(key=lambda card: card.suit.value)
        matches = []

        of_suits = [list(g) for _, g in groupby(test_board, lambda card: card.suit)]
        for of_suit in of_suits:
            of_suit.sort(key=lambda card: card.number)

            for group in consecutive_groups(of_suit, lambda card: card.number):
                group_list = list(group)
                if len(group_list) >= 3:
                    matches.append(Match(Match.Type.Run, group_list))

        return matches
