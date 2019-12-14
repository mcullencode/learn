class Player(object):

    def __init__(self, name):
        self. name = name
        self._lives = 3
        self._level = 1
        self._score = 0

#first step in challenge, create a property for level, create getter and setter to
#  create a score as the level changes. need to create a property called level, so first thing to do is hide the level
# attribute by adding an underscore   '_level'

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        self._lives = lives
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("level cant be less than one ")

    level = property(_get_level, _set_level)

#going to use decortators instead of previous syntax for properties.
#begin by hiding our score attribute. rename score variable to _score


#we hide the lives data attribute by prexifing it with an underscore, good practice
#hiding the methods by adding underscore

    #provided name of methods below, i.e. _get_lives. if you add () at the end, then you are calling
    #method and the properties getter will be set to whatever the result of get_lives is, almost certainly ot anything useful


    lives = property(_get_lives, _set_lives)

    # going to use decortators instead of previous syntax for properties.
    # begin by hiding our score attribute. rename score variable to _score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

#READ DOCS ON PROPERTIES


    def __str__(self):
        #using object attributes, i.e. object(0).name, via importing self.
        return "Name: {0.name}, Lives: {0.lives}, level: {0.level}, Score {0.score}".format(self)
        #identical
        #return "Name: {0}, Lives: {1}, Level: {2}, Score: {3}".format(self.name, self.lives, self.level, self.score)



