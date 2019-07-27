# jabber = open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/sample.txt", 'r')

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
#
# jabber.close()

#using with enables us to not need to use file.close().
# with open("sameple.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

#this produces a list containing each line
# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# #
# # for line in lines:
# #     print(line, end='')
# for line in lines[::-1]:
#     print(line, end='')

# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/sample.txt", 'r') as jabber:
#     lines = jabber.read()
# for line in lines[::-1]:
#     print(line, end='')

#readline reads a single line from a file, readlines reads the entire file into a list of strings,
#read reads entire file, returns a string containing contents of file, has optiona parameter for specifying how
# much data you want to read






# cities =["Adelaide", "Alice Spring", "Darwin", "Melbourne", "Sydney"]
#
# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/cities.txt", 'w') as city_file:
#     for city in cities:
#         #file=city_file is not an assignment, so cant use x = y, no spaces. the equals
#         # is normally an assignment, its providing a named argument. similar to end=''
#         print(city, file=city_file, flush=True)
#

# cities = []
#
# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/cities.txt", 'r') as city_file:
#     for city in city_file:
#         #to get rid of the \n in the list items
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

#strip takes characters only for beginning or end of string.
#print("Adelaide".strip("A"))

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Puling the Rug"), (2, "Psycho"), (3, "Mayhem"))
#
# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
#
# #now stored as a string, but was once a tuple. can convert it back to string using eval
#
# with open("/Users/mc/Documents/Learn/PythonCourse/InputOutput/imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)

###CHALLENGE write a program to append the times table to jabberwocky poem

with open("/Users/mc/Documents/learn/PythonCourse/InputOutput/sample.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=tables)
        print("-"*20, file=tables)



