from deck import Card, Suit
from game import Game, Match


def test_match():
    cards = [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs, Suit.Hearts]]
    game = Game()
    game.board = cards

    expected = [Match(Match.Type.Pair, cards)]

    assert set(game.moves()) == set(expected)


def test_run():
    cards = [Card(number, Suit.Spades) for number in range(3, 6)]
    game = Game()
    game.board = cards

    expected = [Match(Match.Type.Run, cards)]

    assert set(game.moves()) == set(expected)
