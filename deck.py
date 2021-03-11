from dataclasses import dataclass
from enum import Enum, auto
import random


class Suit(Enum):
    Spades = auto()
    Hearts = auto()
    Clubs = auto()
    Diamonds = auto()


@dataclass
class Card:
    number: int
    suit: Suit


class Deck:
    cards: [Card]

    def __init__(self):
        self.cards = [Card(number, suit) for number in range(1, 11) for suit in Suit]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def next_cards(self, count: int) -> [Card]:
        remove = min(len(self.cards), count)
        out = self.cards[-remove:]
        self.cards = self.cards[:-remove]
        return out
