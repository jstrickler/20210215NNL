import pytest
from carddeck import CardDeck

@pytest.fixture
def deck():
    return CardDeck("TestUser")

def test_drawing_card_decrements_deck(deck):
    old_len = len(deck)
    _ = deck.draw()
    assert len(deck) == (old_len - 1)

def test_shuffle_changes_order(deck):
    before = list(deck.cards)
    deck.shuffle()
    after = list(deck.cards)
    assert before != after

def test_invalid_name_raises_error():
    with pytest.raises(TypeError):
        _ = CardDeck(123.456)
    with pytest.raises(ValueError):
        _ = CardDeck("")

