
class Spam():
    def __init__(self, how):
        self.how = how

    def __call__(self):
        print("Making {} Spam".format(self.how))

    def bark(self):
        print("woof woof")

s = Spam('baked')
s()
s.bark()

