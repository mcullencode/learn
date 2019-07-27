#dictionaries are unordered, but by key value pairs. dictionaries and sets items are not acccessed by strings

# fruit = {"orange": "a sweet, orange, citrus cruit",
#          "apple": "good for making cider",
#          "lemon": "sour yellow fruit"}
# # #
# # print(fruit)
# # print(fruit["lemon"])
#
# # bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
# # print(bike["engine_size"])
# # print(bike["colour"])
# # #can add
# # fruit["pear"] = "an odd shaped apple"
# # #can update
# # fruit["pear"] = "no"
# # print(fruit)
#
# # fruit.clear()
# # print(fruit)
#
# #cannot have multiple entries with same key so
# # data = {"first":"1", "second": "2", "first":"5"}
# # print(data)
#
# print(fruit)
# while True:
#     dict_key = input("please enter fruit")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("no " + dict_key + 's')
#
#can use dict_key in fruit as above, or default return value below
# while True:
#     dict_key = input("please enter fruit")
#     if dict_key == "quit":
#         break
#     #can add a default value to return if the key doesnt exist
#     description = fruit.get(dict_key, "We dont have a " + dict_key)
#     print(description)

#all dicts print out in same order, whilst if you run separately, order isnt consistent
# for i in range(10):
#     for snack in fruit:
#         print(snack + "is" + fruit[snack])
#     print('-' * 15)

# ordered_keys  = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + '-' + fruit[f])

# print(fruit.keys())
# print(fruit.values())
# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)
#
# myList = ["a", "b", "c", "d"]
# print(myList)
#
# newString = ''
# for c in myList:
#     newString += c + ', '
#
# print(newString)
#
# #orrr
#
# newString = ", ".join(myList)
# print(newString)
#
# letters = "abcdefghijklmnopqrstuvwxyz"
# newerString = ", ".join(letters)
# print(newerString)

locations = {0:"You are sitting in front of a computer learning python",
             1: "You are standing at end of a road before small brck building",
             2: "Top of a hill",
             3: "inside a buiding, a well house for stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits =  {0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S": 1, "Q": 0}}

vocab = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W"}


# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))
# loc = 1
# while True:
#     availableExits = ', '.join(exits[loc].keys())
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + "").upper()
#     if len(direction) > 1:
#         words = direction.split()
#         for word in words:
#             if word in vocab:
#                 direction = vocab[word]
#                 break
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")
fruit = {"orange": "a sweet, orange, citrus cruit",
         "apple": "good for making cider",
         "lemon": "sour yellow fruit"}


veg = {"cabbage": "every childs fav",
       "sprouts": "lovely",
       "spinach": "can i have some more fruit"}

veg.update(fruit)
#returns none
print(veg.update(fruit))
print(veg)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)



