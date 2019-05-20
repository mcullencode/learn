"""Data Abstraction, Data Encapsulation and Information Hiding are often synonymously used in books and tutorials on OOP
. But there is a difference. Encapsulation is seen as the bundling of data with the methods that operate on that data.
 Information hiding on the other hand is the principle that some internal information or data is "hidden", so that it
 can't be accidentally changed. Data encapsulation via methods doesn't necessarily mean that the data is hidden. You
 might be capable of accessing and seeing the data anyway, but using the methods is recommended. Finally, data abstraction
  is present, if both data hiding and data encapsulation is used. This means data abstraction is the broader term:

Data Abstraction = Data Encapsulation + Data Hiding """

"""Encapsulation is often achieved by providing two kinds of methods for attributes: The methods for retrieving or accessing
the values of attributes are called getter methods. Getter methods do not alter the values of attributes. The ethods used for 
changing the values of attributes are called setter methods."""

class Robot:

    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi I am " + self.name)
        else:
            print("I am a robot with no name")

        if self.build_year:
            print("I was born in" + str(self.build_year))
        else:
            print("I was born never")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, build_year):
        self.build_year = build_year

    def get_build_year(self):
        return self.build_year()


x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()



