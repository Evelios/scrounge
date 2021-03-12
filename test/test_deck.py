from deck import Deck


def test_deck_removal():
    deck = Deck()
    deck.draw(10)

    assert len(deck.cards) == 30


def test_deck_over_count():
    deck = Deck()
    cards = deck.draw(50)

    assert len(deck.cards) == 0
    assert len(cards) == 40
