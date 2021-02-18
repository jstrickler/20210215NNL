#!/usr/bin/env python

import timeit

test_code_one = '''
values = []
for i in range(10000):
    values.append(i)
'''  # <2>
test_code_two = '''
values = []
i = 0
while i < 10000:
    values.append(i)
    i += 1
'''  # <2>

t1 = timeit.Timer(test_code_one)  # <3>
t2 = timeit.Timer(test_code_two)  # <3>

print("test one:")
print(t1.timeit(1000))  # <4>
print()

print("test two:")
print(t2.timeit(1000))  # <4>
print()
