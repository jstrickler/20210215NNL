from jokerdeck import JokerDeck

def test_joker_deck_has_jokers():
    j = JokerDeck("TestUser")
    assert ('1', 'Joker') in j.cards
    assert ('2', 'Joker') in j.cards
