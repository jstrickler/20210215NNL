
class Dog:
    def bark(self):
        print("woof woof")

d1 = Dog()
d2 = Dog()
d2.bark()

Cat = type('Cat', (), {'meow': lambda s: print("meow meow"), 'purr': lambda s: print('prrrrrrrp')})

# this is a block comment
# and there might be multiple lines
c1 = Cat()
c2 = Cat()
c1.meow()  # cats don't bark
c2.purr()

# rope???
# pep8

