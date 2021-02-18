#!/usr/bin/env python
import threading
import random
import time

def doit(num):  # <1>
    time.sleep(random.randint(1, 3))
    print("Hello from thread {}".format(num))

for i in range(10):
    t = threading.Thread(target=doit, args=(i,))  # <2>
    t.start()  # <3>

print("Done.")  # <4>

# myfiles = ['a', 'b', 'c']
# for file_name in myfiles:
#     t = threading.Thread(target=process_file, args=(file_name,))
