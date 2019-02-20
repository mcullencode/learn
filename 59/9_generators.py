# problem with list comprehensions is that they may create a whole new list containng one item for each value in
#inout sequence. fine for small inputs, but for large inputs could cause pc to crash.
# e.g. if you want to read a file and return the number of characters on each line, comprehension would require holding the length
# of every line of the file in memory. if file large or never ending socket, would crash.
# list comp below

#value = [len(x) for x in open('tmp/y_file.txt')]
#print(value)

## >>> [100, 57, 15, 12, 75, 5]

# generator exp dont materialize the whole output sequence when theyre run, instead they evaluate to an iterator that yields one item at a
# time from the expression.

#it = (len(x) for x in open('/tmp/my_file.txt'))

#print(next(it))
#print(next(it))

# >> 100
# >> 57

#another powerful outcome of generators is that they can be composed together.
# below the iterator returned by the generator is used as input for another generator expression

#roots = ((x, x**0.5) for x in it)