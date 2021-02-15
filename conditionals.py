import re

value = 56

if value > 75:
    print("wombat")
elif value > 50:
    print("kangaroo")
    print("wallaby")
elif value > 25:
    print("kookaburra")
else:
    print("cane toad")

#  == != > < >= <= is

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(id(a), id(b), id(c))
print(a is b, a is c)
print(a == b, a == c)

if a is None:
    pass

if a is not None:
    pass

x = 5
del x

m = None

a = 'wombat'

m = re.search('b.t', a)
if m is not None:
    print(m.group())

m = re.search('brizz', a)
if m:
    print(m.group())
else:
    print("NOT FOUND")



