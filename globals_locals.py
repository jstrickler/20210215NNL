
x = 100
y = 10

def spam():
    name = 'Albert'
    loc = locals()
    print(loc['name'])
    return 42

spam()

class Ham:
    pass

g = globals()
print(g)

print(g['x'], g['y'])
m = "wombat"
print(g['m'])

s = g['spam']
result = s()
print(result)

h = g['Ham']()
print(h)

g['animal'] = 'wombat'
print(animal)

with open('config.txt') as config_in:
    for raw_line in config_in:
        name, value = raw_line.rstrip().split('=')
        g[name.upper()] = value

print(FILE_NAME)
print(USER)

