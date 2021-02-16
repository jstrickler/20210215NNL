
x = 5  # GLOBAL x
y = 10  # GLOBAL variables
if x < 20:
    y = 42

print(y)

def spam():
    x = 10000  # LOCAL x
    name = "Fred"  # LOCAL variable   # __name__
    print("in spam(): x is", x)
    print("in spam(): m is", m)
    print(name)
    return name

m = "marmot"

try:
    result = spam()
except ValueError as err:
    print(err)

print("name is", result)
print("in main: x is", x)
#  local -> nonlocal -> global -> builtin