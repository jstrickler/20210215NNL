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
airports['ALB'] = 'Albany'
airports['PIT'] = "Pittsburgh"
for code in 'RDU', 'PIT', 'LAX', 'QQQ':
    print(code, airports.get(code, 'NOT FOUND'))
airports['IAD'] = 'Washington Dulles'
print("-" * 60)

for code, name in airports.items():
    print(code, name)
print("-" * 60)

for code, name in sorted(airports.items()):
    print(code, name)
print("-" * 60)