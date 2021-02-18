#!/usr/bin/env python
import inspect

class Spam:  # <1>
    pass

s = Spam()

def ham(p1: int, p2: str='a', *p3, p4: float, p5: str='b', **p6) -> None:  # <2>
    print(p1, p2, p3, p4, p5, p6)


for thing in (inspect, Spam, ham):
    print("{}: Module? {}. Function? {}. Class? {}".format(
        thing.__name__,
        inspect.ismodule(thing),  # <3>
        inspect.isfunction(thing),  # <4>
        inspect.isclass(thing),  # <5>
    ))

print()

print("Function spec for Ham:", inspect.getfullargspec(ham))  # <6>
print()

print("Current frame:", inspect.getframeinfo(inspect.currentframe()))  # <7>
