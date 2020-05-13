class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee this is fun")
        elif self.ratio == 1:
            print("wow im tired, but still flying")
        else:
            print('fuk')

"""
So in init method of duck class, we create a new wing object and assign it to our _wing 
attribute of the duck class. any duck objects we create will now have their own wing objects
and can use the attributes of the wing, including in this case, the fly method.

when a class contains another obejct like this, its called composition.could have beak, feet classes etc
and the duck could have no attributes of itself, except the ones from the composing classes
 
"""


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("waddle, waddle")

    def swim(self):
        print("come on in, the waters sik")

    def quack(self):
        print('quackin ell')

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("waddle, i do too")

    def swim(self):
        print("water is fukn cold")

    def quack(self):
        print("are you having a laff, im a penguin")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    #
    # percy = Penguin()
    # test_duck(percy)

"""Inheritance results in an "is a" relationship, i.e. vampyre is an enemy.
Composition and Aggregation. Theyre both used when you have a HAS A relationship

I.e. duck has a wing, penguin has a wing."""