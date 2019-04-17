# say you want to sort a list of numbers but prioritize one group of numbers to come first. This is important for uses like
# UI when you want to display import messages or exceptional events to be displayed before everything else.

# a common way to do this is to pass a helper function as the key argument to a lists sort method. the helpers return value will be used
# as the value for sorting each item in the list. the helper can check whether the given item is in the important group and can
# vary the sort key accordingly.

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return(0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sort_priority(numbers, group)
print(numbers)

# 3 reasons why this work.

# Python supports closures: functions that refer to variables from the scope in which they were defined.
# This is why the helper function is able to access the group argument to sort_priority

#Functions are first class objects in Python, meaning you can refer to them directly, assign them to variables, pass them
# as arguments to other functions, compare them in expressions and if statements etc. This is how the sort method can accept
# a closure function as the key argument

#python has specific rules for comparing tuples. It first compares items in index zero, then index one, index two etc. This is why the
# return value from the helper closure causes the sort order to have two distinct groups.


#It'd be nice if this function returned whethe higher-priority items were seen at all so the user interface code can act accordingly.

#here we try to do this in an obvious way

def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

#so found result is wrong, as the numbers were found and sorted correctly. why?

#when you reference a variable in an expression, the python interpreter will traverse the scope to resolve the reference in this order:

# the current functions scope
#any enclosing scopes (like other containing functions)
# the scope of the module that contains the code (also called the global scope)
# the built in scope (that contains functions like len and str)

# if none of these places have a defined variable with the referenced name, then a NameError exception is raised

#assigning a value to a variable works differently. if the variable is already defined in the current scope, then it will just take on the new value
# if the variable doesnt exist in the current scope, then Python treats the assignment as a variable definition.
# the scope of the newly defined variable is the function that contains the assignment

# this assignment behaviour explains the wrong return value of found in the sort_priority2 func.  The found variable is assigned to True
# in the helper closure. the closures assignment is treated as a new variable definition within helper,
# not as an assignment within sort_priority2

# encountering this problem is called the scoping bug. however it is not a big, it is the intended result. this behavour results local
#  variabes in a function from polluting the contaiing module otherwise every assignment within a function would put garbage into
# the global module scope.

#in python 3 there is a special syntax for getting data out of a closure. The nonlocal statement is used to indicate that scope
#  traversal should happen upon assignment for a specific variable name

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key = helper)
    return found

# the nonlocal statement makes it clear when data is being assigned out of a closure into another scope.
# when usage of nonlocal gets complicated, its best to use a helper class.

class Sorter(object):
    def __init__(self, group):

        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key = sorter)
assert sorter.found is True


