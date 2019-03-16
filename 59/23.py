#here we define a hook that logs each time a key is mising and returns 0 for default value
from collections import defaultdict

def log_missing():
    print('Key added')
    return 0

#given an initial dictionary and a set of desired increments i can cause the log_missing function
# to run and print twice for 'red' and 'orange'

current = { 'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

print(increments)
result = defaultdict(log_missing, current)
print('Before', dict(result))
for key, amount in increments:
    result[key] += amount
print('After:', dict(result))

#this exercise adds increments the the defaultdict which contains current. The log_mising makes APIs easy to build and test
# because it separates side effects from deterministic behaviour. I.e if a value was missing from increments, 'log_missing'
# would add 0 so there would be no error produced.

#below we define a helper function that uses such a closure as the default value hook (from Item 15)

def increment_with_report(current, increments):
    added_count = 0

    # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong
    # to the inner function. Use the keyword nonlocal to declare that the variable is not local.

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


result, added_count = increment_with_report(current, increments)
print(result)
print(added_count)

#running yhis function produces the expected result (2), even though defaultdict has no idea that the missing hook maintians state.
#this is another benefit of accepting simple function for interfaces. It's easy to add functionality later by hiding state in a closure

# Another approach is to define a small class that encapsulates the state you want to track.

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

# in other languages you might expect  that now defaultdict would have tobe modified to accommodaye yje omyergave of COuntMissing.
# but in python, thanks to first class functions, you can regerence the CountMissing.missing method directly on an objet and
#pass it to defaultdict as the default value hook. Its trivial to have a method satisfy a function interface

counter = CountMissing()
result = defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2

#to clarify this situation, Python allows classes to define the __call_ special method. __call__ allows an object to be
# called just like a function. It also causes the callable built in function to return True for such an instance

class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


