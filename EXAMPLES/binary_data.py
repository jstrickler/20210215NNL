#!/usr/bin/env python

from struct import Struct

values = 7, 6, 42.3, b'Guido' # <1>

demo = Struct('iif10s')  # <2>

print("Size of data: {} bytes".format(demo.size)) # <3>

binary_stream = demo.pack(*values) # <4>
print(binary_stream)

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # <5>
str1 = raw_bytes.decode().rstrip('\x00')  # <6>

print(raw_bytes)
print(int1, int2, float1, str1)
print(int1, int2, round(float1, 2), str1)

with open('../DATA/mystery', "rb") as mystery_in:
    data = mystery_in.read(10)
    # data = mystery_in.read()  # read all bytes
