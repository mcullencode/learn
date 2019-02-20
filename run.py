from Classes import Robot

r1 = Robot(str(35), 'Steve Mavin', str(40))


#r1.introduceself()

r2 = Robot(str(35), 'Fleve Havin', str(50))



class Person:
    def __init__(self, name, personality, issitting):
        self.name = name
        self.personality = personality
        self.issitting = issitting

    def sit_down(self):
        self.issitting = True

    def stand_up(self):
        self.issitting = False


p1 = Person("alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)


#defining new attribute in p1 called robot_owned and sets it to r2

p1.robot_owned = r2

p2.robot_owned = r1

p1.robot_owned.introduceself()