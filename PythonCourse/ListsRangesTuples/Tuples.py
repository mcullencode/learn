#tuples are immutable. ie cant append or alter.
# people say that lists are enclosed in square brackets which is true,
# and tuples are enclosed in parantheses, that is not true. a comma is used to separate the
#elements in a tuple, but the parantheses are only required when necessary to remove syntactic
# ambiguity. i.e.

# t = "a", "b", "c"
#
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))


welcome = "welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981

print(welcome)
print(welcome[0])

##welcome[0] = "master" gives error.
#tuples support indexing or slicing, so can update like below

budgie = budgie[0], "BUDGIE", budgie[2]

#so here we created a new tuple and pointed the variable to reference it
#so why use a tuple?  one reason is that in cases where you dont want data accidentally altered, prevents bugs

#unpacking the tuple

# song, artist, year = budgie

#tuple within tuple
imelda = "More Mayhem", "Imilida May", 2011, (
    (1, "Pulling The Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town"))

title, artist, year, tracks = imelda

print(title)
print(tracks)
