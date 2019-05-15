"""Four major principles of object oriented programming are : Encapsulation, Data Abstraction, Polymorphism, Inheritance.
Consider a library full of books, newspapers, films etc. Generally there are two stock methods to keeping stock in a library.
You can use a closed access method, where the stock are not displayed on open shelves and trained staff retrieve things. Another
way is open access also known as open shelves. Imperative languages like C could be seen as open access shelving libraries.
Its up to the user to find the book and put it back in the right place. Closed access can be compared to OOP. The analogy can be
 seen like this, the books which the library offer are like the data in an object oriented program. Access to the books is restricted
 like access to the data in OOP. The staff function like the methods in OOP, which control access to the data. So the data, often
 called attributes, in such a program can be seen as being hidden and protected by a shell, and it can only be accessed by special
 functions, usually called methods. Putting the data behind a shell is called encapsulation. So a library can be regarded as a class
 and a book is an instance or an object of the class. Generally speaking, an object is defined by a class. A class is a formal
 description of how an object is designed, i.e. what methods and attributes it has. These objects are called instances as well.
 The expressions are in most cases used synonymously. A class should not be confused with an object."""

"""By this, I meant that I wanted all objects that could be named in the language (e.g., integers, strings, functions, classes, 
modules, methods, and so on) to have equal status. That is, they can be assigned to variables, placed in lists, stored in 
dictionaries, passed as arguments, and so forth." (Blog, The History of Python, February 27, 2009) This means that "everything"
 is treated the same way, everything is a class: functions and methods are values just like lists, integers or floats.
  Each of these are instances of their corresponding classes."""

"""recap. methods are a way of acessing the 'data'. the data, often called attributes, in such a case they can be seen as hidden or 
 protected by a shell, known as encapsulation. only accessible by special functions, or methods. Book or bit of data is an instance 
 or an object of the class"""

"""a class could have attribute of name, and an instance of this is steve."""

x = 42
print(type(x))

y = 4.24
print(type(y))


class Robot:
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)

# We have created two different robots x and y in our example. Besides this, we have created a reference y2 to y,
# i.e. y2 is an alias name for y. The output of this example program is below.


"""We can dynamically create arbitrary new attributes for existing instances of a class. We do this by joining an arbitrary
 name to the instance name, separated by a dot ".". In the following example, we demonstrate this by created an attribute 
 for the name and the build year: """


class Robot2:
    pass

if __name__ == "__main__":
    x2 = Robot2()
    y2 = Robot2()

x.name = "Marvin"
x.build_year = "1972"

y.name = "Steve"
y.build_year = "1800"

print(x.name)
print(y.build_year)

"""As we have said before: This is not the way to properly create instance attributes. We introduced this example, 
because we think that it may help to make the following explanations easier to understand. """

"""If you want to know, what's happening internally: The instances possess dictionaries __dict__, which they use 
to store their attributes and their corresponding values: """

""""
>>> x.__dict__
{'name': 'Marvin', 'build_year': '1979'}
>>> y.__dict__
{'name': 'Caliban', 'build_year': '1993'}
"""

"""Attributes can be bound to class names as well. In this case, each instance will possess this name as well. 
Watch out, what happens, if you assign the same name to an instance: It gets confusing"""

class Robot3(object):
    pass

x = Robot3()
Robot3.brand = "Kuka"

print(x.brand)

x.brand = "Thales"
print(Robot3.brand)

y = Robot3()
print(y.brand)

Robot3.brand = "Thales"
print(y.brand)

print(x.brand)

#have a look at the dictionaries to see whats going on

print(x.__dict__)
print(y.__dict__)
print(Robot3.__dict__)

#If you try to access y.brand, Python checks first, if "brand" is a key of the y.__dict__ dictionary. If it is not,
# Python checks, if "brand" is a key of the Robot.__dict__. If so, the value can be retrieved.

# If an attribute name is not in included in either of the dictionary, the attribute name is not defined.
# If you try to access a non-existing attribute, you will raise an AttributeError: I.E

#print(x.energy) gives attribute error

# you can prevent this error by using the getattr, if you provide a default value as the third argument

print(getattr(x, 'energy', 100))

"""Binding attributes to objects is a general concept in Python. Even function names can be attributed. 
You can bind an attribute to a function name in the same way, we have done so far to other instances of classes: """

def f(x):
    return 42

f.x = 42

print(f.x)

"""This can be used as a replacement for the static function variables of C and C++, 
which are not possible in Python. We use a counter attribute in the following example: """


def g(x):
    g.counter = getattr(g, "counter", 0) + 1
    return "Monty Python"


for i in range(10):
    g(i)

print(g.counter)

"""If you call this little script, it will output 10. 

There may some uncertainty arise at this point. It is possible to assign attributes to most class instances, but this has nothing to do with defining classes. We will see soon how to assign attributes when we define a class. 

To properly create instances of classes we also need methods. You will learn in the following subsection of our Python tutorial, how you can define methods. """

