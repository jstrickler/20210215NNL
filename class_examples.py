from datetime import date

# instance = CLASS(param, param, ...)
d = date(2020, 9, 13)
print(d, type(d))
print(d.ctime())

colors = list()
colors.append('blue')
colors.append('red')

n1 = [1, 2, 3]
n2 = list([8, 99, 35])

#  getter/setter  accessor/mutator

class Dog:  # default base class is 'object'
    def __init__(self, dog_name):  # "constructor"
        self._name = dog_name

    @property  # decorator
    def name(self):  # getter property
        return self._name

    @name.setter
    def name(self, dog_name):  # setter property
        if isinstance(dog_name, str):
            self._name = dog_name
        else:
            raise TypeError("Dog name must be a string")

    def bark(self):
        print("Woof! Woof!, self is", self)

    def get_name(self):  # getter method
        return self._name

    @property
    def spam(self):
        return self._spam

    @spam.setter
    def spam(self, value):
        self._spam = value

    @property
    def ham(self):
        return self._ham

class Cat:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    d1 = Dog('Nellie')  # create new object
    d2 = Dog('Andy')
    d1.bark()  # Dog.bark(d1) # same!!
    d2.bark()
    print(d1.name)
    print(d1.get_name())
    print(d1._name)

    c1 = Cat("Bonnie")
    print(c1.name)

    d1.name = 'Little Bear'
    print(d1.name)

    try:
        d1.name = 123.456
        print(d1.name)
        print(d1.name.upper())
    except TypeError as err:
        print(err)






