import os
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

fp1 = r'\foo\bar\blah\\'
a = 'DATA'
b = 'parrot.txt'
file_path = os.path.join(a, b)
print(file_path)

fp2 = '/foo/bar/blah/'

s = "41\u00B0 C"
print(s)
print(len(s))

print("\U0001F92F")

b = s.encode()
print(b)
print(len(b))
print(b[0], b[-1])

x = "hello"
y = x.encode()  # string -> UTF-8 bytes
print(x, y)
print(x[0], y[0])

print(b.decode())  # UTF-8 bytes -> string


