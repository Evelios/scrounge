from cooperative import Cooperative, Player
from game import Match
from deck import Suit, Card


def test_match():
    cards = [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs]]
    game = Cooperative()
    game.board = cards
    game.players = [Player(Card(7, Suit.Hearts))]

    expected = [Match(
        Match.Type.Pair,
        [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs, Suit.Hearts]]
    )]

    assert game.moves() == expected


def test_run():
    cards = [Card(number, Suit.Spades) for number in range(3, 5)]
    game = Cooperative()
    game.board = cards
    game.players = [Player(Card(5, Suit.Spades))]

    expected = [Match(
        Match.Type.Run,
        [Card(number, Suit.Spades) for number in range(3, 6)]
    )]

    assert game.moves() == expected


def test_match_extra_from_player():
    cards = [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs, Suit.Diamonds]]
    game = Cooperative()
    game.board = cards
    game.players = [Player(Card(7, Suit.Hearts))]

    player_match = [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs, Suit.Diamonds, Suit.Hearts]]
    board_match = [Card(7, suit) for suit in [Suit.Spades, Suit.Clubs, Suit.Diamonds]]

    expected = [Match(Match.Type.Pair, match) for match in [player_match, board_match]]

    assert game.moves() == expected


def test_run_extra_from_player():
    cards = [Card(number, Suit.Spades) for number in range(3, 6)]
    game = Cooperative()
    game.board = cards
    game.players = [Player(Card(6, Suit.Spades))]

    player_match = [Card(number, Suit.Spades) for number in range(3, 7)]
    board_match = [Card(number, Suit.Spades) for number in range(3, 6)]

    expected = [Match(Match.Type.Run, match) for match in [player_match, board_match]]

    assert game.moves() == expected
