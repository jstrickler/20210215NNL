fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

def ignore_case(original_string):
    sort_key = original_string.lower()
    print("Comparing {} as {}".format(original_string, sort_key))
    return sort_key

f3 = sorted(fruits, key=ignore_case)
print("f3: {}\n".format(f3))

f4 = sorted(fruits, key=len)
print("f4: {}\n".format(f4))

def custom_sort(fruit):
    return len(fruit), fruit.lower()

f5 = sorted(fruits, key=custom_sort)
print("f5: {}\n".format(f5))
print("-" * 60)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print("-" * 60)

def by_last_name(p):
    print("Sorting {} by {}".format(p, (p[1], p[0])))
    return p[1], p[0]  # last name, first name

for person in sorted(people, key=by_last_name):
    print(person)
print("-" * 60)

for person in sorted(people, key=lambda p: (p[3])):
    print(person)
print("-" * 60)


airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

for code, name in sorted(airports.items()):
    print(code, name)
print()

for code, name in sorted(airports.items(), key=lambda a: (a[1], a[0])):
    print(code, name)
print()

results = sorted(airports.items(), key=lambda a: (a[1], a[0]))
print(results, '\n')

junk = 'wombat', 'sea lion', 'wildebeest', 'ape'
print(sorted(junk))

results = sorted(airports)
print(results)

def times_five(x):
    return x * 5

#  lambda x: x * 5

def doit(func, value1, value2):
    return func(value1, value2)


x = doit(lambda x, y: x * y, 5, 10)
print(x)

def myfunc(a, b):
    return a * b

x = doit(myfunc, 8, 9)
print(x)

#  min() max() sorted()






