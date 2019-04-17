# accepting positional arguments can make a function call more clear and remove visual noise. These are sometimes called *args.
# for example, say you want to log some debug information. with a fixed number of arguments, you would need a function that takes a
# message and a list of values

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ' ,  '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1,2])
log('Hi there', [])

# but here we have to pass an empty list when there are no values. would be better to leave out the second argument entirely.
# This can be done in python by prefixing the last positional parameter name with *. The first parameter for the log message is
# required, whereas any number of subsequent positional arguments are optional. The function body doesnt need to change, only the call

def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ' ,  '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log2('My numbers are', [1, 2])
log2('Hi there')

#if you already have a list and want to call a variable argument function like log, you can do this by useing the * operator:
# this instructs python to pass items from the sequence as positional arguments

favorites = [7, 33, 99]
log2('favorite colours', *favorites)

#two problems with accepting a variable number of positional arguments:

#first is that the variable arguments are always turned into a tuple before they are passed to your function. This means that
# if the caller of your function uses the * operator on a generator, it will be iterated until its exhausted. The resulting
# tuple will include every value from the generator, which could consime a lot of memory and cause program to crash.

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)

#functions that accept *args are best for situations where you know the number of inputs in the argument list will be reasonably small.
# its ideal for function calls that pass many literals or variable name together. It's primarily for the convenience of the programmer
# and the reliability of the code.

# the second issue with *args is that you cant add new positional arguments to your function in the future without migrating every caller.
# If you try to add a positional argument in the front of the argument list, existing callers will subtly break if they arent updated.

def log3(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

log3(1, 'favorites', 7, 33)
log3('Favorite numbers', 7, 33)

#the problem here is that the second call to log used 7 as the message parameter because a sequence qrgument wasnt given.
# bugs like thisare hard to track down because the code still runs without raising exceptions
