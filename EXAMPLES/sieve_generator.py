#!/usr/bin/env python

def next_prime(limit):
    flags = set()  # <1>

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # <2>
        yield i, j, 'spam'  # <3>  # like EXPR in generator expression (EXPR for ...)

np = next_prime(100)  # <4>
print("What is np?", type(np))
for prime, largest_multiple, whatever in np:  # <5>
    print(prime, end=' ')
