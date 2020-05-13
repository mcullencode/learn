a = 3
b = 'tim'
c = 1, 2, 3
print(a)
print(b)
print(c)

"""
although these three objects are int, string, tuple, they all possess
printable behaviour. and in that respect, they behave like a different type
 of object: an object thats printable.

the ability of objects to have different forms is called polymorphism

In this example, the polymorphic behaviour of the objects is implemented
using inheritance. All pyhton objects inherit from a base class called object
which defines a __str__ method.

In java, a statically typed program, the print method calls the integer class'
toString method, to get the string representation of the object. the valueOf 
method delegates the task of deciding what the string representation of each 
class should be, to the class itself. If valueOf just delegates the task to the class,
it doesnt really need to know what class itsdealing with. whatever it gets,
it could call the toString methof and return the result. and thats what python does 

So in this example f making things printable every object can be printed, as well 
as used for whatever else it does. this is possible because every objects automatically
inherits the __str__ method from its object base class


inheritance isnt the only way to implement polymorphism. they can still share some 
properties without inheriting form a base class. i.e. to a juggler, apples and oranges
share similar properties. as does a loaf of bread and an orange, useful to hungry person, 
useless to juggler.

but what about enemies in python? if we wrote a function that accepted enemy as a paramter,
and called take_damage method of its parameter, theres no guarantee that the object that 
we passed to it would have a take_damage method in python. we could pass a player instance to it,
 for example, and we havent given our player class that method.
 
 in java, that wouldnt be a problem, wed have to specify Enemy, say, as the type of the parameter,
 and the compiler would check that anything we passed fif inherit from the Enemy class.
 

In python, theres no such checking, python isnt interested in the type of objects, its only
interested in their behaviour at the time thyre used
let's relate this to python in ducks.py.
"""







