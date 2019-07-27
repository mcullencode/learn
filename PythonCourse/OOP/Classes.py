"""until now we've been using imperative programming.
imperative programming contains a series of instructions for computer to follow in defined order.
OOP - aims to combine data and the processes that act on that data into objects which is called encapsulation
"""

#imperative programming analogous to a recipe, starts with ingredients and utensils needed, corresponding to data.
#and continues with a list of steps that must e performed on the data to produce the meal

#OOP relies on the objects, such as milk eggs etc knowing how to perform certain operations.
#good example of encapsulation is self lighting cigarettes.
#steps for smoking cig, light match, hold match to cig, inhale.
#OOP would be, place cig in mouth, inhale, the way the cig is lighted is not concerned by user.

#kettle example, step 1 fill kettle, step 2, put kettle on stove, etc, then there has to be a function to monitor water.
#in OOP terms, kettle has a boil method, which is operated by a switch. step 1 turn on kettle, kettle turns off when ready

#so using OOP is easier for the user, but the construction requires more effort.

#everything in python is an object. as seen below, a has an add method

# a = 12
# b = 4
#
# print(a+b)
# print(a.__add__(b))

# class Kettle(object):
#     def __init__(self, make, price):
#         self.make = make
#         self.price = price
#         self.on = False
#         # class is a template, from which objects can be created. i.e. kettles can be created with their own name and price.
#         # each different kettle is a different instance.
#
#         #create a kettle called kenwood, this is an instance of the class. all objects created from this class will share same characteristics, i.e. a name and a price
#         #an instance is another name of an object created from a class definition. kenwood is an object of type kettle.
#
#
# #instance number 1
# kenwood = Kettle("Kenwood", 8.99)
#
# print(kenwood.make)
# print(kenwood.price)
#
# kenwood.price = 12.75
# print(kenwood.price)
#
# #instance number 2
# hamilton = Kettle("Hamilton", 14.55)
#
# #attributes are the price and make. when a variable is bound to an instance of a class, its a data attribute.
# #attributes also known as fields.
#
# print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
# print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. all objected created using the same class will have the same characteristics
Object: an instance of a class.
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class
"""


#clean start
# main difference between a method and a function is this self parameter

class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

    #self is a reference to the instance of the class

#instance number 1
kenwood = Kettle("Kenwood", 8.99)

kenwood.price = 12.75

hamilton = Kettle("Hamilton", 14.55)

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

#term constructor refers to the special method that is executed when the instance of a class is created or constructed
# in python, this is __init__

#equal to lines above.
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

kenwood.power = 1.5
print(kenwood.power)
#gives an error, as hamilton instance does not have power attribute print(hamilton.power)

#classes also have attributes. data attributes in kettle example, are instance attributes.
#introduce a class attribute called power share, as above

print("Switch to atomic power")
Kettle.power_source = "atomic"

print(Kettle.power_source)
print('SWITCH KENWOOD TO GAS')
kenwood.power_source = "gas"
#kenwood_dict now has a shadow attribute
print(kenwood.power_source)
print(hamilton.power_source)



print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

#encapsulation: main idea is that objects contain the data and the methods that operate on that data, and dont expose the actual implementation.
#OOP isnt the only way to achieve this. 

