from datetime import datetime
from functools import wraps
all_function_calls = []

def log_calls(old_func):

    @wraps(old_func)
    def replacement(*args, **kwargs):
        call = old_func.__name__, datetime.now().ctime()
        all_function_calls.append(call)
        return old_func(*args, **kwargs)   # calls original function

    return replacement

@log_calls
def bar():
    print("I am bar")
    return "BAR"

@log_calls
def blah():
    print("I am blah")
    return 100
# bar = foo(bar)
print(bar())
print(blah())
for i in range(10):
    bar()

for func, timestamp in all_function_calls:
    print(timestamp, func)

print(bar.__name__, blah.__name__)
