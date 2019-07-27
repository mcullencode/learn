#define a set using curly braces, same as dict.

farm_animals = {"sheep", "cow", "hen"}

wild_animals = set(["lion", "tiger", "panther", "elephant"])

farm_animals.add("horse")
#cant create an empty set with empty braces as it creates a dictionary. so to create
#an empty set, you must use the set constructor

even = set(range(0,40,2))
#
squares_tuple = (4,6,9,16,25)
squares = set(squares_tuple)
#
# print(even.union(squares))
#
# print(even.intersection(squares))
# print(even & squares)
#
# #even minues squares
#
# print(sorted(even.difference(squares)))
# print(sorted(even-squares))

print(sorted(even))
print(squares)
#even.difference_update(squares)
print(sorted(even))

#symmetric difference, thought of as the opposite of intersection
print(even.symmetric_difference(squares))

squares.discard(4)
squares.remove(16)
squares.discard(13)
print(squares)
#raises an error below
#squares.remove(8)
#instead

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")




