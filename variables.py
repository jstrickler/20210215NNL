import copy

x = 5
print(x, x * 10)
print(x, type(x), id(x))

y = x
print(y, type(y), id(y))

x = 10
print(x, y)
print(id(x), id(y))

#  int (C long) float (C long? double)
print(x * 12.0)
print(x * 8)

y = 42

values = [1, 2, 3, [4, 5, 6]]
vcopy = values
vcopy.append(100)
print(values, vcopy)

vcopy = values  # alias, not copy
truecopy = list(values)  # shallow copy
truecopy.append(1000)
print(values, vcopy, truecopy)
truecopy[3].append("wombat")
print(values, vcopy, truecopy)

deepcopy = copy.deepcopy(values)
deepcopy[3].append("wolverine")
print(values, vcopy, truecopy)
print(deepcopy)

data = [1, 2, 3]   # original object
data_alias = data   # alternate name of original object
data_shallow = list(data)  # new object that copies top-level values of original
data_deep = copy.deepcopy(data)  # new object that recursively copies all nested values

d1 = {'a': 5, 'b': 8, 'c': [1, 2, 3]}
d2 = d1  # alias
d3 = dict(d1) # new object (shallow)
d4 = copy.deepcopy(d1) # new object (recursive)
d1['c'].append(42)
print(d1, d2, d3, d4)
d1['d'] = "Wombat"
print(d1, d2, d3, d4)

#  a-z A-Z 0-9 _

for _ in range(5):
    print(_)
    print("Python is great!")

x = None  # nil, null, etc


print(values[0])

colors = ['red', 'purple', 'ecru', 'mauve', 'chartreuse']

print(colors[0], colors[4], colors[2], colors[-1])
animal = 'wombat'
print(animal[0], animal[3], animal[-1])


























