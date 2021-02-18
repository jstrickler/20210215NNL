"""
Provide CardDeck class
"""
import random

class CardDeck:
    """
    Represent a standard deck of playing cards.

    Synopsis:
    deck_obj = CardDeck("Dealername")
    """
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer  # assign to property
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # empty list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):
        return self._dealer

    @dealer.setter
    def dealer(self, value):
        if not isinstance(value, str):
            raise TypeError("Dealer must be a string")
        elif len(value) == 0:
            raise ValueError("Empty dealer name not allowed")
        else:
            self._dealer = value

    def shuffle(self): # instance method
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        """return list of suits"""
        return cls.SUITS

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer}, {len(self)}"

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}("{self.dealer}")'

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

    def __truediv__(self, other):
        size = len(self) // other
        hands = [self._cards[:size]]
        return hands

    @staticmethod
    def doit():
        """Just some function, you know?"""
        return 42
