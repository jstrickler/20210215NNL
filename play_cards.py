from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Abigail")
print(d1)
print(type(d1))
print(d1.dealer)

d1.shuffle()
print(d1.cards)
for _ in range(5):
    print(d1.draw())
print()

print(d1.get_suits())
print(CardDeck.get_suits())

j1 = JokerDeck("Albert")
print(j1, type(j1))
j1.shuffle()
print(j1.draw())
print(j1.cards)
j1.sing()
j1.roar()
print(JokerDeck.mro())

print(len(d1))
print(len(j1))

print(d1)  # print(str(d1))
#      print(CardDeck.__str__(d1)
print(j1)

print("repr:", repr(d1))

d = d1 + j1
print(d)

d2 = CardDeck("Paula")
hands = d2 / 4
print(hands)

#   path / path
