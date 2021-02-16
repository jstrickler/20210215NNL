
def spam(a, b, c, *, d, e, f):
    print(a, b, c, d, e, f)

spam(1, 2, 3, f=4, d=5, e=99)
print()

def ham(a, b, *c):
    print(a, b, c)

def findit(*, search_term, file_name):
    pass

findit(file_name="wombats.txt", search_term="marsupial")



ham(1, 2, 3)
ham(1, 2)
ham(1, 2, 3, 4, 5, 6, 7, 8, 9)

def config(**values):
    print(values)

config(animal="wildebeest", college="UCLA", file_name="boulder.txt")

def generic_thing(*args, **kwargs):
    pass

def doit(file_name, count=1):
    print(file_name, count)

doit("foo.txt")
doit("bar.txt", 42)


