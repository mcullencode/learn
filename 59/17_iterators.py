#when a function takes a list of objects as a parameter, its often important to iterate over that list multiple times.
# e.g. analyse tourism numbers for US state of texas. data set is the number of visitors to each city (millions per year)
# yet you want a % of overall tourism each city recevies

# need a normalization function. sums the inputs to determine total number of tourists per year, then divides ech citys individual visitor count
#by total to find that citys controbutions to the whole

def normalise(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)

    return result

visits = [15, 35, 80]
percentages = normalise(visits)
print(percentages)

# to scale this up, need to read data from a file that contains ever city in texas. can use a generator for this

def read_visits(data_path)

    with open(data_path) as f:
        for line in f:
            yield int(line)

#surprisingly, calling normalize on the generators return value produces no results.
#the cause of this behaviour is that an iterator only produces results a single time. if you iterate over an iterator
#  or generator that has already raised a StopIteration exception, you wont get any results the second time around.

#it = read_visits('/tmp/my_numbers.txt')
#print(list(it))
#print(list(it))

#this returns [15, 35, 80]
#then []

# you also wont get any errors when you iterate over an already exhausted iterator. for loops, list constructor and many other funcions
#throughout python, they expect the StopIteration exception to be reaised during normal operation. these functions cant
# tell the difference between an iterator that has no output and an iterator that had output and is now exchausted.

#to solve this, you can explicitly exhaust an input iterator and keep a copy of its entire contents in a list. You can then
# iteratoe over the list version of the data as many times as you need to. heres same function as before but it defensively copies the input iterator.

def normalise_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100*value/total
        result.append(percent)
    return result

#this function works correctly on a generators return value. however the problem with this approach is that the copy of the
# input iterators contents could be large. copying the iterator could cause your prgram to run out of memory.
#one way around this is to accept a function that returns a new iterator each time its called.

def normalize_func(get_iter)
    total = sum(get_iter())
    result = []
    for value in get_iter()
        percent = 100 * value / total
        result.append(percent)
    return result

#to use normalize_func you can pass in a lambda expression that calls the generator and produces a ne iterator each time.

percentages = normalize_func(lambda: read_visits(path))

#though it works, having to pass a lambda function like this is clumsy. The better way to achieve the same result is to
# provide a new container class that implements the iterator protocol.

#CONTAINER CLASS
#the iterator protocol is how Python for loops and related expressions traverse the contents of a container type.
# when python sees a statement like for x in foo, it will actually call iter(foo). The iter built in function calls
# the foo.__iter__ special method in turn. The __iter__ method must return an iterator object (ehich itself implements the
# __next__ special method). Then the for loop repeatedly calls the next built-in function on the iterator object until
# it's exhausted (and raises a StopIteration exception).

#it sounds complicated but practically speaking you can achieve all of this behaviour for your classes by implementing __iter__ method
# as a generator. Here, i define an iterable container class that reads the files containing tourism data.

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

#this new container type works correctly when passed to the original function without any modifications.

visits = ReadVisits(path)
percentages1 = normalise(visits)
print(percentages1)

# this works because the sum method in normalize will call ReadVisits.__iter__ to allocate a ew iterator object. The for
# loop to normalise the numbers will also call __iter__ to allocate a second iterator object. Each of those iterator
# will be advanced and exhausted independently, ensuring that each unique iteration sees all of the input data values.
# The only downside of this approach is that it reads the input data multiple times.

#now that w know how containers like ReadVisits work, you can write your functions to ensure that parameters arent just iterators.
# The protocol states that when an iterator is passed to the iter built-in func, iter will return the iterator itself. In contrast,
# when  a container type is passed to iter, a new iterator object will be returned each time. Thus, you can test an input value for
# this behaviour and raise a TypeError to reject iterators.






