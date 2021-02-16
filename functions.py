
def get_message():
    return "Hello, NNL world"

msg = get_message()
print("msg: {}\n".format(msg))

print("This is the message:", get_message())

def spam():
    x = 5

result = spam()
print(result)

def display_message():
    msg = get_message()
    print(msg)

display_message()

def c2f(c_temp):
    f = (1.8 * c_temp) + 32
    return f

fahr = c2f(100)
print(f"{100} C is {fahr} F")




