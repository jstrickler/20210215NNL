fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime"]

for fruit in reversed(fruits):
    print(fruit, end=' ')
print('\n')

rf = reversed(fruits)
print(rf)

ef = enumerate(fruits)
print(ef)
for i, fruit in ef:
    print(i, fruit)

ef = enumerate(fruits)
print(list(ef))
print(list(ef))

uf = [f.upper() for f in fruits]  # list comprehension
print("uf: {}\n".format(uf))

ufgen = (f.upper() for f in fruits)  # generator expression
print("ufgen: {}\n".format(ufgen))
for fruit in ufgen:
    print(fruit)

for i in range(5):
    print(i)
print()

r = range(1000000)
print(r)
x = 0
for i in r:
    x += 1
print(x)



