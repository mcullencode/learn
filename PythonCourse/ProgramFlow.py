
#python itself doesnt have a boolean data type.
# x = "false"
# if x:
#     print("x is true")
#in python true is 1 and false is 0. in a condition, any non zero, or non empty values will evaluate to true.

# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty mapping: {{}}: {7}""".format(False, bool(None), bool(0),bool(0.0), bool([]), bool(()), bool(''), bool({})))

# x = input("Please enter text")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter")

#print(not False)
#print(not True)

# age = int(input("how olf are you"))
# if not(age<18):
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18-age))

parrot = "norwegian blue"

# letter = input("enter character:")
# if letter in parrot:
#     print("Give me an {}, Bob".format(letter))
# else:
#     print("I dont need that letter")

# name = input("gimme name pls")
# age = int(input("gimme age pls"))
#
# if ((age < 31) and (age > 18)):
#     print("you may go on holiday {}".format(name))
# else:
#     print("sorry {} you suck".format(name))

# for i in range(1, 20):
#     print("i is now {}".format(i))

# number = "9,223,372,036,854,775,807"
# for i in range(0,len(number)):
#     print(number[i])

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range(0,len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#         #print(number[i], end = '')
#
# newNumber = int(cleanedNumber)
# print('The number is {}'.format(newNumber))

#python iterates over a variable in a for loop, unlike Java, C etc

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))

# for state in ["not pinin'", "no more", "a stiff", "berefet of life"]:
#     print("This parrot is " + state)
#     #print("This parrot is {}".format(state))

# for i in range(0, 20, 5):
#     print("i is {}".format(i))

# for i in range(1,13):
#     for j in range(1, 13):
#         print("{1} times {0} is {2}".format(i,j,i*j),end = '\t')
#
#     print('========')
#


# divisible=[]
# for i in range(0,101,1):
#     if i % 7 == 0:
#         divisible.append(i)
# print(divisible)
#
# for i in range(101)[::7]:
#     print(i)
#
# # This solution uses a step value for the range function
# for i in range(0, 101, 7):
#     print(i)


# shopping_list = ["milk", "pasta", "eggs", "spam", "bread"]
# for item in shopping_list:
#     #skip spam. continue makes the for loop skip the resr of the block, and restart next loop.
#     if item == 'spam':
#         print("i am ignoring spam")
#         continue
#         print("shouldnt see this")
#     print("buy" + item)


# shopping_list = ["milk", "pasta", "eggs", "spam", "bread"]
# for item in shopping_list:
#     #break terminates the rest of the for loop
#     if item == 'spam':
#         print("i am ignoring spam")
#         break
#         print("shouldnt see this")
#     print("buy" + item)



# in python, char exists outside the for loop iff the for loop is initialised.
#of course this isnt the case in C, where the scope of the variable only exists within the loop.
#can make sure this program executes by merely adding a . to the end of IPAddy, prevents error.
# if IpAddy[-1] != '.':
#     IpAddy += '.'
# segments = 1
# length = 0
#
# IpAddy = input('enter ip address:')
#
# for char in IpAddy:
#     if char == '.':
#         print("segment {} contains {} characters".format(segments, length))
#         segments += 1
#         length = 0
#     else:
#         length += 1
#
# if char != '.':
#     print('segment {} contains {} characters'.format(segments, length))

# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i += 1

# available = ['east', 'neast', 'south']
# chosen = ''
# while chosen not in available:
#     chosen = input("please choose a direction")
#     if chosen == 'quit':
#         print('game over')
#         break
#
# else:
#     print('arent you glad you got out')

import random
highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("please guess higher")
    elif guess > answer:
        print("please guess lower")
    if guess == answer:
        print('congrats')



