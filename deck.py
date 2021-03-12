from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
import random


class Suit(Enum):
    Spades = auto()
    Hearts = auto()
    Clubs = auto()
    Diamonds = auto()


@dataclass(frozen=True, order=True)
class Card:
    number: int
    suit: Suit


class Deck:
    LOWEST_VALUE = 1
    HIGHEST_VALUE = 10
    cards: [Card]

    def __init__(self):
        all_values = range(self.LOWEST_VALUE, self.HIGHEST_VALUE + 1)
        self.cards = [Card(number, suit) for number in all_values for suit in Suit]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        if not self.cards:
            return None
        return self.cards.pop()

    def draw(self, count: int = 1) -> [Card]:
        remove = min(len(self.cards), count)
        out = self.cards[-remove:]
        self.cards = self.cards[:-remove]
        return out
