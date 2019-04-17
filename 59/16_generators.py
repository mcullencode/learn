# the simplest choice for functions that produce a sequence of results is to return a list of items. e.g.
# say you want to find the index of every word in a string. here i accumulate results in a list using the append
# method and return it at the end of a function.

def index_word(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

# this works as expected for some sample input

address = 'Four score and seven years ago...'
#result = index_word(address)

print(result)

#the first problem is that the code is a bit dense.  each time a new result is found, i call the append method.
# the method calls bulk (result.append) deemphasizes the value being added to the list (index + 1) . there is one line for creating
# the result list and another for returning it. the function body cotains 130 characters without whitespace but only 75 characters
# are important. a better way to write this functon is using a generator. generators are functions that use yield expressions.
#  when called generator functions do not actually run, but instead immediately return an iterator. with each cal to the next
# yield expression. Each value passed to the yield by the generator will be returned by the iterator to the caller.
# here we define a generator function that produces the same results as before:

def index_word_iter(text):
    if text:
        yield 0
        for index, letter in enumerate(text):
            if letter == ' ':
                yield index + 1

result = list(index_words_iter(address))

# the iterator returned by the generator call can easily be converted to a list by passing it to the list built-in function (item 9)

#the problem with index_words is that it requires all results to be stored in the list before being returned. for huge inputs this is
#cpu heavy.

# here we define a generator that streams input from a file one line at a time and yields outputs one word at a time. the working
# mmeory for this function is bounded to the maximum length of one line of input.

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset



