#the old way to initialise a parent class from a child class is to directly call the parent class' __init__ method
# with the child instance

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

#this approach works fine for simple hierarchies but breaks down in many cases.
# if your class is affected by multiple inheritance (something to avoid in general, item 26), calling the superclass' __init__
# methods directly can lead to unpredictable behavior.

# one problem is that the __init__ call order isn't specified across all subclasses. For example, here I define 2 parent classes that
# operate on the instances value field.

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

# This class defines its parents classes in one ordering.

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# and constructing it produces a result that matches the parent class ordering.

foo = OneWay(5)
print('First ordering is (5*2) + 5 = ', foo.value)

# heres another class that defines the same parent classes but in a different ordering:

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

#however the calls to the parent class constructors (PlusFive.__init__ and TimesTwo.__init__) is in the same order as before.
# this causes the class' behaviour not to match the order of the parents classes in its definition

bar = AnotherWay(5)
print('Second ordering still is ', bar.value)

#another problem occurs with diamond inheritance. Diamond inheritance happens when a subclass inherits from two separate classes
#that have the same superclass somewhere in the hierarchy. Diamond inheritance causes the common superclass' _init__ method to
# run multiple times, causing unexpected behaviour. E.G.

# we define two child classes that inherit from MyBaseClass

class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

# then define a child class that inherits from both of these classes, making MyBaseClass the top of the diamond.
#need to make a map of parent, super and child classes, i.e. all inheritance.

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

bep = ThisWay(5)
print('Should be (5*5) + 2 = 27 but is ', bep.value)

# the output shoud be 27, but the call to the second parent class' constructor, PlusTwo.__init__, causes self.value to be reset back
#  to 5 when MyBaseClass.__init__ gets called a second time.

#here we create the diamond shaped hierarchy again, but this time using super (in python 2 for now) to initialise the parent class

class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5

class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value +=2

# now the top part of the diamond, MyBaseClass.__init__ is only run a single time. the other parent classes are run in the order
#specified in the class statement

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)

gih = GoodWay(5)
print('should be 5 * ( 5 + 2 ) = 35 and is ', gih.value)

#shouldnt this be the opposite way round? because TimesFive is called first? no. GoodWay called in turn calls
# TimesFiveCorrect.__init__, which calls in turn PlusTwoCorrect.__init__ which calls MyBaseClass.__init__.
# once this reaches the top of the diamond, then all of the initialisation methods actually do their work in the opposite order
# from how their init functions were called.

#two problems with Python 2 is that the syntax is a bit verbose. you have to specify the class youre in, the self object,
#  the method name (usually __init) and all the arguments

# you also have to specify the current class by name in the call to super. if you ever change the class', a very common
# activity when improving a class hierarchy - you also need to update everty call to super.

# Python 3 fixes these issues by making calls to super with no arguments equivalent to calling supper with __class__ and self specified.

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)

class Implicit(MyBaseClass):
    def __init__(self, value)
        super().__init__(value * 2)

# this works because python 3 lets you reliably reference the current class methods using the __class__ variable. This doesnt work in
# python 2 because __class__ isnt defined. you may guess that your could use self.__class__ as an arg to super, but this breaks
# due to the way super is implemented in Python2.






