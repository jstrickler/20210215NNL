from carddeck import CardDeck

class Thing:
    def roar(self):
        print("rowwwrrrrrrr")

class JokerDeck(CardDeck, Thing):
    def _make_deck(self):
        super()._make_deck()
        for i in '1', '2':
            joker = i, 'Joker'
            self._cards.append(joker)

    def sing(self):
        print("la la la la")