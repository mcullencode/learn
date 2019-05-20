"""We will now demonstrate how we can define methods in classes. Lets define a function hi, which takes an object obj
 as an argument and assumes that this object has an attribute 'name'"""

def hi(obj):
    print('Hi, I am ' + obj.name + '!')

class Robot:
    pass

x = Robot()
x.name = 'Marvin'
hi(x)

# we can now bind the function 'hi' to a class attribute 'say_hi'

class Robot2:
    say_hi = hi

x2 = Robot2()
x2.name = 'Marvin'
Robot2.say_hi(x)

"""It is possible to define methods like this but you shouldnt do it. The proper way is:
 Instead of efining function outside class and binding it to class attribute, define a method directly inside the class
 A method is just a function which is defined in a class
 The first parameter is used as a reference to the calling instance, usually called self
 self corresponds to the robot object x"""

"""we have seen that a method only differs from a function in two aspects:
it belongs to a class and is defined in a class AND the first parameter in the definition of the method, has to be a reference
to the instance, which called the method. This parameter is usually called self. """

"""Most other object oriented languages pass the reference to the object (self) as a hidden parameter to the methods.

For a class C, an instance of C, x and a method m of C, the three ways of calling the method are equivalent

type(x).m(x, ...)
C.m(x, ...)
x.m(...)

There is more than one thing about this code, which may disturb you, but the essential problem at the moment is the fact 
that we create a robot and that after the creation, we shouldn't forget about naming it! If we forget it, say_hi will 
raise an error. 
We need a mechanism to initialize an instance right after it's creation..."""

"""We want to define the attributes of an instance right after its creation. __init__ is a method which is immediately 
and automatically called after an instance has been created. This name is fixed and it is not possible to chose another
 name. __init__ is one of the so-called magic methods, of which we will get to know some more details later. The __init__ 
 method is used to initialize an instance. There is no explicit constructor or destructor method in Python, as they are 
 known in C++ and Java. The __init__ method can be anywhere in a class definition, but it is usually the first method 
 of a class, i.e. it follows right after the class header."""

class Robot3:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi my name is " + self.name)
        else:
            print("Hi i am a robot without a name")

x3 = Robot3()
x3.say_hi()
y3 = Robot3("Marv")
y3.say_hi()


