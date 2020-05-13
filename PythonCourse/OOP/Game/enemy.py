import random
#class Enemy(object):
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
        self.max_points = hit_points

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            self._hit_points = self.max_points

            if self._lives > 0:
                print("{0._name} lost a life".format(self))
                self._hit_points = self.max_points
            else:
                print("{0._name} is dead".format(self))
                self._alive = False




    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    #once an init method is added to the subclass, the subclass no longer uses the superclass constructor.

    def __init__(self, name):
        #super(Troll, self).__init__( name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me stupid {0._name}. {0._name} stomp you".format(self))


#imolmeneting overriding methods in superlass, i.e vampyres dodging take damage

class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3 , hit_points=5)

    def hiss(self):
        print("Me scary vampire {0._name}".format(self))

    def dodges(self):
        if random.randint(1,3) == 3:
            print(' *** {0._name} dodges ***'.format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        #i.e. if vampyre does not succeed to dodge, the take_damage method reverts back to super class
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140



    def take_damage(self, damage):
        #the super method we're calling here is actually the
        #Vampyre take damage
        super().take_damage(damage=damage // 4)









