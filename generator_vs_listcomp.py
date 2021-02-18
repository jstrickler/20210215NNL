import timeit

setup = """
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]
"""

code1 = """
f1 = [f.upper() for f in fruits]
target = []
for fruit in f1:
    target.append(fruit)
"""

code2 = """
f1 = (f.upper() for f in fruits)
target = []
for fruit in f1:
    target.append(fruit)
"""

t1 = timeit.Timer(code1, setup)
t2 = timeit.Timer(code2, setup)

NUM_RUNS = 1000
print(t1.timeit())
print(t2.timeit())


