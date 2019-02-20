a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print('first four', a[:4])
print('last four', a[-4:])
print('middle two', a[3:-3])

assert a[:5] == a[0:5]

first_twenty_items = a[:20]
last_twenty_items = a[-20:]


#somelist[start:end:stride] lets you take every nth item when slicing a sequence.

a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]

print(odds)
print(evens)

# stride can often introduce unexpected behaviour that can introduce bugs.

#a commpon python trick for reversing a byte string is to slice the string with a stride of -1

x = b'mongoose'
y = x[::-1]
print(y)

# works well for ASCII characters but breaks for unicode characters.
