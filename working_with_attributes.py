from carddeck import CardDeck

d = CardDeck("Priscilla")

print(dir(d))

print(d.dealer)
print(getattr(d, 'dealer'))

if hasattr(d, 'to_json'):
    getattr(d, 'to_json')()

# getattr() hasattr() setattr() delattr()

def get_ucdealer(self):
    return self.dealer.upper()

setattr(CardDeck, 'get_ucdealer', get_ucdealer)


print(d.get_ucdealer())

