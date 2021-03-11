from deck import Deck


def test_deck_removal():
    deck = Deck()
    deck.next_cards(10)

    assert len(deck.cards) == 30


def test_deck_over_count():
    deck = Deck()
    cards = deck.next_cards(50)

    assert len(deck.cards) == 0
    assert len(cards) == 40
