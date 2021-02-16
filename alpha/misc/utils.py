"""
General utilites for Admiral Rancor
"""

from re import search as seek

ANIMAL = "wombat"

def main():
    print("Hi Mom!!")
    toast()
    spam()

def spam():
    """
    Fatty pig meat
    """
    print("Hello from spam()")


def _ham():
    """
    Helper function
    """
    print("    and _ham()")


def toast():
    """
    Delicious broiled bread.
    """
    print("Hello from toast()")
    _ham()

# print("MY NAME IS:", __name__)

if __name__ == '__main__':  # if run as script and NOT imported as module
    main()