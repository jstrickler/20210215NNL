list1 = []  # empty list
list1.append('blue')
list1.append('red')
list1.append('yellow')
list1.append(['purple', 'pink'])
list1.extend(['orange', 'green', 'mauve'])
print(list1)
a = list1.pop() # same as list1.pop(-1)
b = list1.pop(1)
print(a, b)
print(list1)
list1.insert(2, 'navy blue')
print(list1)

list1[1:2] = ['black', 'white', 'brown']
print(list1)

#    SEQ[START:STOP:STEP]
list1.remove('navy blue')
print(list1)
print(list1.count('green'))
del list1[4]
print(list1)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
print(food.count('spam'), food.count('eggs'))
print(all([f == 'spam' for f in food]))
print(any((f == 'eggs' for f in food)))

#  all(iterable)
#  any(iterable)
a = [f == 'spam' for f in food]
b = (f == 'spam' for f in food)
print(a)
print(b)

name = "Bob"
values = [5, 8, 9, 0]
print(any(values))
print(all(values))






