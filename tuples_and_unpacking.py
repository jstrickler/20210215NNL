person = "Bill", "Gates", "Microsoft", "1955-10-28"
# x = obj, obj, ....
print(person)
print(person[0], person[1], len(person), person.count('Bill'))

# person[0]  person[1]  person[2]  person[3]
first_name, last_name, product,    dob       = person   # unpack

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
print(airports.items(), '\n')
for code, name in airports.items():
    # code, name = next(airports.items())
    print(code, name)
print()

for t in airports.items():
    code, name = t
    print(code, name)
print()

colors = ['blue', 'purple', 'orange']

for i, color in enumerate(colors):
    print(i, color)
print()
print(list(enumerate(colors)))

data = [('a', 5, 19, 6), ('m', 9, 3), ('c', 7)]
for letter, *numbers in data:
    print(letter, numbers)
print()

values = 'abcdef'  # ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

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

for first_name, last_name, _, dob in people:
    print(first_name, last_name, dob)
print()